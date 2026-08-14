# Alur Website & Mobile Client Gamblock-AI (Crosscheck)

Dokumen ini menjelaskan **alur pengguna pada dua permukaan frontend** —
**website** (`gamblock-ai-website/`, Next.js) dan **mobile/desktop client**
(`gamblock_ai_apps/`, Flutter Android/Windows) — beserta hasil **crosscheck**
konsistensi di antara keduanya dan terhadap backend.

Dokumen ini adalah pendamping `ALUR_SISTEM.md` (alur sistem menyeluruh dengan
fokus role Mahasiswa). `ALUR_WEB.md` fokus pada **jalur frontend**: bagaimana
pengguna bergerak antar halaman/screen, apa yang dikirim ke backend, dan di
mana implementasi web vs mobile berbeda atau belum tersambung.

Referensi otoritas: `context/pkm_proposal.md` (sumber mutlak), domain context
(`architecture.md`, `privacy-security.md`, `glossary.md`), status per komponen
pada masing-masing `docs/ai/README.md`. Istilah kemampuan mengikuti label
`context/glossary.md`: `implemented`, `prototype`, `stub`, `not wired`,
`planned`, `blocked`. Setiap klaim didukung bukti `file:line` pada kode/panduan,
bukan klaim target-state.

---

## 1. Ikhtisar Dua Permukaan Frontend

| Permukaan | Direktori | Otoritas blocking? | Role yang dilayani | Fokus utama |
|---|---|---|---|---|
| Website | `gamblock-ai-website/` | Tidak | `user`, `partner`, `admin` | Recovery web, self-regulation, accountability, support, CMS admin |
| Flutter client | `gamblock_ai_apps/` | Ya (Android/Windows) | Hanya `user` (mahasiswa) | Setup proteksi, status perlindungan, Pattern Interrupt, handoff recovery, agregat offline |

Prinsip non-negotiabable tetap berlaku di kedua permukaan: semua klasifikasi
dan blokir berjalan on-device; URL/DOM/riwayat/screenshot tidak pernah keluar
perangkat; extension adalah sensor pasif; website hanya menerima data
recovery yang sukarela + agregat yang diizinkan. Lihat `ALUR_SISTEM.md` §1.2.

### 1.1 Status kemampuan lintas permukaan

| Fitur | Website | Flutter client | Catatan bukti |
|---|---|---|---|
| Intro/onboarding (3 langkah) | — (landing page) | `implemented` | `lib/features/intro/presentation/screens/intro_screen.dart:27` |
| Registrasi email+password | `implemented` | `implemented` | `app/[locale]/(auth)/register/page.tsx:78`; `lib/core/auth/auth_state.dart:178` |
| Verifikasi telepon (Fonnte OTP) | `implemented` | `implemented` | `verify-phone/page.tsx:67`; `auth_state.dart:209` |
| First-login password change | `implemented` | `implemented` | `login/page.tsx:96`; `login_screen.dart:52` |
| Setup proteksi (5 langkah) | — | `implemented` | `lib/features/setup/presentation/screens/setup_screen.dart:74` |
| Pattern Interrupt + handoff | Menerima handoff | `implemented` | `pattern_interrupt_screen.dart:99` |
| Dashboard mahasiswa | `implemented` | `implemented` | `student-dashboard.tsx`; `protection_screen_body.dart:92` |
| Recovery room / jurnal / edukasi / skills | `implemented` | — (kosong) | `lib/features/recovery` tidak berisi kode |
| Daily missions + EXP | `implemented` | — (kosong) | `lib/features/missions` tidak berisi kode |
| Weekly review / progress 7/30/90 | `implemented` | — (web) | Handoff via web |
| Mini-games (4 game, tanpa persist) | `implemented` | `implemented` | 4 game di kedua sisi |
| Accountability (grup/sharing/approval) | `implemented` | `implemented` | `use-accountability.ts`; `accountability_screen.dart` |
| SPK/LLM privacy toggles | `implemented` | `not present` | Hanya error code di `app_messages.dart:276` |
| Aggregat + heartbeat perangkat | — (dikonsumsi) | `implemented` | `lib/core/device/aggregate_sync.dart:7` |

---

## 2. Alur A: Onboarding & Autentikasi (Web vs Mobile)

### 2.1 Perbandingan jalur register → login → dashboard

