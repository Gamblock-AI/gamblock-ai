# Alur Sistem Gamblock-AI (Fokus: Role Mahasiswa)

Dokumen ini menjelaskan alur sistem **Gamblock-AI** secara lengkap pada semua
fitur, dengan fokus pada alur **role Mahasiswa** (Mahasiswa Terlindungi).
Referensi otoritas: `context/pkm_proposal.md` (sumber mutlak), domain context
(`architecture.md`, `privacy-security.md`, `glossary.md`), dan status
implementasi per komponen pada `docs/ai/README.md`.

Istilah kemampuan mengikuti label status pada `context/glossary.md`:
`implemented`, `prototype`, `stub`, `not wired`, `planned`, `blocked`.
Dokumen ini hanya melaporkan status yang memiliki bukti pada kode/panduan,
bukan klaim target-state.

---

## 1. Ikhtisar Sistem

Gamblock-AI adalah platform pemblokir judi online **on-device** dan pemulihan
kecanduan untuk mahasiswa universitas Indonesia. Seluruh deteksi dan
inferensi berjalan di perangkat (Edge AI); backend hanya menerima data
non-browsing dan event agregat.

### 1.1 Komponen Sistem

| Komponen | Direktori | Peran dalam alur mahasiswa |
|---|---|---|
| Flutter Client | `gamblock_ai_apps/` | Otoritas blocking Android/Windows: setup, deteksi lokal, blokir, Pattern Interrupt, sinkronisasi agregat |
| Browser Extension | `browser_extension/` | Sensor pasif Windows: ekstrak DOM + URL, relay ke Windows service via loopback WebSocket (tidak klasifikasi/blokir) |
| Website | `gamblock-ai-website/` | Surface recovery & self-regulation: dashboard, check-in, misi, psikoedukasi, Learning Hub, jurnal, weekly review |
| Backend | `gamblock-ai-backend/` | Identitas/auth/RBAC, grup & approval, recovery state, misi, jurnal terenkripsi, support, ekspor data, release |
| Model | `gamblock-ai-model/` | Artifact Hybrid-v2: Rule-Based + Logistic Regression (ONNX) untuk inferensi lokal |
| Infrastructure | `gamblock-ai-infrastructure/` | Deployment backend/website (Ansible + Docker + Caddy), tidak terlibat langsung di alur pengguna |

### 1.2 Prinsip Non-Negotiable

| Prinsip | Implikasi pada alur mahasiswa |
|---|---|
| Privacy by design | URL, DOM, riwayat, screenshot tidak pernah meninggalkan perangkat; backend hanya menerima agregat |
| Extension pasif | Extension hanya relay ke loopback lokal; tidak pernah memblokir/mengalihkan/menutup tab |
| Blokir otoritas di client | Android (Accessibility Service) dan Windows (service LocalSystem) yang mengeksekusi blokir & Pattern Interrupt |
| Anti-tamper aman | Tidak menggunakan `RtlSetProcessIsCritical`; Android memakai Accessibility Service, Windows memakai SCM recovery |
| Jurnal terenkripsi | Teks jurnal/refleksi dienkripsi AES-256-GCM sebelum persistensi; fail closed |

---

## 2. Peta Fitur Mahasiswa

| Fitur | Komponen | Status |
|---|---|---|
| Onboarding 3 langkah (guest → login/register → dashboard) | Flutter | `implemented` (prototype code-complete) |
| Registrasi email + password | Flutter, Backend | `implemented` |
| Google OAuth login/link | Flutter, Backend, Website | `implemented` (Android butuh OAuth client nyata; Windows perlu bukti VM) |
| Verifikasi telepon via WhatsApp (Fonnte) | Backend | `implemented` |
| Verifikasi email + reset password (12 karakter) | Backend, Website | `implemented` |
| Setup perlindungan Android (Accessibility Service) | Flutter (Android native) | `implemented` (prototype code-complete, butuh bukti perangkat) |
| Setup perlindungan Windows (extension + service) | Extension, Flutter (Windows native) | `implemented` (prototype code-complete, butuh build/VM) |
| Hybrid Analysis (rule + Logistic Regression) lokal | Flutter (native), Model | `prototype` (artifact terlatih, belum dievaluasi) |
| Blokir + counter agregat offline | Flutter (native) | `implemented` (prototype) |
| Pattern Interrupt 5–10 detik | Flutter (native) | `implemented` (code path, butuh bukti perangkat) |
| Handoff web pemulihan (`/post-intervention`) | Flutter, Website | `implemented` |
| Dashboard mahasiswa | Website | `implemented` |
| Intention (niat perubahan) | Website, Backend | `implemented` |
| Mood/urge check-in harian | Website, Backend | `implemented` |
| Daily missions (5 slot, 10 EXP, custom) | Website, Backend | `implemented` |
| Psychoeducation (dokumen bilingual) | Website, Backend | `implemented` |
| Learning Hub / skills (22 program, 5 cluster) | Website, Backend | `implemented` |
| Recovery room + grounding + jurnal terenkripsi | Website, Backend | `implemented` |
| Weekly review | Website, Backend | `implemented` |
| Progress 7/30/90 hari | Website, Backend, Flutter | `implemented` |
| Accountability: group + approval removal | Website, Backend | `implemented` |
| Quick approval (token single-use) | Website, Backend | `implemented` |
| Emergency recovery (dual-admin) | Website, Backend | `implemented` |
| Support tickets | Website, Backend | `implemented` |
| Data export ZIP terenkripsi + penghapusan akun | Website, Backend | `implemented` |
| Sinkronisasi agregat & device heartbeat | Flutter, Backend | `implemented` |

