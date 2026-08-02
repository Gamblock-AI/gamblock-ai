# Register Sumber dan Aset Video Edukasi

Setiap aset final harus memiliki provenance/license/consent sebelum video
ditandai approved. Path repository menunjukkan kandidat sumber, bukan izin
otomatis untuk publikasi eksternal.

## Sumber fakta dan konsep

| ID  | Sumber                                                                                                                                                 | Penggunaan                                                     | Status                                                      |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | ----------------------------------------------------------- |
| S1  | PPATK, _Catatan Capaian Strategis PPATK Tahun 2025_ (2026), `https://www.ppatk.go.id/backend/assets/uploads/20260129025534.pdf`                        | Konteks masalah bila statistik dimasukkan pada cut alternatif  | Sumber pemerintah; tanggal/angka wajib direview             |
| S2  | Eriksen et al. (2023), _Psychological intervention for gambling disorder: A systematic review and meta-analysis_, DOI `10.1556/2006.2023.00034`        | Dasar umum bahwa intervensi psikologis perlu dibahas hati-hati | Open access CC BY-NC 4.0; jangan menggeneralisasi ke produk |
| S3  | Diaz-Sanahuja et al. (2024), _A Self-Applied Psychological Treatment for Gambling-Related Problems via The Internet_, DOI `10.1007/s10899-024-10318-2` | Konteks intervensi internet dan engagement                     | Pilot/feasibility; jangan dipakai sebagai bukti Gamblock-AI |
| S4  | Carver & Scheier (1998), _On the Self-Regulation of Behavior_, Cambridge University Press, DOI `10.1017/CBO9781139174794`                              | Siklus goal/self-monitoring/evaluation/adjustment              | Referensi teori; visual harus dibuat sendiri                |
| S5  | Wang et al. (2025), _Empowering Edge Intelligence: A Comprehensive Survey on On-Device AI Models_, DOI `10.1145/3724420`                               | Konteks local inference, latency, resource, privacy            | Kutip/parafrase secara terbatas                             |
| S6  | `context/pkm_proposal.md`, `proposal-requirements.md`, `privacy-security.md`, `research-evaluation.md`                                                 | Tujuan, batas, status, dan istilah proyek                      | Sumber internal; proposal tidak boleh diubah                |

## Aset visual kandidat

| ID  | Path                                                                                | Fungsi                | Pemeriksaan sebelum publikasi                                |
| --- | ----------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------ |
| A1  | `gamblock-ai-website/public/images/gamblock-1.png`                                  | Logo                  | Konfirmasi owner dan approved brand usage                    |
| A2  | `gamblock-ai-website/public/images/landing/generated/gami-encourage.webp`           | Gami penutup/dukungan | Konfirmasi provenance generatif dan izin publikasi           |
| A3  | `gamblock-ai-website/public/images/landing/generated/gami-shield-feature.webp`      | On-device/privacy     | Konfirmasi provenance generatif dan alt text                 |
| A4  | `gamblock-ai-website/public/images/landing/generated/pillar-detection.webp`         | Deteksi lokal         | Konfirmasi provenance generatif dan tidak memuat UI sensitif |
| A5  | `gamblock-ai-website/public/images/landing/generated/pillar-interrupt.webp`         | Pattern Interrupt     | Psychology/photosensitivity review                           |
| A6  | `gamblock-ai-website/public/images/landing/generated/pillar-accountability.webp`    | Pendamping            | Consent/non-surveillance messaging review                    |
| A7  | `gamblock-ai-website/public/images/landing/generated/pillar-recovery.webp`          | Regulasi diri         | Psychology/accessibility review                              |
| A8  | `gamblock-ai-website/public/images/landing/generated/platform-student-context.webp` | Konteks mahasiswa     | Konfirmasi tidak merepresentasikan orang nyata tanpa consent |

## Font, suara, musik, dan talent

- Plus Jakarta Sans: OFL; sertakan salinan/notis lisensi pada source bundle.
- Voice-over: rekam sendiri atau gunakan sumber dengan izin komersial/non-komersial
  yang sesuai; simpan consent talent bila suara dapat diidentifikasi.
- Musik: opsional. Catat judul, creator, URL/license, tanggal pengambilan, dan
  file hash. Musik tanpa provenance tidak boleh masuk render final.
- Stock footage: hindari bila consent/model release tidak jelas. Gunakan
  ilustrasi/diagram milik tim sebagai default.

## Artefak final yang di-hash

Render video, project/source bundle, voice track, music track, thumbnail,
caption Indonesia, caption Inggris, transcript, dan review record masing-masing
mendapat SHA-256. Source bundle tidak boleh memuat cache editor, credential,
raw participant media, atau material berlisensi yang tidak boleh didistribusikan.
