# Gamblock-AI: Arsitektur Prototipe On-Device untuk Pemblokiran Judi Online, Pattern Interrupt, dan Akuntabilitas Sosial pada Mahasiswa

Jenis naskah: artikel desain dan prototipe dengan protokol evaluasi

Status: draf manuskrip; belum disubmit atau peer-reviewed

Penulis kelompok: Tim Gamblock-AI, Universitas Teknologi Yogyakarta

Tanggal pembekuan bukti: 2 Agustus 2026

## Abstrak

Perubahan domain, URL dinamis, dan kamuflase konten membatasi efektivitas
pemblokiran judi online berbasis daftar statis. Analisis berbasis cloud juga
berpotensi memperluas pemrosesan data penelusuran yang sensitif. Artikel ini
menjelaskan desain dan status implementasi Gamblock-AI, prototipe Android dan
Windows yang memadukan aturan URL, ekstraksi teks DOM terbatas, Bag-of-Words,
Logistic Regression, Pattern Interrupt 5–10 detik, Social Accountability
Protocol, dan web regulasi diri. Ekstensi Chrome/Edge hanya menjadi sensor
pasif ke WebSocket loopback terautentikasi. Feature extraction, inference,
keputusan blokir, dan Pattern Interrupt dijalankan oleh otoritas native pada
perangkat; URL, domain, DOM, riwayat, screenshot, serta skor halaman tidak
dikirim ke backend. Backend dibatasi pada akun, persetujuan, hubungan
pendamping, pemulihan sukarela, dan agregat non-rekonstruktif. Hasil yang dapat
dilaporkan pada tahap ini adalah prototipe code-complete dan workbench evaluasi
yang terinstrumentasi untuk confusion matrix, Precision, Recall, F1, False
Positive Rate, latensi input-to-visible, resilience, retensi, dan outcome
deskriptif Pattern Interrupt. Belum tersedia dataset final yang disetujui,
bukti perangkat Android/Windows, kohort UTY, atau persetujuan etika studi;
karena itu artikel tidak menyatakan performa atau efektivitas. Kontribusi utama
adalah arsitektur privacy-by-design, pemisahan kewenangan komponen, dan kontrak
bukti fail-closed yang dapat menjadi dasar evaluasi eksternal berikutnya.

Kata kunci: On-Device AI; judi online; Logistic Regression; Bag-of-Words;
Pattern Interrupt; self-regulation; accountability partner; mahasiswa.

## 1. Pendahuluan

PPATK melaporkan perputaran dana judi online Indonesia tahun 2025 sebesar
Rp286,84 triliun dan 12,3 juta orang tercatat melakukan deposit [1]. Kelompok
mahasiswa menghadapi risiko kehilangan dana pendidikan, utang, gangguan
aktivitas akademik, dan tekanan psikologis. Pada saat yang sama, domain baru,
redirect, serta penyamaran konten pada domain legal membuat daftar blokir
memerlukan pembaruan terus-menerus.

Deteksi konten dapat membantu menghadapi perubahan tersebut, tetapi inputnya
sendiri—URL, domain, title, heading, dan anchor text—mengungkap perilaku
penelusuran. On-device machine learning memindahkan inferensi mendekati sumber
data dan relevan untuk kebutuhan latency/privacy dengan tetap menghadapi
batasan komputasi, energi, serta lifecycle artefak [2,3]. Gamblock-AI memilih
model linear ringan dan aturan eksplisit agar pipeline dapat direplikasi pada
Android dan Windows tanpa remote inference.

Pemblokiran teknis saja tidak menjelaskan bagaimana pengguna menghadapi impuls
setelah akses dihentikan. Literatur menunjukkan dukungan intervensi psikologis
untuk gambling disorder, tetapi kualitas dan karakter hasil beragam serta tidak
dapat langsung digeneralisasi pada fitur aplikasi tertentu [4]. Studi
internet-based juga menekankan feasibility dan keterlibatan pengguna [5].
Gamblock-AI karena itu tidak diposisikan sebagai terapi: Pattern Interrupt
memberi jeda singkat dan web berikutnya menerapkan siklus tujuan, pemantauan,
evaluasi, dan penyesuaian yang berangkat dari teori regulasi diri [6].

Artikel ini bertujuan: (1) mendeskripsikan arsitektur lintas platform dan trust
boundary; (2) mendokumentasikan status prototipe tanpa mempromosikan artefak
menjadi hasil evaluasi; dan (3) menyajikan protokol evaluasi teknis,
behavioral, privacy, serta safety yang dapat direproduksi.

## 2. Metode

