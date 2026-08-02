# Laporan Traceability Proposal, Implementasi, dan Bukti

Tanggal pembekuan: 2 Agustus 2026

Sumber requirement: `context/proposal-requirements.md`

Aturan status: `context/glossary.md` dan `context/research-evaluation.md`

## Cara membaca

- `implemented` berarti jalur aktif tersambung, bukan otomatis telah dievaluasi.
- `prototype` berarti perilaku dapat dijalankan tetapi memiliki batas/gate.
- `instrumented` berarti alat pengumpulan/analisis bukti tersedia.
- `planned` atau `blocked` menunjukkan acceptance evidence belum tersedia.
- Kolom bukti menunjuk sumber version-controlled; bukti perangkat, studi,
  approval, submission, dan publication tetap membutuhkan record eksternal.

## Platform, AI, dan blocking

| ID              | Status saat dibekukan | Bukti utama                                                                       | Gap acceptance                                         |
| --------------- | --------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------ |
| `PKM-PLAT-001`  | `prototype`           | `gamblock_ai_apps/android/`, Flutter status doc                                   | Android device matrix dan release review               |
| `PKM-PLAT-002`  | `prototype`           | `gamblock_ai_apps/windows/`, Flutter status doc                                   | Windows build/VM trace dan release review              |
| `PKM-PLAT-003`  | `prototype`           | Android Accessibility Service, Windows service/agent, setup/health UI             | Profil resource dan coverage perangkat nyata           |
| `PKM-AI-001`    | `implemented`         | `gamblock_ai_apps/assets/protection/gamblock-rules-v2.json`                       | Evaluasi rule-only pada final split                    |
| `PKM-AI-002`    | `implemented`         | Hybrid-v2 artifacts serta Android/Windows classifier                              | Evaluasi hybrid dan calibration review                 |
| `PKM-AI-003`    | `prototype`           | `browser_extension/content_script.js`, Android Accessibility Service              | Extraction fixtures dinamis dan device review          |
| `PKM-AI-004`    | `implemented`         | `gamblock-lr-v2.json` vocabulary/weights dan native classifiers                   | Paritas terhadap training preprocessing asli           |
| `PKM-AI-005`    | `blocked`             | Artefak terlatih tersedia; `evaluation/phase4/evaluate_model.py` terinstrumentasi | Training source, dataset card, split, metrics final    |
| `PKM-AI-006`    | `prototype`           | Android/Windows inferensi lokal dan manifest hashed                               | CPU/memory/energy/latency representative               |
| `PKM-AI-007`    | `instrumented`        | Slice evaluator `gambling/dynamic/camouflage/government/education`                | Governed holdout dan reviewed error analysis           |
| `PKM-BLOCK-001` | `prototype`           | Android local Back/overlay; Windows service + user agent                          | End-to-end device trace                                |
| `PKM-BLOCK-002` | `instrumented`        | Native timing capture dan `summarize_latency.py`                                  | Declared device matrix dan hasil <200 ms yang ditinjau |

## Privasi

| ID             | Status saat dibekukan             | Bukti utama                                                                   | Gap acceptance                                      |
| -------------- | --------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------- |
| `PKM-PRIV-001` | `implemented` design/runtime      | Native classifiers, passive loopback extension, `context/privacy-security.md` | Independent network/data-flow inspection            |
| `PKM-PRIV-002` | `implemented` design/runtime      | Backend schema prohibition, client aggregate contracts, privacy notice        | Cross-platform network/log inspection               |
| `PKM-PRIV-003` | `implemented` supporting workflow | Consent, export/delete, retention boundaries, aggregate categories            | Qualified legal/privacy review; no compliance claim |

## Pattern Interrupt

| ID            | Status saat dibekukan | Bukti utama                                                        | Gap acceptance                                   |
| ------------- | --------------------- | ------------------------------------------------------------------ | ------------------------------------------------ |
| `PKM-INT-001` | `prototype`           | Android overlay dan Windows/Flutter intervention path              | End-to-end real-device trace                     |
| `PKM-INT-002` | `prototype`           | Seven-second path, reduced motion, offline fallback                | Asset provenance dan accessibility/device review |
| `PKM-INT-003` | `instrumented`        | Phase 4 study protocol/analyzer                                    | Ethics approval dan executed outcome study       |
| `PKM-INT-004` | `implemented`         | Handoff membawa locale + fixed source only ke `/post-intervention` | Device usability evidence                        |

## Social Accountability Protocol

| ID            | Status saat dibekukan | Bukti utama                                                            | Gap acceptance                                  |
| ------------- | --------------------- | ---------------------------------------------------------------------- | ----------------------------------------------- |
| `PKM-ACC-001` | `implemented`         | Backend relationship/group state, website dan Flutter partner flows    | Operational consent/usability review            |
| `PKM-ACC-002` | `prototype`           | Request/approval/deny/expire/cancel/grant state dan quick approval     | Native uninstall/removal device trace           |
| `PKM-ACC-003` | `prototype`           | Android settings friction, Windows settings monitoring, bounded grants | Platform limitation and permission review       |
| `PKM-ACC-004` | `instrumented`        | SCM recovery, Android recovery harness, Phase 4 resilience matrix      | Executed safe kill/recovery matrix dan sign-off |