| Langkah | Website | Flutter client |
|---|---|---|
| 1. Mulai | Landing → CTA `Daftar` (`HeroSection.tsx:43`) | Intro 3 slide → `onboardingProvider.complete()` → `/login` (`intro_screen.dart:58`) |
| 2. Register | `POST /v1/auth/register` role `user`/`partner` dipilih di form (`register/page.tsx:40,160`) | `POST /v1/auth/register` role **hardcoded `user`** (`auth_state.dart:191`) |
| 3. Respon register | Jika `verification_required` → simpan konteks OTP → `/verify-phone` (`:89-91`) | Sama (`register_screen.dart:63-77`) |
| 4. Verifikasi OTP | `origin:'register'` → setelah sukses ke **login** (`verify-phone/page.tsx:84`) | Sama (`verify_phone_screen.dart:91`) |
| 5. Login | `POST /v1/auth/login`; simpan token ke localStorage + cookie (`lib/auth.ts:56`) | `POST /v1/auth/login`; token di secure storage (`auth_state.dart:152`) |
| 6. `verification_required` saat login | Konteks `origin:'login'` → OTP sukses → **langsung dashboard** (`verify-phone/page.tsx:80`) | Sama (`verify_phone_screen.dart:79-86`) |
| 7. First-login (password sementara) | Form inline → `POST /v1/auth/first-login/password` (`login/page.tsx:96-136`) | Mode temp-password (`login_screen.dart:52,72-104`) |
| 8. Setelah login | `defaultRouteForRole` → `/dashboard` untuk semua role (`routes.ts:76`) | `context.go('/dashboard')` (`login_screen.dart:60`) |
| 9. Sesi tersimpan | `localStorage` + cookie `gamblock_access_token` (proxy) | Secure storage; role ≠ `user` ditolak (`auth_state.dart:266`) |
| 10. dev-login | — | Tidak ada (hanya sisa mapping kode `dev_login_failed`) |

**Catatan crosscheck:**
- Website menerima role `partner` di register dan mengarahkan ke `/partners`
  (`register/page.tsx:94-96`); Flutter **hanya** `user`.
- Website tidak punya halaman intro; intro hanya di Flutter.
- Refresh token berotasi di kedua sisi (`lib/api-client.ts:71`;
  `api_client.dart:76`); `auth_time` utama dipertahankan (lihat ALUR_SISTEM §3.3).

### 2.2 Proteksi route website

- `proxy.ts:32` hanya memeriksa **keberadaan cookie** `gamblock_access_token`
  (bukan role); route terproteksi tanpa token → `/login?next=...`
  (`proxy.ts:44-59`).
- Gating role berjalan **client-side** di `DashboardAccessGate`
  (`components/dashboard/dashboard-access-gate.tsx:8-35`) via
  `canAccessDashboardRoute` (`routes.ts:82-105`): `/admin*` admin-only,
  `/support` user/partner, `/skills`, `/mini-games`, `/journal` user-only,
  konsumen `/dashboard|/recovery|/education|/partners|/accountability` untuk
  user/partner.
- Flutter melakukan gating di `go_router` redirect (`router.dart:81-114`) +
  penolakan role pada pemulihan sesi (`auth_state.dart:106-108`).

---

## 3. Alur B: Setup Perlindungan (Flutter; Website tidak terlibat)

1. Setelah login, mahasiswa membuka setup (checklist 5 langkah):
   `setup_screen.dart:74-134`:
   1. **Privacy** — selalu selesai (`:75`).
   2. **Account** — selesai bila `auth.isAuthenticated` (`:81`).
   3. **Device registration** — `ensureDeviceRegistered()` → `POST /v1/devices`
      + enroll grant key (ES256) (`:91`, `device_registry.dart:53-115`).
   4. **Platform setup** — `PlatformBridge.openPlatformSetup()` → Android:
      Accessibility Service; Windows: pairing extension (`:105`,
      `platform_bridge.dart:31`).
   5. **Self-test** — `PlatformBridge.runLocalSelfTest()` (`:122`).
2. Dashboard proteksi (`protection_screen_body.dart:92-146`) menampilkan:
   header profil + status pill, banner status hero, apresiasi mingguan
   (7 hari blokir+intervensi), kartu aksi (setup + self-test), grid 4 sensor
   (service, browser relay, permission/accessibility, model+rules artifact),
   dan kartu accountability.
3. Windows: pairing token di `options` extension; client menautkan DPAPI, pipe
   logon-SID, dan bridge Flutter. Status `degraded` jika extension terputus.

---

## 4. Alur C: Perlindungan Real-Time & Handoff Recovery

Alur inti (semua on-device): **akuisisi → analisis hybrid → keputusan → blokir
+ Pattern Interrupt → handoff web**.

### 4.1 Deteksi dan blokir