### 2.1 Proses pengembangan dan traceability

Requirement diturunkan dari proposal PKM-KC menjadi ID terdaftar untuk
platform, AI, blocking, privasi, Pattern Interrupt, accountability, web,
evaluasi, data, konten, dokumentasi, komunikasi, dan publikasi. Target
arsitektur dipisahkan dari status komponen. Label `implemented` hanya diberikan
pada jalur runtime aktif, sedangkan `prototype`, `instrumented`, `planned`, dan
`blocked` digunakan sesuai bukti terlemah yang tersedia.

Workspace terdiri dari aplikasi Flutter/native, ekstensi browser, website,
backend, infrastruktur, serta repository umbrella untuk kontrak/evaluasi.
Setiap komponen memiliki status doc dan linter mandiri. Perubahan kontrak
lintas repository memerlukan sinkronisasi implementasi, dokumentasi, dan
validator.

### 2.2 Pipeline Hybrid Analysis

Input yang didukung dibatasi panjang dan tipenya, lalu diproses melalui:

1. normalisasi URL dan teks title/heading/anchor;
2. perhitungan rule score serta fitur karakteristik URL;
3. pembentukan term-frequency Bag-of-Words untuk unigram/bigram;
4. scaling fitur numerik dan Logistic Regression sigmoid;
5. fusi probabilitas model dan rule score pada threshold artefak;
6. keputusan allow/block lokal.

Implementasi model menggunakan artefak JSON ter-hash agar Android dan Windows
mengonsumsi vocabulary, koefisien, feature ordering, scaler, bias, bobot fusi,
dan threshold yang sama. Library scikit-learn menjadi target pipeline training
yang dapat direproduksi [7], tetapi source training asli untuk artefak yang
sekarang terintegrasi belum tersedia; hal ini dipertahankan sebagai gap.

### 2.3 Android

Accessibility Service menangani input Chrome/Edge yang didukung, debounce,
single-thread local classification, tindakan Back, overlay Pattern Interrupt,
friksi pengaturan/uninstall, grant yang dilindungi Android Keystore, dan
agregat harian allowlisted. Handoff pemulihan hanya menyertakan locale dan
kategori sumber tetap.

### 2.4 Windows

Ekstensi Manifest V3 mengekstrak snapshot terbatas dan menyampaikannya ke
`127.0.0.1` setelah pairing. Ekstensi tidak mengklasifikasikan, memblokir,
menutup tab, mengalihkan halaman, atau menerima perintah blok. LocalSystem
service memiliki pairing, klasifikasi, aggregate counters, DPAPI state, dan
SCM recovery. Agen sesi pengguna memiliki pipe terbatas SID, interaksi UI,
tindakan navigasi yang didukung, dan Pattern Interrupt. Desain tidak memakai
critical-process API.

### 2.5 Pattern Interrupt dan web regulasi diri

Keputusan positif memicu intervensi tujuh detik dengan reduced-motion dan
grounding/help offline. Pengguna dapat melanjutkan ke web tanpa URL/DOM.
Siklus web terdiri dari intention, structured mood/urge check-in, impulse
education, daily self-control mission, explainable skill recommendation, dan
weekly review. Data pemulihan bersifat private-by-default; refleksi/jurnal
dienkripsi sebelum persistence.

### 2.6 Social Accountability Protocol

Mahasiswa mengundang orang tua atau rekan sebaya dan mengonfirmasi relasi serta
kategori agregat. State permintaan pelepasan mencakup pending, approved, denied,
expired, cancelled, normal exit, unsafe exit, dan emergency recovery.
Pendamping tidak memperoleh browsing context atau recovery detail. Mekanisme
memberi friksi sesuai batas OS, bukan uninstall impossibility.

### 2.7 Rencana evaluasi model

Dataset final harus memiliki card yang mencakup source, license, consent,
unit/classes, labeling guide, reviewer agreement, deduplication, camouflage,
benign education/government controls, retention, dan known bias. Split harus
dikelompokkan menurut registrable domain/site family/template, membekukan final
test sebelum calibration, serta menyediakan time-shifted/domain-churn slice.

Laporan menghitung TP, FP, TN, FN, Precision, Recall, F1, dan FPR beserta count
dan uncertainty bila layak. Slice mencakup gambling, dynamic, camouflage,
ordinary benign, government, dan education. Hybrid dibandingkan dengan
rule-only serta model-only. Failure report hanya menggunakan opaque sample ID;
raw URL/DOM tetap di research storage lokal yang disetujui.

### 2.8 Rencana evaluasi latensi dan resilience