---

## 3. Alur A: Onboarding & Autentikasi

### 3.1 Instalasi dan Intro

1. Mahasiswa mengunduh aplikasi Flutter (Android) atau menjalankan installer
   Windows.
2. Aplikasi membuka intro 3 langkah yang mempersistenkan status setup.
3. Route onboarding mengarahkan guest ke halaman **login/register** dan
   mahasiswa yang sudah terautentikasi ke **dashboard**.
4. Role akun yang diterima client **hanya `user`** (mahasiswa). Role lain
   ditolak sebelum token dipersistensikan.

### 3.2 Registrasi Akun

1. Mahasiswa mengisi **email + password** (dengan kontrol visibilitas/autofill).
2. Backend membuat akun role `user`; kata sandi diverifikasi dengan Argon2id.
3. **Verifikasi telepon** (gate utama akun) dilakukan via kode sekali pakai yang
   dikirim WhatsApp melalui adapter **Fonnte**. Email tetap identitas login.
4. Verifikasi email didukung dengan refresh/resend dan link verifikasi.
5. Alternatif: **Google OAuth** (ID-token dengan allowlist audience + nonce
   validasi). Akun Google dengan email sama bisa di-link setelah autentikasi
   password saat ini (Android: butuh OAuth client/signing nyata; Windows: butuh
   bukti VM).

### 3.3 Login dan Sesi

1. Login via email+password, Google, atau `dev-login` (khusus development).
2. Backend menerbitkan **JWT access token** + **refresh token berotasi**;
   `auth_time` utama dipertahankan melalui rotasi.
3. Status disabled/role divalidasi ulang per request.
4. Akun yang diprovisioning admin mendapat **password sementara** dan wajib
   menyelesaikan **first-login password change** (jendela 10 menit, purpose-
   specific) sebelum sesi normal disimpan.
5. Logout mencabut sesi; reset password mencabut sesi terkait.

---

## 4. Alur B: Setup Perlindungan Perangkat

Tujuan: mengaktifkan otoritas blocking lokal dan menautkan perangkat ke akun.

### 4.1 Android

1. Mahasiswa mengaktifkan **Accessibility Service** (Android) untuk sensing
   Chrome/Edge.
2. Client mendaftarkan perangkat ke backend (`POST /devices`), memperoleh
   device instance dan kepemilikan perangkat.
3. **Artifact model Hybrid-v2** (ONNX) + ruleset + fixtures dimuat dari aset
   lokal dengan hash terverifikasi; artifact korup ditolak dan versi known-good
   dipertahankan.
4. **Self-test perlindungan** tersedia untuk memverifikasi jalur sensing →
   keputusan.

### 4.2 Windows

1. Mahasiswa menginstal **browser extension** dan memasukkan **pairing token**
   pada halaman `options` (token disimpan di `chrome.storage.local`).
2. Windows service (LocalSystem + SCM recovery) berjalan sebagai otoritas;
   status diperkuat tanpa mekanisme critical-process.
3. Extension merelay data hanya melalui **loopback WebSocket terautentikasi**
   (`ws://127.0.0.1:9090`) dengan keepalive/reconnect.
4. Client menautkan state DPAPI, pipe logon-SID ke agent user-session, dan
   bridge Flutter.