1. Android Accessibility / Windows (extension + service) mengakuisisi URL +
   teks DOM secara lokal.
2. Artifact **Hybrid-v2** (`assets/protection/manifest.json`; rule 0.25 +
   logistic regression 0.75, threshold 0.4) diklasifikasi di perangkat; belum
   dievaluasi (status `prototype`).
3. Jika positif → blokir lokal + increment counter agregat offline.
4. Native mengirim event `intervention_shown`; Flutter memantau
   `PlatformBridge.events()` (`app.dart:33-44`).

### 4.2 Pattern Interrupt

- `pattern_interrupt_screen.dart:25` — durasi **7 detik** (dalam jendela
  5–10s); breathing orb + progress ring; `PopScope` memblokir keluar sampai
  selesai (`:121`).
- Setelah selesai: lanjut **grounding 5-4-3-2-1** (`pattern_grounding_panel.dart`)
  atau aksi handoff.

### 4.3 Handoff web recovery

- Flutter membuka browser eksternal:
  `WEB_BASE_URL/<locale>/post-intervention?source=pattern_interrupt`
  (`pattern_interrupt_screen.dart:99-115`).
- Website `/post-intervention` adalah landing self-contained: latihan napas 3
  fase (Inhale 4s → Hold 2s → Exhale 6s × 3 ronde), **tanpa API call, tanpa
  membaca query parameter** (`post-intervention/page.tsx:32-69`).
- CTA: `Buka Recovery` → `/recovery`, `Bantuan` → `/help`.

**GAP C1 (crosscheck):** parameter `source=pattern_interrupt` dikirim oleh
Flutter tetapi **tidak dibaca** oleh halaman website. Kontrak privasi "locale +
kategori sumber tetap" hanya dipertahankan di sisi klien; tidak ada yang
melanggar privasi (param diabaikan), tetapi sinkronisasi kontrak doc↔kode tidak
utuh. Lihat §10.

---

## 5. Alur D: Recovery Web & Self-Regulation (Website)

Website adalah permukaan utama recovery. Seluruhnya `user`-centric; partner
hanya melihat agregat konsen.

### 5.1 Dashboard mahasiswa

- Setelah login → `/dashboard` → `StudentDashboard`
  (`components/dashboard/student-dashboard.tsx`).
- **Gate pertama kali** `NiatPerubahanGate`: jika belum ada intention/check-in
  hari ini → modal niat (5 pertanyaan) + intention + mood/urge check-in
  (`niat-perubahan-gate.tsx:47`, `POST /intentions` :175, `POST /check-ins`).
- Menampilkan: ringkasan `GET /client/dashboard-summary`,
  `GET /client/protection-status`, next psychoeducation, weekly snapshot,
  emergency help, FAB misi harian (`GET /missions/today`,
  `POST /missions/claim`).

### 5.2 Intention, Check-in, Misi, Reminder

| Fitur | Alur | Endpoint |
|---|---|---|
| Intention (niat) | Local-first di localStorage; sinkronisasi opt-in via Settings | `GET/POST /v1/intentions` (`use-recovery-sync-settings.ts:28`) |
| Mood/urge check-in | Submit eksplisit harian; `0` = tidak diungkapkan | `POST /v1/check-ins` (`check-in-actions.ts:40`) |
| Daily missions | 4 slot sistem (10 EXP) + hingga 5 custom (judul AES-256-GCM) | `/v1/missions/today`, `/claim`, `/custom` (`routes.go:79-83`) |
| Daily reminder | 1 sumber kebenaran lintas perangkat; web via Web Push (VAPID) | `GET/PUT /v1/me/reminder-preference` (`use-reminder-preference.ts:31`); `POST/DELETE /v1/me/push-subscription` (`use-push-notifications.ts:47`) |

### 5.3 Edukasi & Skills

- **Psychoeducation** `/education`: katalog `GET /psychoeducation/modules?locale=`;
  detail `{slug}` dengan progress per revisi
  (`PUT .../revisions/{rev}/progress`, `POST .../checks/{checkID}/answer`;
  `use-education.ts:200-257`).
- **Learning Hub** `/skills`: katalog 22 program `GET /learning-hub/catalog?locale=`
  (`use-learning-hub.ts:95`). **GAP D1:** `updateState`/`checkpoint`
  (`use-learning-hub.ts:112-178`) terdefinisi di hook tetapi **tidak ter-wire
  ke UI** — tidak ada tombol "selesai/checkpoint + EXP" di halaman skills.

### 5.4 Recovery room, Jurnal, Weekly Review, Progress

