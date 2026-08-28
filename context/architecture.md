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
   mengakuisisi input lokal **hanya pada komitmen navigasi** (Enter/submit/klik
   link/perubahan halaman). Ketikan dan perubahan teks biasa tidak pernah
   diekstrak atau diklasifikasi: Android melewati event
   `CONTENT_CHANGE_TYPE_TEXT`, extension tidak membaca keystroke dan hanya
   memicu pada load, Enter/submit, dan perubahan URL.
2. Input masuk ke local protection runtime: normalisasi dan pembatasan input
   yang didukung
3. Dua jalur paralel:
   - **URL rules:** karakteristik URL dievaluasi dengan aturan eksplisit
   - **DOM analysis:** title, heading, anchor text → Bag-of-Words vectorizer →
     Logistic Regression menghasilkan skor
4. Hybrid decision menggabungkan hasil rule + model dengan threshold dan
   fusion policy
5. Keputusan positif → local block + aggregate counter (offline-capable); the
   authenticated client may publish the current UTC-day cumulative snapshot
   immediately, while completed-day rows remain retryable and idempotent
6. Pattern Interrupt 5-10 detik yang tenang dan non-klinis
7. Privacy-safe recovery web handoff (tanpa URL, DOM, atau skor)

### Accountability removal path (terpisah dari browsing path)

1. Sinyal uninstall/settings dari native client → approval request ke backend
2. Partner menerima dan memutuskan (approve/deny/expiry)
3. Backend menerbitkan grant JWS ES256 berumur pendek yang memuat action,
   device ID, dan thumbprint public key native
4. Android Keystore atau Windows LocalSystem/CNG memverifikasi signature,
   claim, batas waktu, dan device binding sebelum controlled action

Grant signing key terpisah dari access-token, Android application-signing, dan
Windows Authenticode key. Private key hanya berada di backend; client membawa
trust store public key `kid` saat ini dan berikutnya untuk rotasi. Grant lama
yang tidak ditandatangani ditolak.

## Distribution architecture

- **Android Play:** package publik mempertahankan sensing browser, inferensi
  lokal, block, dan Pattern Interrupt, tetapi source set-nya tidak memuat
  pemantauan Settings/package installer atau pencegahan uninstall.
- **Android research:** package dan signing identity terpisah mempertahankan
  seluruh prototipe Social Accountability untuk instalasi terbantu pada
  perangkat pilot. Resistensi removal tetap best-effort dan memiliki
  administrator break-glass.
- **Windows pilot:** per-machine MSI memasang binary ke `Program Files`, state
  ke `ProgramData`, dan LocalSystem service melalui Windows Installer/SCM.
  Peserta berjalan sebagai standard user; grant partner adalah offboarding
  normal dan administrator pilot tetap dapat melakukan clean break-glass
  uninstall.

Debug APK, unsigned ZIP, script dari folder user-writable, dan pemaksaan
`ExecutionPolicy Bypass` bukan artifact distribusi.

### Flutter build lanes

The Flutter repository has two CI lanes that must remain separate:

- **Diagnostic lane:** PR and `main` builds use loopback fixture configuration
  and no production signing material. Android debug APKs, the Windows debug
  ZIP, and an unsigned MSI packaging check are short-retention Actions
  artifacts only.
- **Signed lane:** an immutable `vMAJOR.MINOR.PATCH` tag in a protected
  environment builds the Play AAB, Research APK, and Windows pilot MSI. Missing
  keys or a malformed public grant trust store fail closed. Store submission,
  pilot distribution, and runtime evidence remain outside the compile step.

The variant/package/signing matrix is maintained in
`gamblock_ai_apps/docs/ai/distribution-matrix.md`.

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

### Query-driven server pagination

Collection views on the website use server pagination. The API returns a
`PaginatedList` envelope (`items`, `total_count`, `page`, `page_size`,
`total_pages`, `has_more`), while the reusable Next.js pagination hooks keep
the active page in a namespaced query key such as `page[content]` or
`page[groupMembers][<group-id>]`. This allows multiple independent lists on
one route to navigate without overwriting one another. Filters preserve
unrelated query keys and reset only the paginator they control.

### Query-driven dashboard tabs

In-page dashboard tab selectors are URL state, not component-local state. Each
independent selector uses a namespaced key such as `tab[support]`,
`tab[recovery]`, or `tab[adminTickets]`; analytics period selectors use the
semantic `period` key. The reusable website `useQueryTab` hook validates values,
preserves unrelated query parameters, resets only explicitly owned pagination,
and uses browser history for tab changes. Generic legacy keys such as `tab`,
`channel`, `range`, and `section` are no longer part of the dashboard
contract.

### Query-driven dashboard filters and editor state

Dashboard filters use the reusable website `useQueryFilters` and
`useQueryFilterInput` hooks. Browser filter keys follow
`filter[resource][field]`, search is debounced, and select changes are
immediate. Editor state uses resource-scoped keys such as `lang[content]`,
`lang[learningHub]`, and `item[learningHub]`. These browser keys are kept
separate from backend API parameters (`page`, `limit`, `q`, `group_id`, and
similar); legacy flat browser keys are removed without compatibility reads.
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
- Aggregate ingestion accepts a monotonic current-day snapshot so client and
  partner/admin analytics can reflect a recent block before UTC day rollover
- Support, content, operational audit, and emergency administration

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

## Supporting feature: student mini-games (session-only)

Website menyediakan empat mini-game sukarela untuk role `user` sebagai aktivitas
jeda adaptif: interferensi warna-kata, susun gambar, pencocokan pasangan, dan
trivia umum. Seluruh state, jawaban, skor, urutan kartu, serta waktu respons
hanya hidup selama sesi halaman dan tidak disimpan atau dikirim ke backend,
analytics, SPK/LLM, EXP, kalender pemulihan, partner, atau admin. Pada klien
mobile, permainan aktif meminta konfirmasi sebelum keluar; konfirmasi keluar
membuang sesi sehingga permainan berikutnya selalu dimulai dari awal.

Mini-games bukan intervensi klinis maupun requirement inti proposal. UI tidak
menggunakan leaderboard, hadiah acak, mata uang, loot, streak hukuman, atau
mekanik lain yang menyerupai reinforcement perjudian. Akses route ditegakkan
khusus role `user`; partner dan admin tidak mendapat proyeksi hasil permainan.

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
- Android/Windows client sends `X-Client-Type: native`; session-issuing auth
  endpoints (`/v1/auth/login`, `/v1/auth/first-login/password`,
  `/v1/auth/phone-verification/verify`) reject non-`user` accounts for it
  (`student_only`, 403). Website login stays role-agnostic (no native header).
- Partner invitation: email-bound, 7 hari kadaluarsa
- Quick approval: high-entropy, 24 jam, single-use, hashed token
- Emergency recovery: dual-operator, device-bound, 30 menit/24 jam window

## Degraded and failure behavior

- Backend unavailable: local block/Pattern Interrupt tetap berjalan
- Website unavailable: local recovery/help fallback
- Extension disconnected: Windows menunjukkan status degraded
- Model/rules corrupt: tolak artifact, pertahankan known-good version
- Partner unavailable: defined pending state, audited emergency path
