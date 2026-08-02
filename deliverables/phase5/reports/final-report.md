# Laporan Akhir PKM-KC 2026 — Gamblock-AI

Status dokumen: draf kerja lengkap; finalisasi hasil menunggu evidence manifest
Phase 4 berstatus `evaluated`

Tanggal pembekuan isi: 2 Agustus 2026

Institusi: Universitas Teknologi Yogyakarta

## Abstrak

Gamblock-AI dirancang sebagai prototipe perlindungan digital Android dan
Windows untuk mahasiswa yang menggabungkan deteksi Hybrid Analysis secara
lokal, Pattern Interrupt singkat, Social Accountability Protocol, dan web
psikoedukasi berbasis regulasi diri. Ekstensi browser hanya mengekstrak input
DOM terbatas dan mengirimkannya ke service lokal terautentikasi; klasifikasi,
keputusan, pemblokiran, dan intervensi tetap menjadi kewenangan aplikasi
native. Backend hanya menerima data akun/persetujuan/pemulihan sukarela serta
agregat non-rekonstruktif dan tidak menerima URL, domain, DOM, screenshot, atau
riwayat penelusuran. Implementasi saat ini merupakan prototipe code-complete
dengan instrumentasi evaluasi model, latensi, resilience, retensi, dan Pattern
Interrupt. Karena dataset final, bukti perangkat, kohort UTY, persetujuan etika,
dan review hasil belum tersedia, laporan ini tidak menyatakan nilai Precision,
Recall, F1, False Positive Rate, latensi final, retensi, maupun efektivitas
psikologis. Kontribusi yang telah dapat diverifikasi adalah arsitektur dan
integrasi prototipe yang menjaga pemrosesan browsing tetap pada perangkat,
beserta paket evaluasi yang gagal secara aman ketika bukti belum lengkap.

Kata kunci: judi online, On-Device AI, Logistic Regression, Pattern Interrupt,
regulasi diri, accountability partner, privasi.

## 1. Pendahuluan

Judi online menimbulkan risiko finansial, akademik, sosial, dan psikologis bagi
mahasiswa. Daftar blokir domain statis tidak memadai ketika operator mengganti
domain, mengubah URL, atau menyamarkan konten pada domain legal. Di sisi lain,
pemantauan berbasis cloud dapat memperluas risiko privasi karena input deteksi
merupakan data browsing sensitif. Program ini menggabungkan deteksi konten
lokal dengan hambatan prosedural yang aman dan tindak lanjut regulasi diri.

Tujuan program adalah menghasilkan prototipe Android/Windows yang mampu
memproses karakteristik URL dan DOM pada perangkat, memicu pemblokiran serta
Pattern Interrupt saat keputusan positif, meminta persetujuan pendamping untuk
pelepasan perlindungan, dan menawarkan pemulihan berbasis web tanpa membawa
konteks browsing.

## 2. Landasan desain

### 2.1 Hybrid Analysis

Pipeline menggabungkan rule-based URL features dengan Bag-of-Words dan
Logistic Regression atas teks title, heading, dan anchor. Model ringan dipilih
agar inferensi dapat dijalankan pada perangkat. Threshold dan bobot fusi yang
terintegrasi diperlakukan sebagai input rekayasa yang harus dikalibrasi, bukan
angka mandat proposal atau hasil evaluasi proyek.

### 2.2 Pattern Interrupt dan regulasi diri

Intervensi visual 5–10 detik dimaksudkan untuk memberi jeda pada momen akses,
bukan untuk menggantikan layanan klinis. Handoff berikutnya mengarahkan
pengguna ke niat perubahan, pemantauan mood/dorongan, edukasi, misi harian,
pengembangan keterampilan, dan evaluasi mingguan sebagai siklus goal,
self-monitoring, evaluation, dan behavioral adjustment.

### 2.3 Akuntabilitas sosial

Pendamping yang menerima undangan dapat meninjau permintaan pelepasan
perlindungan dan agregat yang secara eksplisit dibagikan. Friksi tidak boleh
berubah menjadi pengawasan tersembunyi atau penguncian perangkat yang tidak
dapat dipulihkan. Emergency recovery terpisah, terbatas, device-bound, dan
diaudit.

