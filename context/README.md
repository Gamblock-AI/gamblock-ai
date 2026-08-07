# Gamblock-AI Context Router


Jika ada pertentangan antara dokumen konteks dengan `pkm_proposal.md`, proposal
PKM adalah sumber mutlak.

## Source-of-truth hierarchy

1. `pkm_proposal.md` — otoritas utama: masalah, target pengguna, fitur PKM,
   dasar ilmiah, tujuan evaluasi, deliverables PKM
2. Domain documents (`architecture.md`, `privacy-security.md`,
   `research-evaluation.md`) — menjelaskan bagaimana produk memenuhi
   persyaratan teknis
4. Component `docs/ai/README.md` — kebenaran implementasi saat ini per repositori

## Proposal integrity warning

Ekstraksi Markdown `pkm_proposal.md` tidak lengkap: konten Fase 1-3 di bagian
3.2 hilang, fragmen OCR/gambar tersisa, paragraf Fase 5 terpotong. Jangan
menciptakan teks akademik yang hilang. Pulihkan dari sumber PDF/DOC asli tim
saat tersedia.

## Reading routes

| Task | Required context |
|---|---|
| Product/implementation change | `pkm_proposal.md`, component `docs/ai/README.md` |
| Detection, native client, API, storage | `architecture.md`, `privacy-security.md` |
| Dataset, model, metric, experiment | `research-evaluation.md` |
| Implementation status | affected component `docs/ai/README.md` |
| Terminology | `glossary.md` |

## AI development workflow

### 1. Load authority before implementation

Baca `AGENTS.md` root dan komponen, `context/README.md`, bagian proposal yang
relevan dan `docs/ai/README.md` komponen.
Periksa `git status` — perubahan yang sudah ada milik user.
`pkm_proposal.md` tidak boleh diedit untuk mencocokkan kode.

### 2. Resolve conflicts by source

Urutan otoritas: proposal → requirement IDs → domain context → component
status/code → component instructions. Jika kode bertentangan dengan proposal,
pertahankan requirement proposal, beri label status kode, catat kesenjangan.

### 3. Respect non-negotiable boundaries

- Sensing, inferensi, dan keputusan konten browsing tetap di perangkat
- Data browsing mentah tidak pernah masuk backend/website/partner/admin
- Extension tetap sensor pasif lokal
- Blocking dan Pattern Interrupt di Android/Windows
- Anti-uninstall menggunakan mekanisme OS yang aman
- Jangan edit file yang dihasilkan/dilindungi
- Jangan deploy, release, push, atau ubah sistem eksternal tanpa izin eksplisit

### 4. Default verification: lint only

| Component | Command |
|---|---|
| Umbrella/context-only | `./scripts/verify-ai-context.sh --allow-untracked` |
| Backend | `make lint` |
| Website | `npm run lint -- <changed-source-files>` |
| Flutter | `flutter analyze` |
| Browser extension | `npm run lint` |
| Infrastructure | `make lint` |
| Model          | *(no lint configured)* |

Test, build, packaging, coverage, E2E hanya dijalankan jika user meminta
eksplisit. Context validator wajib jika file instruksi, manifes, adapter,
snapshot, atau kontrak berubah.

### 5. Cross-repository coordination

Urutan dependensi: proposal → backend → website/Flutter/extension →
infrastructure → validasi. Contoh koordinasi wajib:
- WebSocket shape: extension + Windows service
- Kode error API: backend + website + Flutter
- Client-facing endpoint: backend + konsumen

### 6. Protected files

- `context/pkm_proposal.md`
- Website `components/ui/*`
- Backend `ent/` yang dihasilkan
- File lokalisasi/artifact yang dihasilkan
- `.env`, kredensial, keystore, vault, token, database lokal

## Ownership and update rules

| Change | Update first | Then update |
|---|---|---|
| Proposal requirement / academic claim | `pkm_proposal.md` (owner-authorized) | affected domain docs |
| Architecture / trust boundary | `architecture.md` / `privacy-security.md` | component snapshots |
| Research method / metric | `research-evaluation.md` | traceability |
| Workflow / validation policy | `AGENTS.md` / `context/README.md` | component `AGENTS.md`, manifests |
| Current capability evidence | component `docs/ai/README.md` | affected README |

Meaningful scope/architecture/workflow/contract changes require `context_version`
bump di `manifest.yaml` dan setiap snapshot komponen yang terpengaruh.

## Default validation policy

Selama development AI normal, hanya jalankan linter/analyzer yang relevan dan
context-integrity validator (jika file konteks berubah). Test, build, packaging,
coverage, E2E hanya dijalankan jika user meminta secara eksplisit.