Latensi proposal dioperasionalkan sebagai waktu dari input lokal lengkap
hingga frame Pattern Interrupt pertama committed. Report memisahkan extraction,
preprocessing, rules, inference, decision, IPC, UI, p50/p95/p99/maksimum,
warm/cold, online/offline, serta foreground/background pada matriks Android dan
Windows. Target proposal <200 ms tidak dinilai menggunakan model-only timing.

Resilience matrix mencakup restart, reboot, ordinary process kill, service
stop, permission removal, partner state, token expiry/reuse/revoke, emergency,
update/rollback, false-positive recovery, dan accessibility. Semua skenario
berjalan pada perangkat/VM yang dapat dipulihkan tanpa critical-process,
boot-loop, atau destructive lockout.

### 2.9 Rencana evaluasi retensi dan Pattern Interrupt

Retention memerlukan definisi cohort, index event, window, qualifying activity,
withdrawal/deletion/missing-data, minimum suppression, dan interpretasi yang
disetujui sebelum collection. Product consent tidak menjadi research consent.

Studi Pattern Interrupt memerlukan review etika atas populasi, allocation,
outcome, instrument, consent/withdrawal, 5–10 second stimulus, reduced-motion,
photosensitivity, adverse-event, compensation, retention, dan access.
Tahap yang direncanakan adalah expert review, accessibility/usability pilot,
controlled immediate-outcome pilot, recovery-engagement evaluation, lalu studi
preventif lebih besar hanya jika disetujui. Analisis awal bersifat deskriptif
dan tidak menetapkan kausalitas atau manfaat klinis.

## 3. Hasil

### 3.1 Status implementasi

Jalur aplikasi utama telah terhubung pada source dan build configuration:
artefak Hybrid-v2 dikonsumsi Android/Windows, ekstensi melakukan relay lokal
terautentikasi, native authority memiliki block/intervention path, backend dan
website menangani accountability/recovery tanpa browsing schema, dan alat
Phase 4 dapat menghasilkan report agregat yang dibatasi privasi.

Workbenches juga menyediakan manifest yang menolak status final ketika
dataset, device matrix, resilience result, cohort, ethics approval, adverse
event review, limitation review, reviewer, atau hash belum tersedia. Hasil ini
adalah hasil rekayasa prototipe dan instrumentasi, bukan hasil performa.

### 3.2 Performa deteksi

Belum ada final-test report yang memenuhi dataset card, leakage-safe split,
FPR slice, calibration, dan reviewer gate. Accuracy/precision/recall/F1 yang
dibawa metadata artefak berstatus tidak terverifikasi dan tidak dilaporkan
sebagai hasil penelitian.

### 3.3 Latensi dan resilience

Native timing capture serta safe kill/recovery harness tersedia, tetapi belum
ada device matrix lengkap dan report yang disetujui. Target <200 ms dan
ketahanan anti-uninstall karena itu belum dapat dinyatakan tercapai.

### 3.4 Retensi dan outcome psikologis

Belum ada definisi retensi final, cohort yang memenuhi suppression, ethics
approval, atau executed Pattern Interrupt study. Tidak ada hasil efektivitas,
engagement, retention, association, atau causal effect yang dilaporkan.

## 4. Pembahasan

Pemisahan sensor pasif, local protection authority, dan layanan web/server
mengurangi kebutuhan mengirim input deteksi ke sistem eksternal. Model linear
dan aturan eksplisit juga memudahkan parity lintas runtime dan bounded resource
use, meskipun manfaat tersebut tetap perlu diukur. State accountability yang
eksplisit memungkinkan friksi dan jalur keselamatan hidup berdampingan tanpa
mengubah pendamping menjadi pengawas browsing.

Pendekatan fail-closed pada evidence manifest mencegah source code, seeded
metric, atau template kosong dianggap sebagai evaluasi. Ini penting dalam
proyek lintas teknologi dan psikologi karena istilah seperti “akurat”,
“efektif”, atau “aman” memerlukan protokol dan cakupan bukti berbeda.

Trade-off utama adalah coverage. Accessibility dan content-script hanya dapat
menangani browser serta struktur yang dideklarasikan. On-device pipeline harus
mengelola artifact compatibility dan resource constraints. Accountability
tidak boleh menghilangkan kendali OS atau keselamatan pengguna. Recovery web
menambah data sukarela sehingga pernyataan “semua data lokal” harus diganti
dengan penjelasan kategori data yang jujur.

## 5. Etika, privasi, dan keselamatan