5. Jika extension terputus, Windows menampilkan status **degraded**.
6. Self-test perlindungan tersedia seperti pada Android.

---

## 5. Alur C: Perlindungan Real-Time

Alur inti: **akuisisi input → analisis hybrid lokal → keputusan → blokir &
Pattern Interrupt → handoff pemulihan** — seluruhnya tanpa mengirim data
browsing keluar perangkat.

### 5.1 Akuisisi Input Lokal

- **Android:** Accessibility Service menangkap karakteristik URL + teks DOM
  (title, heading, anchor text) dari permukaan yang didukung.
- **Windows:** Extension mengekstrak teks DOM + URL lalu merelay ke Windows
  service via loopback WebSocket.

### 5.2 Preprocessing dan Analisis Hybrid

1. Input dinormalisasi (Unicode, case, tokenisasi, whitespace, batas fitur)
   mengikuti aturan yang sama antara training dan runtime.
2. Dua jalur paralel dievaluasi:
   - **Rule branch:** karakteristik URL eksplisit + keyword match (bobot 0.25).
   - **Model branch:** Bag-of-Words → Logistic Regression lokal (bobot 0.75).
3. Fusion policy menggabungkan kedua skor; keputusan diambil dengan threshold
   `0.4` (artifact Hybrid-v2; butuh kalibrasi berbukti).
4. Keputusan dijalankan di **client/service**, bukan extension/backend.

### 5.3 Keputusan dan Aksi

- **Positif (judi):**
  1. Blokir akses secara lokal.
  2. Increment **counter agregat** offline-capable (bounded, tanpa URL/DOM).
  3. Tampilkan **Pattern Interrupt 5–10 detik** (non-klinis, mendukung reduced
     motion; di Android dan Windows).
  4. Setelah interupsi, tawarkan **handoff web pemulihan** `/post-intervention`
     yang mengirim hanya **locale + kategori sumber tetap** — tanpa URL, DOM,
     atau skor.
- **Negatif/uncertain:** safe fallback (tidak diblokir, tidak ada intervensi).
- **Backend tidak tersedia:** blokir dan Pattern Interrupt tetap berjalan
  (offline-first).

### 5.4 Sinkronisasi Agregat

1. Event agregat disimpan di antrian offline: hanya kategori yang diizinkan,
   tanggal UTC, hitungan terbatas, device ID opsional, dan idempotency key.
2. Saat online, dikirim ke backend (`POST /client/aggregate-events`) dengan
   ingest idempoten per hari selesai.
3. Backend menyajikan **analytics 7/30 hari** agregat-only; tidak pernah ada
   skema browsing.

---

## 6. Alur D: Recovery Web & Self-Regulation

Alur ini membentuk loop **Self-Regulation Theory**: penetapan tujuan → monitor
diri → evaluasi → penyesuaian perilaku. Seluruh permukaan privasi student.

### 6.1 Dashboard Mahasiswa

- Landing role `user` setelah login (route `/dashboard`).
- Menampilkan ringkasan progress, status proteksi, misi hari ini, dan pintu
  masuk ke modul recovery (progress, recovery, jurnal, education, skills,
  accountability, support, settings).

### 6.2 Intention (Niat Perubahan)

1. Mahasiswa menetapkan **niat/perubahan** pribadi (alasan untuk berubah).
2. Niat bersifat **local-first** di website localStorage; sinkronisasi akun
   bersifat opt-in.
3. Backend menyimpan intention (`GET/POST /intentions`) sebagai recovery data
   privat, bukan kontrak punitif.

### 6.3 Mood / Urge Check-In Harian

1. Form harian berisi **mood 1–5** dan **urge opsional 1–5** (`0` = tidak
   diungkapkan).
2. Dikirim hanya setelah mahasiswa menekan submit (`POST /check-ins`).
3. Check-in memperbarui hari `Asia/Jakarta` berjalan tanpa backfill; privasi
   dijaga (tidak otomatis terlihat partner).

### 6.4 Daily Missions

1. Tersedia **5 slot harian** `Asia/Jakarta`, masing-masing **10 EXP**:
   proteksi aktif, check-in, section edukasi, modul edukasi, recovery practice.
2. Mahasiswa dapat membuat hingga **5 custom mission** privat; judul
   dienkripsi AES-256-GCM saat disimpan.
3. Klaim sistem diverifikasi server; self-attestation custom memakai kontrak
   klaim yang sama (idempoten). Custom self-attestation tidak masuk agregat
   partner/admin.
