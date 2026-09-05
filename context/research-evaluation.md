# Research and Evaluation Context


Jika ada pertentangan antara dokumen ini dengan `pkm_proposal.md`, proposal PKM
adalah sumber mutlak.

## Purpose

Dokumen ini menerjemahkan maksud evaluasi proposal menjadi rencana bukti yang
dapat direproduksi. Tidak mengklaim bahwa eksperimen telah selesai.

## Evaluation questions

1. Dapatkah Hybrid Analysis membedakan konten judi dan non-judi?
2. Dapatkah Android/Windows menerapkan keputusan secara lokal, cepat, dan andal?
3. Dapatkah mekanisme social-accountability menahan manipulasi biasa dengan aman?
4. Apakah perjalanan Pattern Interrupt dan web recovery dapat digunakan, aman,
   dan terkait dengan outcome keterlibatan/preventif yang ditentukan?

## Dataset protocol

Sebelum mengumpulkan atau melatih, buat dataset card yang berisi:
- Objective, classes, unit of observation
- Source dan collection date range
- Legal/ethical basis, license
- Label definition: `Judi`, `Non-Judi`, excluded/uncertain
- Class counts, duplicate removal
- Handling of camouflage cases dan benign controls
- Known bias, language, coverage limitations

## Split and leakage controls

1. Connect exact/normalized model-text duplicates and registrable domain/site family into one group
2. Exclude groups whose rows have conflicting labels, and record the exclusion count
3. Isolate train, validation, final test groups
4. Keep camouflage/government/education sebagai slice terpisah
5. Fit vocabulary/vectorizer hanya pada training data
6. Freeze final test set sebelum threshold selection
7. Record split manifests dan hashes

## Model pipeline

Training bundle berversi harus mencakup:
- Python/scikit-learn environment lock
- Deterministic preprocessing dan tokenization rules
- Bag-of-Words vocabulary/vectorizer artifact
- Logistic Regression configuration dan random seed
- Threshold-calibration method
- Model, vectorizer, ruleset, metadata, cryptographic hashes
- Evaluation script/report dan model card

## Detection metrics and targets

- Confusion matrix (TP, FP, TN, FN)
- Precision, Recall, F1-Score
- False Positive Rate
- Performance by slice: ordinary gambling, camouflage, ordinary benign,
  government, education
- Hybrid system + rule-only + model-only ablations

Evaluasi memakai gate pengembangan dan gate laporan current secara terpisah;
lulus checkpoint pengembangan bukan otomatis lulus target laporan kemajuan.

`developmental_checkpoint` dipakai untuk penyaringan kandidat dan regresi
engineering, dengan ambang berikut:

- Accuracy >= 90%
- Precision >= 90%
- Recall >= 90%
- F1-score >= 90%
- False Positive Rate (FPR) <= 5%

Gate laporan current memakai Accuracy, Precision, Recall, dan F1-score >=90%,
serta FPR <=5%, pada split final yang bebas leakage. Ambang ini adalah target
engineering/pelaporan internal, bukan persyaratan numerik baru dari proposal
PKM. Nilai metrik aktual, split, audit leakage, dan keterbatasan tetap harus
dilaporkan. Bila snapshot prediksi dan proyeksi deployment berbeda, keduanya
harus dilaporkan dan klaim hanya boleh mengikuti hasil deployment.

Ambang dan cakupan current diringkas di `progress-targets.md` dan diwujudkan
oleh `gamblock-ai-testing/docs/config/targets.json`. Perubahan target harus
ditinjau bersama report current dan batas evidence terkait.

Artefak yang diperiksa adalah artefak Hybrid yang benar-benar dimuat runtime
Android/Windows, bukan sekadar format sumber pelatihan. Kontrak ukuran adalah
total artefak Hybrid lokal < 5 MB, hash/provenance dapat diperiksa, dan inferensi
tetap lokal. Proposal tidak mensyaratkan runtime ONNX.

## Threshold selection