## Web psikoedukasi dan regulasi diri

| ID            | Status saat dibekukan | Bukti utama                                                       | Gap acceptance                                     |
| ------------- | --------------------- | ----------------------------------------------------------------- | -------------------------------------------------- |
| `PKM-WEB-001` | `implemented`         | Public post-intervention dan authenticated recovery route         | Content/accessibility review record                |
| `PKM-WEB-002` | `implemented`         | Intention create/review/update dan local-first sync               | Usability review                                   |
| `PKM-WEB-003` | `implemented`         | Reviewed-content workflow, education modules, reflection progress | Psychology/editorial approval per content revision |
| `PKM-WEB-004` | `implemented`         | Structured mood/urge check-in dan history/trend                   | Research use needs separate consent                |
| `PKM-WEB-005` | `implemented`         | Deterministic five-slot missions dan private custom mission       | Content review dan usage evidence                  |
| `PKM-WEB-006` | `implemented`         | Program-study Learning Hub, explainable context, progress         | External-link/content periodic review              |
| `PKM-WEB-007` | `implemented`         | Intention → check-in → education/mission/skill → weekly review    | Cohort/usability evidence; no efficacy claim       |

## Evaluation

| ID             | Status saat dibekukan | Bukti utama                                                        | Gap acceptance                                                  |
| -------------- | --------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------- |
| `PKM-EVAL-001` | `instrumented`        | Phase 4 confusion matrix, Precision/Recall/F1 evaluator            | Approved dataset/final report/reviewer                          |
| `PKM-EVAL-002` | `instrumented`        | FPR slice dan opaque failure-ID evaluator                          | Representative education/government samples dan target decision |
| `PKM-EVAL-003` | `instrumented`        | Android/Windows capture + latency summarizer                       | Executed matrix dan approved percentile gate                    |
| `PKM-EVAL-004` | `instrumented`        | Consent/withdrawal/suppression-aware retention analyzer            | Definition, approved cohort, collected data                     |
| `PKM-EVAL-005` | `instrumented`        | Disposable device/VM harness dan resilience summarizer             | Complete scenario matrix dan reviewer sign-off                  |
| `PKM-EVAL-006` | `instrumented`        | Pattern Interrupt protocol/analyzer, adverse/limitations templates | Ethics approval, staged study, accessibility and safety review  |

## Data, content, dokumentasi, komunikasi, dan publikasi

| ID                | Status saat dibekukan            | Bukti utama                                                      | Gap acceptance                                                           |
| ----------------- | -------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `PKM-DATA-001`    | `blocked`                        | Dataset/split templates dan evaluator tersedia                   | Governed labeled data, provenance/license, labeling review               |
| `PKM-DATA-002`    | `blocked`                        | Runtime export script tersedia; original training source absent  | Reproducible scikit-learn training environment/source                    |
| `PKM-CONTENT-001` | `prototype`                      | Pattern Interrupt media/runtime dan reduced-motion path          | Versioned asset inventory, provenance, psychology/accessibility approval |
| `PKM-DOC-001`     | `implemented` draft              | `deliverables/phase5/reports/progress-report.md`                 | Approval dan submission receipt                                          |
| `PKM-DOC-002`     | `implemented` draft              | `deliverables/phase5/reports/final-report.md`                    | Phase 4 results, approval, submission receipt                            |
| `PKM-DOC-003`     | `implemented` documentation      | Guide, limitations, traceability, release schema                 | Immutable evaluated Android/Windows demo release                         |
| `PKM-COMMS-001`   | `implemented` package            | Account register, content plan, archive, continuity procedure    | Ownership verification dan real publication archive                      |
| `PKM-COMMS-002`   | `implemented` production package | Script/storyboard, captions, sources, review/publication schemas | Rendered reviewed video dan publication record                           |
| `PKM-PUB-001`     | `implemented` draft              | `deliverables/phase5/scientific-article/manuscript.md`           | Phase 4 results dan author/venue approval                                |

## Evidence roll-up

| Layer                          | Status                                   | Syarat promosi                                                                    |
| ------------------------------ | ---------------------------------------- | --------------------------------------------------------------------------------- |
| Implementasi produk            | Code-complete prototype pada jalur utama | Device/build/runtime evidence                                                     |
| Phase 4                        | `instrumented`                           | Semua protocol dijalankan, reviewed, hashed, manifest `evaluated`                 |
| Phase 5 repository preparation | `implemented`                            | Artefak lokal, public transparency, dan verifier tersedia                         |
| Phase 5 accepted delivery      | `blocked`                                | Approval, submission, release, ownership, publication, dan Phase 4 evidence nyata |

Tidak ada requirement yang dipromosikan menjadi `evaluated` hanya karena file,
handler, UI, seed, atau template tersedia. Manifest Phase 5 adalah gerbang
kanonik untuk accepted delivery.