4. Misus selesai tidak dihapus; bisa diskip/diganti tanpa menghapus progress.

### 6.5 Psychoeducation

- Modul dokumen **bilingual berversi** dengan progress **per revisi**.
- Mahasiswa membaca bagian, menandai progress, dan menjawab check.
- Media (gambar/video/PDF) hanya dari sumber yang di-allowlist backend.

### 6.6 Learning Hub / Skills

- Katalog **22 program UTY, 5 cluster** dengan progress scoped per akun
  (saved/started/completed).
- Checkpoint/refleksi hasil terenkripsi; pemberian 10 EXP sekali per item
  dengan cap harian Jakarta 50.

### 6.7 Recovery Room, Jurnal, dan Grounding

- **Recovery room:** unlock/placement state deterministik (rule version 2,
  tema kedua `sunrise_study` di level 18); hanya practice selesai yang dikirim.
- **Jurnal:** satu refleksi rich-text per hari `Asia/Jakarta` (headings,
  emphasis, lists, quotes, hingga 5 gambar inline privat) — dienkripsi
  **AES-256-GCM** sebelum persistensi; baca/tulis fail closed.
- **Grounding tools:** membantu di luar intervensi.

### 6.8 Weekly Review

- Satu review terenkripsi per minggu Jakarta (`GET/PUT /weekly-reviews/current`)
  yang merestorasi dan upsert.
- Memberikan **10 EXP** idempoten di bawah cap harian bersama.

### 6.9 Progress 7/30/90

- Progress privat menyajikan aktivitas **7/30/90 hari** bertag kategori.
- Tren ditekan di bawah 3 check-in; tidak ada detail browsing di mana pun.

---

## 7. Alur E: Accountability (Pendamping)

Sosial Accountability Protocol: relasi pendamping berbasis persetujuan,
pembagian agregat yang dikontrol mahasiswa, dan proses penghapusan ber-friction
tinggi tanpa melanggar OS.

### 7.1 Invitasi dan Keanggotaan Grup

1. Partner (terverifikasi) membuat grup dan **mengundang** mahasiswa via email
   (invitasi terikat email, **7 hari** masa berlaku).
2. Mahasiswa menerima invitasi dan mengonfirmasi → menjadi member.
3. Alternatif: mahasiswa **join via kode grup** — halaman preview memperlihatkan
   ringkasan grup sebelum bergabung (`POST /accountability/groups/join`).

### 7.2 Pembagian Agregat

- Mahasiswa mengontrol **4 kategori pembagian agregat** (`PATCH
  /accountability/memberships/:id/sharing`).
- Partner hanya melihat total `block_count_sync` agregat 7 hari + preferensi
  pembagian — **tidak pernah** URL, DOM, jurnal, mood, atau detail recovery.

### 7.3 Persetujuan Penghapusan (Removal)

1. Mahasiswa mengajukan permintaan keluar/removal (`approval-request`).
2. Partner memutuskan **approve/deny/expiry** (butuh recent-auth ≤15 menit).
3. Jalur:
   - **Normal exit:** dapat **dibatalkan** oleh mahasiswa sebelum diputuskan.
   - **Unsafe exit:** langsung dan di-review support.
4. Keputusan partner tervalidasi dari state otoritatif backend; client
   menjalankan aksi terkontrol.

### 7.4 Quick Approval

- Backend menerbitkan **token single-use** ber-entropi tinggi (24 jam, hash
  disimpan).
- Partner meresolusi request tertentu via `/approve/[token]` tanpa sesi normal.

### 7.5 Emergency Recovery

- Jalur sempit untuk kehilangan akses partner/perangkat (bukan bypass biasa).
- Mahasiswa mengajukan request; **satu admin** meninjau dan **admin kedua**
  yang menerbitkan dalam jendela 30 menit.
- Kunci terikat perangkat, single-use 24 jam, menghasilkan grant 10 menit.

---

## 8. Alur F: Manajemen Akun & Data

### 8.1 Profil, Settings, dan Password

- Mahasiswa melihat/mengubah profil (`/profile`, `PATCH /me`), avatar (WebP 2
  MiB), password (`PATCH /me/password`), dan link akun Google.
- Settings aplikasi: locale, haptics, dan kategori pembagian agregat.

### 8.2 Support Tickets

- Mahasiswa (`user`/`partner`) membuka kasus (`/support`), mengirim pesan
  terenkripsi, dan melihat history.
