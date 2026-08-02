# Keterbatasan Prototipe dan Klaim

Dokumen ini wajib dibaca bersama panduan penggunaan dan release record. Status
berikut menggambarkan bukti yang tersedia pada 2 Agustus 2026.

## Cakupan platform

- Android secara eksplisit mendukung Chrome dan Microsoft Edge melalui
  Accessibility Service. Browser lain dan arbitrary WebView tidak diklaim.
- Windows memerlukan aplikasi, LocalSystem service, agen sesi pengguna, dan
  ekstensi Chrome/Edge yang terpasang serta ter-pairing.
- Istilah multiplatform berarti target Android dan Windows, bukan semua sistem
  operasi atau seluruh lalu lintas jaringan.
- Website adalah permukaan pemulihan/accountability, bukan blocking authority.

## Kematangan implementasi

- Jalur utama berstatus code-complete prototype, bukan production-ready.
- Android belum memiliki bukti matriks perangkat nyata yang ditinjau.
- Windows belum memiliki build dan trace VM/perangkat final yang ditinjau.
- Release workflow saat ini dapat menghasilkan debug/unsigned artifacts;
  signed production jobs tetap bergantung pada material signing dan otorisasi.
- Integrasi dengan provider OAuth, WhatsApp, delivery, dan host produksi
  memiliki gate konfigurasi/operasional terpisah.

## Model dan deteksi

- Hybrid-v2 terintegrasi dan `trained: true`, tetapi `evaluated: false` menurut
  bukti proyek.
- Dataset card, provenance/license, labeling review, leakage-safe split,
  training source, FPR slices, calibration, dan preprocessing-parity belum
  lengkap.
- Metrik pada metadata pemasok tidak boleh dipresentasikan sebagai hasil
  Gamblock-AI.
- Situs baru, bahasa/format yang tidak tercakup, konten dinamis, cloaking, dan
  perubahan struktur browser dapat menghasilkan false negative/false positive.
- Fokus minimisasi false positive pendidikan/pemerintah belum dapat disebut
  berhasil sebelum evaluasi slice final.

## Latensi dan resilience

- Target proposal adalah latensi pemblokiran di bawah 200 ms, tetapi hasil
  final belum tersedia.
- Model-only benchmark tidak dapat menggantikan input-to-visible latency yang
  mencakup extraction, preprocessing, inference, IPC, keputusan, dan UI.
- Ordinary process-kill harness tersedia, tetapi recovery matrix belum
  dieksekusi dan ditinjau pada Android/Windows.
- Android sideloading memberi friksi, bukan perlindungan uninstall absolut.
- Windows menggunakan SCM recovery; critical-process API, boot loop, dan
  destructive lockout dilarang.

## Psikologi dan keselamatan

- Pattern Interrupt dirancang memberi jeda, bukan terapi, diagnosis, atau obat.
- Belum ada hasil kohort UTY, uji kausal, atau bukti preventif yang disetujui.
- Materi visual memerlukan review psikologi, accessibility, photosensitivity,
  reduced-motion, dan adverse-event sebelum studi/publikasi final.
- Fitur tidak menggantikan konselor, psikolog, layanan kesehatan, dukungan
  finansial, atau layanan darurat.

## Retensi dan gamifikasi

- Retention rate belum memiliki definisi, periode, cohort, consent, missing-data
  policy, dan minimum suppression yang disetujui.
- EXP, level, badge, streak, dan completion menunjukkan interaksi produk, bukan
  pemulihan klinis atau berhentinya perilaku judi.
- Gamifikasi sengaja dibatasi agar tidak memakai variable reward, loot box,
  punishment, atau manipulasi rasa malu.

## Privasi dan data

- Desain melarang URL/domain/DOM/history/screenshot/per-page score keluar dari
  perangkat, tetapi network inspection eksternal tetap dibutuhkan sebagai
  acceptance evidence.
- Akun, consent, relationship, recovery sukarela, dan agregat dapat diproses
  server sesuai tujuan; ungkapan “semua data lokal” tidak boleh digunakan.
- Product consent tidak sama dengan research consent atau media/testimonial
  consent.
- Journal/reflection encryption tidak menghilangkan kebutuhan kontrol akses,
  retention, export, deletion, dan operational review.

## Generalisasi

- Target utama adalah mahasiswa dan pengujian direncanakan di Universitas
  Teknologi Yogyakarta. Hasil tidak dapat digeneralisasi ke semua mahasiswa,
  usia, institusi, wilayah, browser, atau pola perjudian tanpa sampel/protokol
  yang sesuai.
- Proposal Markdown yang tersedia kehilangan teks Fase 1–3 dan berhenti di
  tengah paragraf Fase 5; PDF/DOC akademik asli harus dipulihkan sebelum
  pembekuan laporan akhir.