Raw browsing input tidak digunakan sebagai production training data. Research
data memerlukan purpose, consent, pseudonym, access, retention, deletion, dan
publication policy terpisah. Partner tidak menerima detail pemulihan. Media
dan testimoni memerlukan publication consent. Pattern Interrupt tidak disebut
terapi, cure, atau proven behavior change. Jalur help/withdrawal, reduced
motion, photosensitivity, dan adverse event wajib sebelum studi manusia.

## 6. Keterbatasan

1. Proposal Markdown kehilangan Fase 1–3 dan bagian akhir Fase 5.
2. Artefak model tidak disertai training source/dataset evidence yang memadai.
3. Tidak ada bukti real-device Android atau signed Windows VM release final.
4. Tidak ada hasil UTY, ethics approval, atau final retention definition.
5. Coverage hanya untuk browser/surface yang dideklarasikan.
6. Generalisasi lintas institusi, populasi, dan jenis perjudian belum dapat
   dilakukan.
7. Code completeness tidak membuktikan absence of privacy/security defects.

## 7. Kesimpulan

Gamblock-AI telah menghasilkan prototipe lintas Android/Windows yang
mengintegrasikan Hybrid Analysis lokal, Pattern Interrupt, accountability, dan
web regulasi diri dengan trust boundary yang eksplisit. Workbench evaluasi
telah terinstrumentasi dan menjaga raw browsing data di perangkat/research
store lokal. Kontribusi performa dan psikologis belum dapat dinilai sebelum
dataset, perangkat, kohort, etika, serta review final tersedia. Penelitian
berikutnya harus menjalankan protokol yang telah dibekukan dan melaporkan hasil
beserta kegagalan serta keterbatasannya.

## Pernyataan ketersediaan data dan kode

Source code berada pada repository komponen Gamblock-AI sesuai kebijakan akses
tim. Raw dataset URL/DOM dan participant rows tidak dipublikasikan dari paket
Phase 5. Publikasi dataset/model/report mengikuti provenance, license, consent,
redaction, dan publication restriction yang disetujui. Evidence publik
menggunakan aggregate report, version, hash, reviewer, dan limitation.

## Pendanaan

Program Kreativitas Mahasiswa Karsa Cipta (PKM-KC) 2026. Detail acknowledgement
akhir harus diselaraskan dengan ketentuan pendanaan resmi sebelum submisi.

## Konflik kepentingan

Tim harus mendeklarasikan konflik kepentingan aktual sebelum submisi. Naskah
ini tidak mencatat adanya conflict assessment yang telah disetujui.

## Referensi

[1] Pusat Pelaporan dan Analisis Transaksi Keuangan. (2026). _Catatan Capaian
Strategis PPATK Tahun 2025_. PPATK.

[2] Wang, X., Tang, Z., Guo, J., Meng, T., Wang, C., Wang, T., & Jia, W. (2025).
Empowering Edge Intelligence: A Comprehensive Survey on On-Device AI Models.
_ACM Computing Surveys, 57_(9), Article 228. https://doi.org/10.1145/3724420

[3] Dhar, S., Guo, J., Liu, J., Tripathi, S., Kurup, U., & Shah, M. (2021). A
Survey of On-Device Machine Learning: An Algorithms and Learning Theory
Perspective. _ACM Transactions on Internet of Things, 2_(3), Article 15.
https://doi.org/10.1145/3450494

[4] Eriksen, J. W., Fiskaali, A., Zachariae, R., Wellnitz, K. B., Oernboel,
E., Stenbro, A. W., Marcussen, T., & Petersen, M. W. (2023). Psychological intervention for gambling
disorder: A systematic review and meta-analysis. _Journal of Behavioral
Addictions, 12_(3), 613–630. https://doi.org/10.1556/2006.2023.00034

[5] Diaz-Sanahuja, L., Suso-Ribera, C., Lucas, I., Jiménez-Murcia, S., Tur, C.,
Gual-Montolio, P., Paredes-Mealla, M., García-Palacios, A., & Bretón-López,
J. M. (2024). A Self-Applied Psychological Treatment for Gambling-Related
Problems via The Internet: A Pilot, Feasibility Study. _Journal of Gambling
Studies, 40_(3), 1623–1651. https://doi.org/10.1007/s10899-024-10318-2

[6] Carver, C. S., & Scheier, M. F. (1998). _On the Self-Regulation of
Behavior_. Cambridge University Press. https://doi.org/10.1017/CBO9781139174794

[7] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel,
O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J.,
Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, É. (2011).
Scikit-learn: Machine Learning in Python. _Journal of Machine Learning
Research, 12_, 2825–2830.