- Status transisi: waiting-support ↔ waiting-user → resolved → closed. Admin
  hanya membalas dari queue `/admin/tickets`.

### 8.3 Data Export

1. Mahasiswa membuat permintaan ekspor (`POST /data-requests`).
2. Backend membuat **ZIP terenkripsi AES-256-GCM**; unduhan butuh recent-auth
  ≤15 menit dan berlaku 7 hari.
3. Export kedaluwarsa/gagal ditandai unavailable (tidak diiklankan sebagai
  unduhan).

### 8.4 Penghapusan Akun

1. Mahasiswa meminta penghapusan; backend mengirim **token email hashed**
  berlaku 30 menit.
2. Konfirmasi dengan recent-auth menghapus record scoped akun dan
  menganonimkan baris audit/request yang dipertahankan.

---

## 9. Alur G: Sinkronisasi Agregat & Status Perangkat

| Langkah | Endpoint / Mekanisme | Isi yang dikirim |
|---|---|---|
| Daftar perangkat | `POST /devices` | Instance client, kepemilikan device |
| Update status | `PATCH /devices/:id` | Status proteksi |
| Heartbeat | `POST /devices/:id/heartbeat` | Status/kesehatan perangkat |
| Ingest agregat | `POST /client/aggregate-events` | Kategori bounded, tanggal UTC, count, idempotency |
| Ringkasan | `GET /client/dashboard-summary` | Ringkasan scoped user |
| Progress | `GET /client/progress` | Snapshot 7/30/90 (role `user`) |
| Analytics | `GET /client/protection-analytics` | Agregat 7/30 hari, tanpa detail browsing |

---

## 10. Batasan Privasi Semua Alur

| Data | Diperbolehkan keluar perangkat? | Aturan |
|---|---|---|
| URL, domain, DOM text, title, heading, anchor | **Tidak** | Diproses lokal; hanya relay loopback Windows |
| Riwayat browsing, screenshot | **Tidak** | Tidak pernah dikirim ke backend/website/analytics |
| Skor per halaman / fitur | **Tidak** | Tidak disimpan backend |
| Event agregat (kategori, count) | Ya | Allowlist, bounded, non-rekonstruktif |
| Recovery data (intention, check-in, jurnal) | Ya | Sukarela, privat-by-default, jurnal terenkripsi |
| Custom mission title | Ya | Terenkripsi AES-256-GCM |

---

## 11. Ringkasan End-to-End Mahasiswa

| Tahap | Alur | Komponen utama | Status |
|---|---|---|---|
| 1 | Install → intro → register/login/Google | Flutter, Backend | `implemented` |
| 2 | Verifikasi telepon (Fonnte) + email | Backend, Website | `implemented` |
| 3 | Setup proteksi Android/Windows + pairing + artifact | Flutter, Extension | `implemented` (prototype) |
| 4 | Deteksi hybrid → blokir → Pattern Interrupt | Flutter native, Model | `implemented`/`prototype` |
| 5 | Handoff `/post-intervention` | Flutter, Website | `implemented` |
| 6 | Recovery: intention, check-in, misi, edukasi, skills, jurnal, weekly review | Website, Backend | `implemented` |
| 7 | Accountability: join grup, sharing agregat, removal, quick approval, emergency | Website, Backend | `implemented` |
| 8 | Support, export data, penghapusan akun | Website, Backend | `implemented` |
| 9 | Sinkronisasi agregat & heartbeat | Flutter, Backend | `implemented` |

---

## 12. Lampiran: Referensi Kunci

| Komponen | File/area kunci |
|---|---|
| Flutter client | `lib/features/{intro,setup,auth,protection,pattern_interrupt,recovery,accountability,analytics,missions,journey,settings}/`, `windows/service/`, `android/` |
| Browser extension | `content_script.js`, `background/`, `options.js`, `manifest.json` |
| Website | `app/[locale]/`, `routes.ts`, `proxy.ts`, `hooks/`, `lib/api-client.ts` |
| Backend | `internal/routes/routes.go`, `internal/handler/`, `internal/service/`, `internal/crypto/aes.go`, `internal/i18n/messages.go` |
| Model | `models/gamblock_logistic_regression.onnx`, `gambling_keywords.json`, `gamblock_hybrid_metadata.json` |
| Konteks | `context/{architecture,privacy-security,research-evaluation,glossary,pkm_proposal}.md` |

Glossary lengkap ada di `context/glossary.md`. Otoritas produk ada di
`context/pkm_proposal.md`.