### 2.4 Privasi menurut desain

Input dan keputusan deteksi adalah data lokal. Server tidak menyediakan field
untuk URL/domain/DOM/history/screenshot/per-page score. Journal dan refleksi
sensitif dienkripsi sebelum persistence. Ekstensi tetap pasif, sedangkan
Android Accessibility Service dan Windows LocalSystem service menjadi
otoritas perlindungan sesuai batas platform.

## 3. Metode pengembangan

Program menggunakan lima repository komponen dan satu repository umbrella:

1. Flutter/native Android dan Windows untuk perlindungan lokal;
2. ekstensi Chrome/Edge sebagai sensor Windows pasif;
3. backend Go untuk akun, consent, accountability, pemulihan, agregat, konten,
   dan metadata rilis;
4. website Next.js untuk psikoedukasi, regulasi diri, accountability, dan
   transparansi publik;
5. infrastruktur Ansible/Docker/Caddy untuk delivery operasional;
6. umbrella context/evaluation untuk kontrak, traceability, dan bukti.

Pengembangan memisahkan target proposal, keputusan produk pendukung, status
implementasi, dan bukti evaluasi. Setiap klaim final harus terhubung ke versi,
protokol, dataset/perangkat/kohort, prosedur analisis, reviewer, tanggal,
path/hash, limitation, dan langkah demo.

## 4. Implementasi prototipe

### 4.1 Android

Accessibility Service aktif menangani input Chrome/Edge yang didukung,
klasifikasi lokal, navigasi block, overlay Pattern Interrupt, friksi pengaturan,
grant Keystore, dan agregat. Jalur code-complete ini belum menjadi bukti bahwa
setiap skenario berfungsi pada matriks perangkat nyata.

### 4.2 Windows

Service LocalSystem menangani pairing loopback, klasifikasi, DPAPI state,
agregat, dan SCM recovery. Agen sesi pengguna menangani UI Flutter, pipe
terbatas SID, tindakan navigasi, friksi pengaturan, dan Pattern Interrupt.
Critical-process API tidak digunakan. Build/VM trace final masih menjadi
gerbang eksternal.

### 4.3 Website dan backend

Website mengimplementasikan alur inti regulasi diri dan permukaan pendamping
berbasis consent. Backend mempertahankan RBAC `user`, `partner`, dan `admin`,
state approval, audit, enkripsi recovery-sensitive text, agregat terbatas,
content governance, serta release metadata. Detail browsing tidak tersedia
pada kontrak server.

## 5. Metode evaluasi

Evaluasi final harus menjawab pertanyaan yang terpisah:

1. performa Hybrid Analysis menggunakan confusion matrix, Precision, Recall,
   F1, FPR, slice pendidikan/pemerintah, ablation, dan error analysis;
2. latensi input-lengkap-ke-frame-intervensi pada matriks Android/Windows,
   termasuk p50/p95/p99/maksimum dan warm/cold;
3. resilience terhadap restart, process kill, permission removal, partner
   state, emergency recovery, update/rollback, dan false-positive recovery;
4. retensi berdasarkan definisi/kohort/periode/consent/suppression yang
   disetujui sebelum pengumpulan;
5. keamanan, aksesibilitas, dan outcome deskriptif Pattern Interrupt melalui
   protokol yang telah memperoleh review etika.

## 6. Hasil

### 6.1 Hasil implementasi

Hasil yang sudah didukung bukti repository adalah prototipe code-complete,
kontrak privasi lintas komponen, jalur Hybrid-v2 pada Android/Windows,
intervensi tujuh detik, accountability state, recovery loop, dan instrumentasi
Phase 4. Paket Phase 5 juga menyediakan dokumentasi penggunaan, traceability,
materi diseminasi, manuskrip, serta verifier bukti.

### 6.2 Hasil evaluasi model dan perangkat

Belum tersedia hasil final yang dapat dilaporkan. Nilai yang berasal dari
metadata model pemasok tetap `reported_metrics_unverified` dan tidak boleh
dipindahkan ke tabel hasil. Bagian ini hanya boleh diperbarui dari manifest
Phase 4 yang telah ditinjau dan berstatus `evaluated`.