Hybrid-v2 yang diimpor menspesifikasikan threshold `0.4` dan bobot
`0.75/0.25`. Ini adalah input engineering, bukan persyaratan proposal.
Kalibrasi threshold pada data validasi, catat keputusan, jangan pernah
tune terhadap final test set.

## Latency evaluation

Target proposal: block latency di bawah 200 ms.
- start event: input lokal lengkap tersedia
- end event: block/intervention terlihat committed
- Pisahkan durasi extraction, preprocessing, rule, inference, decision, IPC, UI
- Gunakan dua tingkat bukti latency yang tidak boleh dipertukarkan:
  1. **Kelayakan latency:** sedikitnya satu kelompok lingkungan homogen,
     minimal 30 sampel berhasil, tanpa kegagalan aksi blok/visibility, dan p95
     `input_to_visible_ms` secara ketat di bawah 200 ms. Ini menjawab apakah
     prototipe mampu mencapai target pada lingkungan yang diukur.
  2. **Checkpoint laporan kemajuan current:** satu demonstrasi yang dapat
     diulang pada APK **Research release**, Android, Chrome,
     `warm_foreground_online`, dengan minimal 30 sampel berhasil dan p95
     secara ketat di bawah 200 ms. Mode debug tidak dapat memenuhi checkpoint
     ini karena ia mengukur assertion/instrumentasi debug, bukan APK yang
     didemonstrasikan.
- **Pengujian runtime klien:** ini bukan tingkat latency ketiga. Gate
  final-readiness sebelumnya diganti oleh kontrak regresi dukungan peramban.
  Regresi ini mewajibkan satu perangkat Android yang menguji Chrome, Edge,
  Brave, dan Firefox dengan 5 sampel judi dan 5 non-judi per peramban.
  Pengujian Windows pada Chrome, Edge, Brave, Opera, dan Firefox bersifat
  opsional dan tidak menggagalkan gate Android.
  Hasil runtime harus menunjukkan `intervention` untuk judi dan `allow` untuk
  non-judi. Evidence ini disimpan di `flutter/evidence/client-runtime/` dan
  divalidasi terpisah dari ledger latency.
- Pengukuran lokal yang belum dipromosikan sebagai ledger agregat tervalidasi
  hanya berstatus *recorded, unpromoted*. Ia dapat mendukung catatan sumber,
  tetapi bukan klaim checkpoint atau hasil final.
- Cakupan checkpoint current di atas dipakai oleh evaluator tunggal dan tidak
  memerlukan salinan report atau konfigurasi alternatif.
- Bedakan warm/cold start, online/offline, foreground/background

## Functional and resilience evaluation

Skenario: navigasi normal, offline protection, restart browser/client/service,
device reboot, process kill, uninstall/settings interaction, expired/revoked
token, partner unavailable, update/rollback, false-positive recovery,
accessibility/reduced-motion.

## Pattern Interrupt evaluation

Sebelum studi subjek manusia, dapatkan review etis/akademik untuk:
- Populasi partisipan, inclusion/exclusion, informed consent
- Konten stimulus, durasi 5-10 detik, opsi reduced-motion/non-visual
- Primary outcome dan observation window
- Adverse-event/help protocol

## Privacy and ethics gates

- Tidak ada evaluasi yang mengumpulkan URL, DOM, browsing history, screenshot
- Product consent, partner consent, dan research consent berbeda
- Withdrawal harus menghentikan pengumpulan riset di masa depan

## Reproducible prototype evidence

Cross-repository orchestration and the single public testing summary now belong
to the `Gamblock-AI-Testing` repository, mounted in the umbrella at
`gamblock-ai-testing/`. The testing repository consumes component artifacts
and privacy-safe aggregate exports; it does not copy source code or browsing
data into the umbrella.

The canonical operational rules are in `context/testing-evaluation.md`,
`context/progress-testing.md`, and
`gamblock-ai-testing/docs/ai/android-anti-uninstall-testing.md`. Component
`docs/ai/README.md` files contain status and links only; they do not duplicate
run-specific results.

## Decisions still required

- Restorasi proposal asli
- Dataset governance owner dan labeling protocol
- Definisi retensi
- Rute review etis dan desain studi Pattern Interrupt
