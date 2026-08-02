# Laporan Kemajuan PKM-KC 2026 — Gamblock-AI

Status dokumen: draf lengkap untuk peninjauan tim dan dosen pendamping

Tanggal pembekuan isi: 2 Agustus 2026

Institusi: Universitas Teknologi Yogyakarta

Judul: **Gamblock-AI: Sistem Pemblokiran Judi Online Berbasis On-Device
Artificial Intelligence dengan Mekanisme Pattern Interrupt dan Social
Accountability Protocol untuk Mahasiswa**

## Ringkasan kemajuan

Program telah menghasilkan prototipe lintas platform yang menghubungkan sensor
peramban pasif, klasifikasi Hybrid Analysis pada perangkat, otoritas pemblokiran
Android/Windows, Pattern Interrupt tujuh detik, Social Accountability Protocol,
serta web psikoedukasi dan regulasi diri. Website menyediakan alur tujuan
perubahan, pemantauan diri, edukasi impuls, misi harian, rekomendasi
keterampilan, evaluasi mingguan, dan dukungan pendamping berbasis agregat.

Status yang dapat dipertanggungjawabkan saat dokumen ini dibekukan adalah
**prototipe code-complete dan Phase 4 terinstrumentasi**. Kode, kontrak, dan
alat evaluasi tersedia, tetapi model belum memiliki dataset card dan evaluasi
final yang disetujui; runtime Android belum memiliki bukti perangkat nyata;
runtime Windows belum memiliki bukti VM/perangkat yang ditinjau; dan penelitian
Pattern Interrupt/retensi belum dijalankan pada kohort UTY dengan persetujuan
etika. Oleh sebab itu, laporan ini tidak mengklaim akurasi, efektivitas,
retensi, ketahanan, atau latensi final.

## 1. Tujuan program

1. Mengembangkan prototipe Android dan Windows untuk mendeteksi serta memblokir
   indikasi konten judi online secara lokal.
2. Menggabungkan aturan URL, teks DOM terbatas, Bag-of-Words, dan Logistic
   Regression sebagai Hybrid Analysis yang ringan.
3. Menampilkan Pattern Interrupt 5–10 detik dan mengarahkan pengguna ke web
   psikoedukasi tanpa mengirim konteks penelusuran.
4. Menambahkan persetujuan pendamping sebagai friksi aman untuk pelepasan
   perlindungan sesuai batas sistem operasi.
5. Menyediakan siklus regulasi diri yang relevan bagi mahasiswa dan tetap
   menjaga data pemulihan pribadi.

## 2. Capaian teknis

### 2.1 Aplikasi Android dan Windows

- Aplikasi Flutter menyediakan onboarding, autentikasi mahasiswa, status
  perlindungan, analitik agregat, pengelolaan pendamping, pengaturan, dan
  handoff pemulihan yang tidak memuat URL atau DOM.
- Android menggunakan Accessibility Service untuk input yang didukung,
  keputusan lokal, intervensi, friksi pengaturan, grant berbasis Keystore, dan
  sinkronisasi agregat.
- Windows memisahkan LocalSystem service dari agen sesi pengguna, menggunakan
  WebSocket loopback terautentikasi, named pipe terbatas SID, DPAPI, SCM
  recovery, dan tindakan navigasi yang didukung.
- Mekanisme critical-process yang dapat menyebabkan kerusakan sistem tidak
  digunakan.

### 2.2 Deteksi Hybrid Analysis

- Aturan URL, ekstraksi title/heading/anchor text, vektor unigram/bigram,
  fitur URL, Logistic Regression, serta fusi keputusan dijalankan lokal.
- Android dan Windows mengonsumsi kontrak artefak Hybrid-v2 yang sama.
- Artefak terintegrasi berstatus terlatih tetapi belum dievaluasi oleh bukti
  proyek. Metrik yang ikut dalam metadata pemasok tidak digunakan sebagai hasil
  penelitian Gamblock-AI.

### 2.3 Pattern Interrupt dan pemulihan

- Jalur intervensi tujuh detik, reduced-motion, grounding offline, bantuan, dan
  handoff web tanpa browsing context telah diimplementasikan.
- Web pemulihan menghubungkan niat, check-in mood/dorongan, edukasi,
  misi, pengembangan keterampilan, dan evaluasi mingguan.
- Teks jurnal/refleksi sensitif mengikuti alur terenkripsi AES-256-GCM dan
  tidak ditampilkan kepada pendamping.

### 2.4 Social Accountability Protocol

- Undangan/penerimaan hubungan, grup, preferensi empat kategori agregat,
  permintaan tindakan, persetujuan/penolakan/kedaluwarsa, pembatalan, unsafe
  exit, dan emergency recovery telah memiliki state dan audit yang terhubung.
- Pendamping hanya melihat status serta agregat yang disetujui, bukan URL,
  riwayat, jurnal, mood, atau detail aktivitas pemulihan.

### 2.5 Website dan Learning Hub

- Website memiliki dashboard berbasis peran untuk mahasiswa, pendamping, dan
  admin tanpa memindahkan otoritas pemblokiran dari aplikasi native.
