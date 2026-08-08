# Architecture Context


Jika ada pertentangan antara dokumen ini dengan `pkm_proposal.md`, proposal PKM
adalah sumber mutlak.

## Repository topology

| Repository | Stack | Primary responsibility |
|---|---|---|
| `gamblock_ai_apps/` | Flutter + Android/Windows native | Local protection, Pattern Interrupt, device/accountability |
| `browser_extension/` | Chrome/Edge MV3 | Passive Windows browser DOM/URL sensor via loopback IPC |
| `gamblock-ai-website/` | Next.js, React | Web psychoeducation/self-regulation, accountability, public |
| `gamblock-ai-backend/` | Go + ent + PostgreSQL | Identity, relationships, approvals, recovery state, aggregates |
| `gamblock-ai-infrastructure/` | Ansible + Docker + Caddy | Backend/website delivery, TLS, database |

## Architecture principles

1. **Proposal-first:** arsitektur harus mencakup setiap persyaratan inti PKM
2. **Local protection authority:** sensing, feature extraction, inference,
   block, dan Pattern Interrupt tetap di perangkat
3. **Offline-first core:** blocking/intervention tidak bergantung pada backend
4. **Explicit trust boundaries:** loopback IPC diautentikasi; API server hanya
   menerima skema non-browsing yang dideklarasikan
5. **Safe resistance:** anti-uninstall menggunakan mekanisme OS yang didukung

## System flow

### Protection flow

1. Android (Accessibility Service) atau Windows (Extension → loopback WebSocket)
   mengakuisisi input lokal
2. Input masuk ke local protection runtime: normalisasi dan pembatasan input
   yang didukung
3. Dua jalur paralel:
   - **URL rules:** karakteristik URL dievaluasi dengan aturan eksplisit
   - **DOM analysis:** title, heading, anchor text → Bag-of-Words vectorizer →
     Logistic Regression menghasilkan skor
4. Hybrid decision menggabungkan hasil rule + model dengan threshold dan
   fusion policy
5. Keputusan positif → local block + aggregate counter (offline-capable)
6. Pattern Interrupt 5-10 detik yang tenang dan non-klinis
7. Privacy-safe recovery web handoff (tanpa URL, DOM, atau skor)

### Accountability removal path (terpisah dari browsing path)

1. Sinyal uninstall/settings dari native client → approval request ke backend
2. Partner menerima dan memutuskan (approve/deny/expiry)
3. Client validasi state otoritatif dari backend → controlled action

## Hybrid detection pipeline

### Input acquisition

- URL characteristics dan DOM text (title, headings, anchor text) dari surface
  yang didukung
- Windows extension merelay ke loopback service yang dipasangkan; Android
  menggunakan bridge/accessibility path

### Preprocessing

Training dan runtime berbagi aturan: Unicode, case, tokenization, whitespace,
feature limits, vocabulary, unknown terms.

### Rule and model branches

- Rule branch: karakteristik URL eksplisit + keyword matches
- Model branch: Bag-of-Words → Logistic Regression secara lokal
- Fusion policy mendefinisikan precedence, score normalization, threshold,
  dan safe fallback

### Decision and action

- Keputusan positif dijalankan native client/service, bukan extension/backend
- Keputusan negatif/uncertain mengikuti safe fallback

## Web recovery architecture

Next.js pages mengonsumsi typed hooks → API client → Go response envelope.
Core recovery services: intention lifecycle, mood/urge check-in,
psychoeducation, daily mission, skill recommendations, weekly review.

Student-private by default. Partner projections adalah aggregate read models
terpisah, bukan penggunaan ulang respons API privat student.

## Backend boundaries

### Layering

`cmd → api → routes → handler → service → repository → ent/PostgreSQL`

### Server responsibilities

- Identity/auth/RBAC dan consent
- Partner/group relationship dan approval state
- Published psychoeducation/missions/skills dan student recovery state
- Encrypted sensitive reflections/journal (enkripsi dilakukan client-side
  sebelum persistensi)
- Aggregate events dan device health
- Support, content/release metadata, operational audit

### Server prohibitions

- Tidak menerima URL/domain/DOM/history/screenshot
- Tidak melakukan remote inference pada konten browsing
- Tidak menyimpan per-page score/feature
- Tidak memberikan akses raw recovery content ke partner/admin

## Supporting feature: daily reminder (opt-in)

Fitur pengingat harian bersifat *supporting* (bukan requirement proposal). Satu
preferensi `{ enabled, local_time, timezone, locale }` per akun disimpan di
PostgreSQL (`reminder_preferences`) dan disinkronkan lintas permukaan:

- **Web**: situs PWA berlangganan Web Push (VAPID). Endpoint langganan
  (`push_subscriptions`) hanyalah metadata pengiriman — bukan data browsing.
  Scheduler backend (satu proses API, interval 1 menit) mengirim notifikasi
  saat waktu lokal pengguna tercapai; endpoint 404/410 dipangkas.
- **Android**: notifikasi lokal berulang via `flutter_local_notifications`.
- **Windows**: toast satu-kali untuk kemunculan berikutnya (plugin Windows
  tidak mendukung repeat), dijadwalkan ulang saat aplikasi berjalan berikutnya.

Konten pesan netral dan tidak memuat data sensitif. Tidak ada token FCM/APNs;
pengiriman web murni Web Push berbasis VAPID.

## Storage model

| Store | Target data | Boundary |
|---|---|---|
| Device local | model/rules/media, pairing token, protection state, offline queue | Detection data stays here |
| PostgreSQL | accounts, relationships, approvals, recovery state, encrypted text, aggregates | No browsing schema |
| chrome.storage.local | pairing token, connection config | No remote sync |
| Website localStorage | local-first intention, check-in drafts, weekly plan | No browsing fields |

## Authentication and API contracts

- JWT access token + rotating refresh token
- Backend RBAC otoritatif
- Partner invitation: email-bound, 7 hari kadaluarsa
- Quick approval: high-entropy, 24 jam, single-use, hashed token
- Emergency recovery: dual-operator, device-bound, 30 menit/24 jam window

## Degraded and failure behavior

- Backend unavailable: local block/Pattern Interrupt tetap berjalan
- Website unavailable: local recovery/help fallback
- Extension disconnected: Windows menunjukkan status degraded
- Model/rules corrupt: tolak artifact, pertahankan known-good version
- Partner unavailable: defined pending state, audited emergency path
