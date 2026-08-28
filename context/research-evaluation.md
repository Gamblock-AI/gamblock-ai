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
- Known bias, language, time-drift, coverage limitations

## Split and leakage controls

1. Group by registrable domain/site family
2. Isolate train, validation, final test groups
3. Reserve time-shifted set untuk domain-churn evaluation
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

## Detection metrics

## Threshold selection

- Confusion matrix (TP, FP, TN, FN)
- Precision, Recall, F1-Score
- False Positive Rate
- Performance by slice: ordinary gambling, dynamic/new-domain, camouflage,
  ordinary benign, government, education
- Hybrid system + rule-only + model-only ablations

Target numerik untuk Precision, Recall, F1, dan FPR adalah keputusan pemilik
riset; tidak dibuat dalam dokumentasi implementasi.

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
- Engineering gate: p95 `input_to_visible_ms` harus secara ketat di bawah 200 ms
  pada setiap grup platform/perangkat/skenario, dengan minimal 30 sampel dan
  tanpa kegagalan aksi blok atau visibility; report juga median, p99, maksimum
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

## Decisions still required

- Restorasi proposal asli
- Dataset governance owner dan labeling protocol
- Target numerik deteksi dan FPR
- Final latency gate dan device matrix
- Definisi retensi
- Rute review etis dan desain studi Pattern Interrupt