### 6.3 Hasil retensi dan Pattern Interrupt

Belum tersedia kohort atau studi yang memenuhi persetujuan etika dan gerbang
suppression. Tidak ada klaim perubahan perilaku, efektivitas preventif, atau
kausalitas pada versi laporan ini.

## 7. Pembahasan

Arsitektur menunjukkan bahwa pembagian tanggung jawab dapat menjaga input
browsing tetap lokal sambil menyediakan layanan akun, consent, accountability,
dan pemulihan berbasis web. Pemisahan service dan agen Windows menghindari
pemberian kewenangan interaksi UI kepada LocalSystem, sedangkan pemisahan
ekstensi pasif dari blocking authority mencegah perluasan trust boundary.

Namun, code completeness bukan bukti performa atau keamanan operasional.
False positive pada situs pendidikan/pemerintah, variasi Accessibility API,
perilaku browser dinamis, signed delivery, recovery setelah kill, kualitas
dataset, dan outcome psikologis hanya dapat ditentukan melalui evaluasi yang
direncanakan. Keterbatasan ini mencegah generalisasi tentang semua browser,
semua aktivitas jaringan, atau seluruh mahasiswa.

## 8. Keterbatasan

- Ekstraksi proposal yang tersedia kehilangan Fase 1–3 dan berhenti di tengah
  paragraf Fase 5; cakupan akhir harus dibandingkan dengan PDF/DOC asli.
- Dataset card, provenance, labeling review, split manifest, dan kalibrasi
  final belum disetujui.
- Android dan Windows belum memiliki matriks perangkat/VM yang ditinjau.
- Rilis saat ini berupa scaffolding/debug; belum ada dasar untuk menyebutnya
  signed production release.
- Retention rate belum memiliki definisi akademik final.
- Pattern Interrupt belum memiliki bukti efektivitas atau kelayakan klinis.
- Social-media ownership, publication archive, dan continuity belum dibuktikan.
- Hasil UTY belum tersedia sehingga generalisasi populasi tidak dapat dibuat.

## 9. Etika dan perlindungan peserta

Penggunaan produk tidak otomatis mendaftarkan pengguna sebagai peserta riset.
Penelitian membutuhkan consent terpisah, pseudonymization, tujuan/retensi,
withdrawal, suppression, dan akses terbatas. Materi Pattern Interrupt harus
melewati review psikologi, photosensitivity, reduced-motion, accessibility,
dan adverse-event response. Testimoni, foto, suara, atau identitas mahasiswa
tidak digunakan tanpa consent publikasi khusus.

## 10. Kesimpulan

Gamblock-AI telah mencapai prototipe code-complete dan menyiapkan alat evaluasi
yang diperlukan untuk menguji deteksi, latensi, resilience, retensi, dan
Pattern Interrupt secara terukur. Arsitektur mempertahankan klasifikasi serta
keputusan pada perangkat dan membatasi server pada data yang tidak memuat
konteks browsing. Kesimpulan performa dan efektivitas belum dapat diberikan
sebelum Phase 4 selesai dan ditinjau. Versi final laporan wajib mengganti
pernyataan status ini hanya dengan hasil agregat yang terhubung ke bukti
immutable.

## 11. Luaran

- Prototipe Android/Windows dan dokumentasi penggunaan: disiapkan; validasi
  rilis/perangkat menunggu.
- Laporan kemajuan dan laporan akhir: draf lengkap; approval/submission menunggu.
- Akun media sosial: link dikonfigurasi; ownership/archive/continuity menunggu.
- Video edukasi: paket produksi dan caption disiapkan; render/review/publikasi
  menunggu.
- Artikel ilmiah: manuskrip disiapkan; hasil/review penulis menunggu.

## 12. Lampiran yang harus menyertai versi final

1. evidence manifest Phase 4 dan Phase 5;
2. matriks requirement-to-evidence;
3. release record Android/Windows beserta checksum/signature state;
4. approval dan submission receipt laporan;
5. account ownership dan social publication archive;
6. video review/publication record;
7. manuscript author/reviewer approval;
8. limitation and ethics review.
