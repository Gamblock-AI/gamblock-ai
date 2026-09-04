# Gamblock-AI Context Router


Jika ada pertentangan antara dokumen konteks dengan `pkm_proposal.md`, proposal
PKM adalah sumber mutlak.

## Source-of-truth hierarchy

1. `pkm_proposal.md` — otoritas utama: masalah, target pengguna, fitur PKM,
   dasar ilmiah, tujuan evaluasi, deliverables PKM
2. `progress-targets.md` — registri target per versi dan keputusan perubahan;
   target baru tidak boleh disisipkan ke laporan versi yang sudah dibekukan
3. `laporan-kemajuan-v5.md` (dan kelak salinan versi berikutnya) — konteks
   pelaporan kemajuan dan target/temuan yang sedang dilaporkan; v5 read-only
4. Domain documents (`architecture.md`, `privacy-security.md`,
   `research-evaluation.md`) — menjelaskan bagaimana produk memenuhi
   persyaratan teknis
5. Component `docs/ai/README.md` — kebenaran implementasi saat ini per repositori

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
| PKM progress targets | `progress-targets.md`, report copy yang sedang aktif |
| PKM progress testing/status | `laporan-kemajuan-v5.md` atau report copy aktif, `progress-testing.md`, `research-evaluation.md` |
| Cross-repository testing/evidence | `testing-evaluation.md`, testing repo `docs/ai/` |
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
- Test/evidence workflow: testing repository + affected component snapshots

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

## Versioned progress-report rule

`laporan-kemajuan-v5.md` is a frozen report snapshot. Later measurements,
proposed targets, and target changes belong in `progress-testing.md` or the
versioned target registry `progress-targets.md`; they must not be appended to
the v5 report. A future v6 report is made by copying v5 and then explicitly
activating the approved v6 targets from the registry. Until that happens,
`gamblock-ai-testing/docs/config/targets.json` remains the active v5 machine
configuration, and proposed targets have no effect on its gates.

Meaningful scope/architecture/workflow/contract changes require `context_version`
bump di `manifest.yaml` dan setiap snapshot komponen yang terpengaruh.

## Default validation policy

Selama development AI normal, hanya jalankan linter/analyzer yang relevan dan
context-integrity validator (jika file konteks berubah). Test, build, packaging,
coverage, E2E hanya dijalankan jika user meminta secara eksplisit.

## Read-only testing audits

Permintaan dengan kata “cek”, “periksa”, “review”, “audit”, atau “ringkasan
pengujian yang ada” berarti inspeksi read-only. Agen membaca test source,
konfigurasi, workflow, report/evidence yang sudah tersimpan, status repository,
dan dokumentasi untuk menyimpulkan kekurangan atau status pending. Permintaan
tersebut tidak memberi izin untuk menjalankan test, build, packaging, model
replay, prosedur perangkat/VM, atau `run_evaluation.py`.

Eksekusi hanya dilakukan bila user secara eksplisit meminta menjalankan,
menguji, memvalidasi, mengevaluasi ulang, melakukan prosedur runtime, atau
merekam evidence baru. Dalam audit read-only, report lama dilabeli sebagai
“status tercatat” dan tidak diregenerasi atau diperlakukan sebagai hasil terbaru.