- **Jurnal** `/journal`: satu entri rich-text per hari, **AES-256-GCM**,
  `GET/PUT /v1/journal/today` + `GET /v1/journal` (`use-daily-journal.ts`).
- **Weekly review** `/recovery?range=7`: 3 langkah (yang membantu/sulit →
  penyesuaian + misi berikutnya → skill rekomendasi), `GET/PUT
  /v1/weekly-reviews/current` (+10 EXP idempoten) (`use-recovery-experience.ts:48-75`);
  refleksi fokus opsional `POST /v1/reflections`.
- **Progress 7/30/90**: `GET /v1/client/progress?days=7|30|90`
  (`use-progress-snapshot.ts:33`); ekspor CSV/PDF **client-side**
  (`progress-export.ts`) — tidak ada panggilan API ekspor.

### 5.5 Mini-games, Settings, Profile

- **Mini-games** `/mini-games`: hub + 4 game (color-sprint, picture-forge,
  twin-trace, brain-summit), murni session tanpa persist/sinkron
  (`components/mini-games/*`).
- **Settings** `/settings`: toggle sinkron intention (opt-in), daily reminder +
  push subscription, dan **SPK privacy toggles** — master
  `spk_recommendation_enabled` + 4 kategori (protection/recovery/personal) +
  `llm_personalization_enabled` via `GET/PUT /v1/client/spk-preference`
  (`use-spk-preference.ts:17`; `spk-privacy-settings.tsx:43-49`).
- **Profile** `/profile`: nama `PATCH /v1/me`, avatar `POST/DELETE /v1/me/avatar`,
  password `PATCH /v1/me/password` → logout semua sesi (`use-profile.ts:17-50`).

---

## 6. Alur E: Accountability (Website + Flutter)

### 6.1 Grup & keanggotaan

- **Partner** (website `/partners`): wajib verifikasi telepon dulu
  (`POST /auth/phone-verification/start|confirm`); buat grup
  (`POST /accountability/groups`), rotasi kode
  (`POST /groups/{id}/rotate-code`), hapus member/grup.
- **Mahasiswa**: preview grup `POST /accountability/groups/preview` → join
  `POST /accountability/groups/join` (kode). Tersedia di website
  (`student-partners-workspace.tsx:52-71`) **dan** Flutter
  (`accountability_screen.dart:74-244`).
- Route token lama (`/partner/invitations/[token]`,
  `/onboarding/create-group`) mengarahkan ulang ke `/partners`
  (`partner/invitations/[token]/page.tsx:12`).

### 6.2 Sharing agregat & approval

- Mahasiswa mengontrol 4 kategori sharing (`protection_health`,
  `protection_activity`, `recovery_engagement`, `education_progress`) →
  `PATCH /v1/accountability/memberships/{id}/sharing` — website
  (`student-accountability.tsx:113`) dan Flutter (`accountability_screen.dart:317`).
- Approval pause/uninstall: `POST /v1/approval-requests` +
  `/{id}/cancel|apply` (Flutter `accountability_repository_impl.dart:81-132`);
  partner approve/deny `POST /approval-requests/{id}/approve|deny`
  (`partner-accountability.tsx:67`).
- **Quick approval** token single-use: `GET /approval-requests/verify/{token}` +
  `POST /approval-requests/{id}/resolve-by-token` tanpa sesi
  (`use-approval.ts:50-122`; `/approve/[token]`).
- **Emergency recovery**: `POST /emergency-key-requests` (Flutter
  `accountability_repository_impl.dart:145`), admin dual-control
  `/admin/emergency` (`use-admin-operations.ts:412-445`).

---

## 7. Alur F: Support, Ekspor Data, Penghapusan Akun

- **Support** `/support`: `user`/`partner` buka kasus
  (`GET/POST /v1/support-cases`, `.../{id}/messages`, `.../transition`);
  admin membalas via `/admin/tickets`. (Flutter tidak punya surface support —
  mengarah ke web.)
- **Ekspor data** `/data-requests`: `POST /v1/data-requests` → backend buat ZIP
  AES-256-GCM → unduh `GET /v1/data-requests/{id}/download` (recent-auth ≤15
  menit, 7 hari) (`use-data-requests.ts:83-119`).
- **Penghapusan akun**: request delete → token email hashed (30 menit) → halaman
  `/data-requests/confirm-delete` dengan `?token=` → `POST
  /v1/data-requests/confirm-delete` → bersihkan sesi → `/`
  (`confirm-delete-client.tsx:28-37`).

---

## 8. Alur G: Sinkronisasi & Status Perangkat