- Learning Hub menyediakan materi dan sumber belajar yang dikelompokkan untuk
  program studi UTY, disertai konteks manfaat, tingkat, estimasi waktu, dan
  progres/gamifikasi yang terfokus.
- Gamifikasi tetap berada pada perjalanan pemulihan dan belajar; aplikasi
  perlindungan native tetap tipis dan tidak menduplikasi sistem EXP website.

## 3. Privasi, keamanan, dan etika

- URL, domain, DOM, riwayat, screenshot, feature vector, dan skor per halaman
  tetap di perangkat.
- Ekstensi peramban hanya menjadi sensor pasif dan tidak memblokir, menutup tab,
  mengalihkan halaman, atau merender Pattern Interrupt.
- Backend menerima data akun, consent, accountability, pemulihan sukarela, dan
  agregat non-rekonstruktif sesuai tujuan; tidak tersedia skema browsing.
- Persetujuan penggunaan produk, hubungan pendamping, penelitian, dan publikasi
  media/testimoni dipisahkan.
- Pattern Interrupt belum dinyatakan sebagai terapi atau intervensi yang telah
  terbukti efektif.

## 4. Kesiapan pengujian dan bukti

Workbench Phase 4 telah menyediakan evaluator model, ringkasan latensi,
analisis retensi, analisis Pattern Interrupt, matriks resilience, serta manifest
bukti yang gagal secara aman bila bukti belum lengkap. Instrumentasi Android
dan Windows hanya merekam durasi, skenario, dan versi artefak ketika mode bukti
diaktifkan. Data tersebut tidak memuat konteks penelusuran.

Bukti yang masih harus dikumpulkan oleh tim pada jalur resmi:

1. dataset card, split leakage-safe, lisensi/provenance, dan evaluasi final;
2. matriks perangkat Android dan Windows beserta skenario warm/cold,
   online/offline, foreground/background;
3. skenario kill/recovery aman pada perangkat/VM sekali pakai;
4. definisi retensi, persetujuan penelitian, dan kohort yang memadai;
5. persetujuan etika, review psikologi/aksesibilitas, adverse-event review, dan
   studi Pattern Interrupt;
6. review batasan dan persetujuan reviewer atas setiap hasil agregat.

## 5. Luaran dan status

| Luaran                    | Status saat pembekuan                 | Bukti berikutnya                                         |
| ------------------------- | ------------------------------------- | -------------------------------------------------------- |
| Prototipe Android/Windows | Code-complete; belum device-evaluated | Rilis demo berversi, checksum, matriks perangkat, review |
| Laporan Kemajuan          | Draf lengkap                          | Persetujuan dan receipt submisi                          |
| Laporan Akhir             | Draf kerja                            | Hasil Phase 4, persetujuan, receipt submisi              |
| Akun media sosial         | URL dikonfigurasi                     | Bukti ownership, arsip publikasi, continuity test        |
| Video edukasi             | Paket produksi lengkap                | Render, review, caption check, publication record        |
| Artikel ilmiah            | Draf manuskrip                        | Hasil Phase 4 dan persetujuan penulis/reviewer           |

## 6. Risiko dan mitigasi

| Risiko                                          | Mitigasi                                                                                |
| ----------------------------------------------- | --------------------------------------------------------------------------------------- |
| False positive pada situs pendidikan/pemerintah | Slice evaluasi khusus, threshold review, safe recovery, tanpa klaim sebelum hasil final |
| Izin atau service dinonaktifkan                 | Status kesehatan transparan, recovery aman, accountability, tanpa critical-process API  |
| Kebocoran browsing data                         | Inferensi lokal, denylist skema backend, log redaction, agregasi kasar                  |
| Overclaim efektivitas psikologis                | Review etika/psikologi, bahasa non-klinis, pemisahan asosiasi dan kausalitas            |
| Akun media sosial kehilangan akses              | 2FA, recovery owner, inventaris admin, handover dan continuity drill                    |
| Luaran tidak konsisten                          | Manifest berbasis hash dan traceability requirement-ke-artefak                          |

## 7. Rencana penyelesaian

1. Menjalankan Phase 4 pada dataset, perangkat, VM, dan kohort yang telah
   disetujui.
2. Membekukan versi prototipe serta seluruh hash model/rules/content.
3. Memasukkan hanya hasil agregat yang telah ditinjau ke laporan dan artikel.
4. Meninjau seluruh luaran dari aspek akademik, psikologi, privasi,
   aksesibilitas, dan keamanan klaim.
5. Melakukan submisi/publikasi melalui akun resmi dan merekam receipt/URL/hash.
6. Menjalankan verifier Phase 5 sampai seluruh gerbang bukti diterima.

## 8. Pernyataan status

Dokumen ini siap untuk review, tetapi belum merupakan laporan yang disetujui
atau disubmit. Approval record dan submission record harus diisi oleh pihak
yang benar-benar melakukan tindakan tersebut. Tidak ada automation yang boleh
mengisi tanda tangan, identitas reviewer, receipt, atau status persetujuan
secara fiktif.