| Langkah | Flutter | Website |
|---|---|---|
| Daftar perangkat + grant key | `POST /v1/devices` + challenge/ES256 enroll (`device_registry.dart:53-115`) | — |
| Heartbeat & status | `PATCH /v1/devices/{id}` + `POST /devices/{id}/heartbeat` (`:117-135`) | — |
| Aggregat offline | `POST /v1/client/aggregate-events` per hari/tipe + idempotency key; ack setelah sukses (`aggregate_sync.dart:7-35`) | — |
| Analytics proteksi | `GET /v1/client/protection-analytics?days=` merge data lokal (`analytics_repository_impl.dart:15-104`) | `GET /v1/client/protection-status` di dashboard |
| Reminder preference | `GET/PUT /v1/me/reminder-preference` sinkron (`settings_preferences_section.dart`) | `GET/PUT` sama + push subscription |
| Dashboard summary | — | `GET /v1/client/dashboard-summary` |

Payload agregat hanya berisi kategori allowlist, tanggal UTC, count bounded,
device ID opsional, histogram 24-slot opsional, timestamp blokir opsional (UTC)
— tanpa URL/DOM (lihat `platform_models.dart:77-119` dan ALUR_SISTEM §5.4).

---

## 9. Alur Admin & Partner (ringkas)

- **Admin** `/admin`: overview + konten CMS (psychoeducation + Learning Hub
  taxonomy/cluster/program), antrean support, data requests (retry/reject),
  emergency key (dual control), platform (accounts, social links, audit,
  translate). Semua via `use-admin-operations.ts`.
- **Partner** `/partners` + `/accountability`: ringkasan **agregat saja**
  (status proteksi, device aktif, hari check-in, band edukasi) — tanpa URL/DOM
  (`partner-progress.tsx:316`; `partner-groups-workspace.tsx:816`).

---

## 10. Tabel Crosscheck & Gap

| # | Temuan | Bukti | Implikasi |
|---|---|---|---|
| C1 | `?source=pattern_interrupt` dikirim Flutter tapi **tidak dibaca** halaman `post-intervention` | `pattern_interrupt_screen.dart:99-115` vs `post-intervention/page.tsx:32` | Kontrak doc↔kode tidak utuh; aman (param diabaikan), perlu disinkronkan |
| D1 | Learning Hub `updateState`/`checkpoint` terdefinisi tapi **belum ter-wire ke UI** | `use-learning-hub.ts:112-178`; tidak ada call site | Status `not wired` untuk alur checkpoint/reflection/EXP |
| D2 | `research-sandbox/` di website **kosong** | direktori tanpa `page.tsx` | Direktori mati; tidak direferensikan route |
| D3 | `ProtectionStatusCard` di Flutter **dead code** | `protection_status_card.dart` tidak diimpor | Bersihkan bila menyentuh area proteksi |
| D4 | Grounding `onCompleted` callback tidak ter-wire | `pattern_grounding_panel.dart:38`; `pattern_interrupt_screen.dart:188` | Durasi grounding tidak tercatat |
| D5 | SPK/LLM privacy toggles **hanya di website**; Flutter tidak punya UI (hanya error code) | `spk-privacy-settings.tsx:43` vs `app_messages.dart:276-286` | Mahasiswa mobile tidak dapat mengatur preferensi SPK dari aplikasi |
| D6 | Fitur recovery/journey/missions **kosong di Flutter**; seluruhnya lewat web | `lib/features/{recovery,journey,missions}` 0 file | Sesuai desain "thin protection surface" (`docs/ai/README.md:29-30`) |
| D7 | Role: Flutter hardcoded `user`; website mendukung `user`/`partner` | `auth_state.dart:191` vs `register/page.tsx:40` | Sesi non-`user` ditolak di aplikasi (`auth_state.dart:266`) |
| D8 | dev-login tidak ada di Flutter (sisa mapping kode saja) | `app_messages.dart:37-38` | Sinkronkan penghapusan label bila kode dicabut di backend |

---

## 11. Referensi Kunci

| Area | Lokasi |
|---|---|
| Website | `app/[locale]/`, `routes.ts`, `proxy.ts`, `lib/auth.ts`, `lib/api-client.ts`, `hooks/use-*.ts` |
| Flutter client | `lib/app/router.dart`, `lib/app/app.dart`, `lib/core/auth/auth_state.dart`, `lib/core/device/`, `lib/features/` |
| Backend route | `gamblock-ai-backend/internal/routes/routes.go` |
| Kontrak & status | `context/{architecture,privacy-security,glossary,pkm_proposal}.md`, `ALUR_SISTEM.md`, `docs/ai/README.md` (per komponen) |
