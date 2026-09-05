# **DAFTAR ISI** 

|DAFTAR ISI ............................................................................................................ i|
|---|
|DAFTAR GAMBAR .............................................................................................. ii|
|DAFTAR TABEL .................................................................................................. iii|
|DAFTAR LAMPIRAN .......................................................................................... iv|
|BAB 1. PENDAHULUAN ......................................................................................1|
|1.1 Latar Belakang ...................................................................................................1|
|1.2 Tujuan dan Manfaat ...........................................................................................2|
|1.2.1<br>Tujuan ........................................................................................................2|
|1.2.2<br>Manfaat ......................................................................................................2|
|BAB 2. TARGET LUARAN ...................................................................................2|
|2.1 Target Luaran PKM ...........................................................................................2|
|2.2 Target Luaran Produk Karsa Cipta ....................................................................3|
|BAB 3. TAHAP PELAKSANAAN .........................................................................3|
|3.1 Persiapan Umum ................................................................................................3|
|3.2 Perancangan Sistem ...........................................................................................4|
|3.3 Pembuatan Produk Karsa Cipta/Prototipe ..........................................................5|
|3.4 Pengujian ............................................................................................................6|
|BAB 4. HASIL YANG DICAPAI ...........................................................................6|
|4.1.<br>Hasil Luaran PKM-KC .................................................................................6|
|4.2.<br>Hasil Luaran Prototipe Produk Karsa Cipta ..................................................7|
|BAB 5. POTENSI HASIL .......................................................................................9|
|BAB 6. RENCANA TAHAPAN BERIKUTNYA ..................................................9|
|DAFTAR PUSTAKA ............................................................................................10|
|LAMPIRAN ...........................................................................................................11|
|Lampiran 1. Penggunaan Dana ..............................................................................11|
|Lampiran 2. Bukti-bukti Pendukung Kegiatan ......................................................13|
|Lampiran 3. Rincian Target dan Protokol Pengujian Gamblock-AI .....................14|



i 

# **DAFTAR GAMBAR** 

|Gambar 3.1 Diagram Alir Tahap Pelaksanaan Gamblock-AI .................................3|
|---|
|Gambar 3. 2 Arsitektur Sistem Perlindungan Gamblock-AI ...................................4|
|Gambar 3. 3 Alur Hybrid Analysis dan Pembatasan Akses Gamblock-AI .............4|
|Gambar 3.4 Implementasi Prototipe Gamblock-AI pada Android dan Windows ...5|
|Gambar 3.5 Dokumentasi Gamblock-AI bersama Mahasiswa Universitas|
|Teknologi Yogyakarta ..............................................................................................6|
|Gambar 4. 1 Tampilan Prototipe Gamblock-AI .......................................................8|



ii 

# **DAFTAR TABEL** 

|Tabel 2. 1 Target Luaran Produk Karsa Cipta Gamblock-AI ................................14|
|---|
|Tabel 3. 1 Protokol Pengujian Sistem Gamblock-AI .............................................14|
|Tabel 4. 1 Konten Media Sosial ...............................................................................7|
|Tabel 4. 2 Perbandingan Target dan Capaian Prototipe Gamblock-AI ...................8|



iii 

# **DAFTAR LAMPIRAN** 

|Lampiran 1. Penggunaan Dana ..............................................................................11|
|---|
|Lampiran 1. 1 Rekap Penerimaan Dana .................................................................11|
|Lampiran 1. 2 Rincian penggunaan dana (total_in-cash_Belmawa).......................11|
|Lampiran 1. 3 Bukti Penggunaan Dana .................................................................12|
|Lampiran 2. Bukti-bukti Pendukung Kegiatan ......................................................13|
|Lampiran 3. Rincian Target dan Protokol Pengujian Gamblock-AI .....................14|



iv 

1 

# **BAB 1. PENDAHULUAN** 

# **1.1 Latar Belakang** 

Judi _online_ telah menjadi persoalan digital yang melibatkan pengguna internet pada skala global. Pada kuartal I 2025, 7,7% pengguna internet global berusia 16 tahun ke atas mengakses situs atau aplikasi judi _online_ (We Are Social, 2025). Di Indonesia, keterlibatan pelajar dan mahasiswa dalam judi _online_ menjadi perhatian dalam upaya pencegahan. Kemdiktisaintek mencatat sekitar 960 ribu pemain judi _online_ berasal dari kalangan pelajar dan mahasiswa, dengan jumlah yang didominasi mahasiswa (Kemdiktisaintek, 2024). Data PPATK turut memperlihatkan keterlibatan kelompok usia muda. Pemain berusia 17-19 tahun tercatat melakukan deposit sebesar Rp47,9 miliar pada kuartal I 2025 (PPATK, 2025). Rangkaian data menunjukkan perlunya pencegahan yang menjangkau mahasiswa dan kelompok usia muda secara terarah. 

Keterlibatan mahasiswa dalam judi _online_ juga tercatat di lingkungan perguruan tinggi. Survei terhadap 340 mahasiswa Universitas Negeri Makassar menunjukkan bahwa 13% responden pernah terlibat dalam judi _online_ (Hamid, Nawir and Amahoru, 2023). Keterlibatan mahasiswa dalam judi _online_ berpotensi menimbulkan tekanan finansial dan gangguan psikologis. Kerugian finansial akibat judi _online_ dapat mengganggu stabilitas keuangan pemain (Sriyana, 2025). Pada mahasiswa, judi _online_ juga berkaitan dengan stres, kecemasan, depresi, gangguan pola tidur, dan penurunan kinerja akademik (Wirareja and Sa’adah, 2024). Risiko finansial dan psikologis memperkuat perlunya pencegahan sebelum pengguna melanjutkan akses menuju layanan judi _online_ . Pencegahan perlu membatasi akses sekaligus menyediakan dukungan pemulihan dan sosial setelah pengguna mencoba mengakses layanan judi _online_ (Chandrakumar _et al._ , 2026). 

Pemblokiran situs dan konten merupakan salah satu bentuk pencegahan yang telah dilakukan pemerintah untuk membatasi akses judi _online_ . Kemkomdigi menindak 711.522 konten judi _online_ pada periode 20 Oktober 2024 hingga 6 Januari 2025 (Komdigi, 2025). Pemblokiran berbasis daftar domain memiliki keterbatasan karena hanya mengenali alamat situs yang telah tercatat. Alamat situs baru belum dapat diblokir apabila belum masuk ke dalam daftar pemblokiran. Akibatnya, sebagian halaman judi _online_ masih berpeluang dapat diakses. Diperlukan sistem pencegahan yang memeriksa URL dan teks halaman untuk mengenali indikasi judi _online_ . Kebutuhan teknis dan pemulihan menjadi dasar pengembangan sistem yang mengintegrasikan deteksi, pembatasan akses, dan tindak lanjut pengguna. 

Gamblock-AI dikembangkan untuk melengkapi pemblokiran berbasis daftar statis dengan deteksi lokal dan tindak lanjut pemulihan. Sistem menerapkan _Hybrid Analysis_ memadukan _Logistic Regression_ dan _Rule-Based System_ untuk menganalisis _Uniform Resource Locator (URL)_ serta teks halaman. _Arsitektur OnDevice Artificial Intelligence (On-Device AI)_ menjalankan klasifikasi secara lokal pada Android dan Windows menggunakan artefak _Hybrid_ yang benar-benar dimuat prototipe dengan ukuran gabungan di bawah 5 

2 

MB. Mekanisme pembatasan akses menargetkan waktu respons P95 di bawah 200 ms untuk keseluruhan proses dari pengambilan data hingga pembatasan akses. Saat sistem mengenali indikasi judi _online,_ aplikasi membatasi akses dan menampilkan _Pattern Interrupt_ selama 5-10 detik sebelum mengarahkan pengguna ke laman psikoedukasi. _Social Accountability Protocol_ mengatur persetujuan Pendamping pada penghapusan perlindungan dan pembagian data agregat sesuai izin pengguna. Rancangan ini membantu mahasiswa membatasi akses tanpa mengirim riwayat penelusuran ke peladen eksternal. 

# **1.2 Tujuan dan Manfaat** 

# **1.2.1 Tujuan** 

- a. Menghasilkan sistem klasifikasi konten judi online berbasis _Hybrid Analysis_ dan _On-Device AI_ yang memproses URL serta teks halaman secara lokal menggunakan artefak _Hybrid_ lokal berukuran gabungan di bawah 5 MB. 

- b. Mewujudkan prototipe Gamblock-AI pada Android dan Windows yang mengintegrasikan klasifikasi lokal serta pembatasan akses dalam waktu respons P95 di bawah 200 ms. 

- c. Menghasilkan sistem pencegahan akses judi online bagi mahasiswa yang memadukan _Pattern Interrupt_ , laman psikoedukasi, dan _Social Accountability Protocol._ 

# **1.2.2 Manfaat** 

- a. Memberikan sarana bagi mahasiswa untuk membatasi akses konten judi online pada Android dan Windows serta memperoleh tindak lanjut melalui laman pemulihan. 

- b. Mendukung Pendamping melalui persetujuan penghapusan perlindungan dan pembagian data agregat sesuai izin pengguna tanpa akses terhadap data perambanan atau jurnal pribadi. 

- c. Mendukung pengembangan teknologi melalui penerapan _On-Device AI_ untuk klasifikasi konten lokal yang menjaga privasi pengguna. 

# **BAB 2. TARGET LUARAN** 

# **2.1 Target Luaran PKM** 

Luaran PKM-KC Gamblock-AI terdiri atas luaran wajib dan luaran tambahan. 

# **2.2.1. Luaran Wajib** 

- a. Laporan Kemajuan PKM-KC Gamblock-AI. 

- b. Laporan Akhir PKM-KC Gamblock-AI. 

- c. Prototipe fungsional Gamblock-AI pada Android dan Windows yang mendeteksi serta membatasi akses konten judi _online_ . Prototipe menerapkan _Hybrid Analysis_ berbasis _On-Device Artificial Intelligence_ ( _On-Device AI_ ), _Pattern Interrupt_ , laman web pemulihan, dan _Social Accountability Protocol_ . 

- d. Akun media sosial Gamblock-AI. 

# **2.2.1. Luaran Tambahan** 

- a. Paten Sederhana atas inovasi Gamblock-AI. 



<!-- Start of picture text -->
e Persiapanidentifikasi dankebutuhan 2) Perancangansistem 3) Pembuatanprototipe<br>6 Finalisasiprototipe 6 evaluasiPengujianawal dan ra) Integrasipenyempurnaandan<br><!-- End of picture text -->



<!-- Start of picture text -->
PEMROSESAN LOKAL PADA PERANGKAT LAYANAN TERHUBUNG<br>Hybrid Analysis =e) | He<br>Oe) <7<br><!-- End of picture text -->



<!-- Start of picture text -->
PEMROSESAN LOKAL PADA PERANGKAT<br>i Logistic Regression el)<br>oatcd7<br>1Pola URL + kata/rass JUDI ONLINE<br>| SacesGes>(aae)<br>:\ % }\<br><!-- End of picture text -->



<!-- Start of picture text -->
sraroa wodous<br>coe Tare Geen e @ 6<br>Perlindungan : al =<br>petangkat aktif ’ oo — _s ——<br>Seas Sse<br>Pett<br>serie 1 . €)ea |<br>— © =< paren een<br>Ld cs SD— Coo<br><!-- End of picture text -->

6 

# **3.4 Pengujian** 

Pengujian fungsi dan pengalaman penggunaan dilakukan bersama sembilan mahasiswa Universitas Teknologi Yogyakarta. Peserta mencoba alur Gamblock-AI dan menyampaikan temuan mengenai fungsi serta penggunaan prototipe. Kegiatan ini bersifat formatif untuk menemukan kendala alur, bukan pengukuran _System Usability Scale_ (SUS), skor kuantitatif kegunaan, atau uji efektivitas. Salah satu temuan berkaitan dengan proses uninstall yang tetap gagal meskipun Administrator telah memberikan persetujuan. Temuan tersebut menjadi dasar pengembangan jalur emergency sebagai alternatif ketika Pendamping tidak dapat menyelesaikan proses perizinan. 



Gambar 3.5 Dokumentasi Gamblock-AI bersama Mahasiswa Universitas 

# Teknologi Yogyakarta 

Pengujian teknis menilai kinerja Hybrid Analysis, ukuran artefak Hybrid yang dipakai prototipe, fungsi perlindungan lintas platform, waktu respons, dan kesesuaian alur pemulihan. Uji pengguna terbatas digunakan untuk menemukan kendala fungsi dan langkah penggunaan yang belum berjalan sesuai rancangan. Setiap pengujian memiliki parameter, metode, dan kriteria lulus yang mengacu pada target Bab 2. Rincian protokol disajikan pada Tabel 3.1 di Lampiran 3, sedangkan status bukti dan batasannya dirujuk pada `context/progress-testing.md` dalam repositori proyek. 

# **BAB 4. HASIL YANG DICAPAI** 

Pelaksanaan PKM-KC Gamblock-AI telah mencapai 90% pada tahap penyusunan laporan kemajuan. 

# **4.1. Hasil Luaran PKM-KC** 

# **4.1.1 Laporan Kemajuan** 

Laporan Kemajuan PKM-KC Gamblock-AI telah selesai 100% sesuai target luaran wajib. 

# **4.1.2 Laporan Akhir** 

Laporan Akhir PKM-KC Gamblock-AI berada pada capaian 0% dan akan disusun pada tahap akhir pelaksanaan program. 

# **4.1.3 Prototipe Gamblock-AI** 

Prototipe Gamblock-AI mencapai 80% pada tahap pelaporan. Android dan Windows telah terintegrasi dengan pembatasan akses, _Pattern Interrupt_ , layanan pemulihan, dan _Social Accountability Protocol_ . Tahap berikutnya berfokus pada evaluasi hasil pengujian dan finalisasi prototipe. 

# **4.1.4 Akun Media Sosial** 



<!-- Start of picture text -->
1 e gamblockai. pkmkc ee<br>- e gamblockai.pkmke Niat aja nggak cukup buat<br>mahasiswa itu nyata, Dari masalah finansial<br>“ sampai akademik, masa depanbisa jadi<br>4 taruhannya kalau siklus canduini nggak diputus<br>2 * Kenalin, ini dia Gamblock-Al: Pelindung digital<br>a A pertamamul @ il<br>= me j ‘<br>. ¢*, Cod<br>a * Ae BBD)QSisu’ oleh7 vicore.path den 15 lsinnya A<br>seems m<br><!-- End of picture text -->



<!-- Start of picture text -->
@ gamblockai_pkmkearo ot ZA<br>@ gamblockai.pkmikelepas dari kebiasaanNiatdigitalaja nggakyang merusak!cukup buat@<br>Darurat perilaku digital negatifdi kalangan<br>tegas.tuntasa Dicaravideokerjaini, sistemtim Gamblodk-AIpelindungbakaldigital kita!bedab@<br>Bukan sekadar pemblokir biasa. Kami<br>memadukan kecerdasan buatan dan Behavioral<br>Oo 9 A<br>TAD Disukai oleh derywhy_dan 13 lainnya<br>A<br>©<br>o=~<br>ens 5<br><= S 12%: La]<br><!-- End of picture text -->



<!-- Start of picture text -->
silos oe ;<br>Pectetingetrem urd Y a" ‘ Perlindungan perangkat aktif = \¢é Y/ae<br>pS Nims<br>: = ; : :<br>pene e os<br>—= Ne >| a<br>=<——s<br><!-- End of picture text -->

9 

<u>Tabel 4. 2 Perbandingan Target dan Capaian Prototipe Gamblock-AI</u> 

|<br>**No.**|<br>**Komponen**|<br>**Target**|<br>**Capaian**|<br>|<br>**Status**|
|---|---|---|---|---|---|
|||psikoedukasi,<br>aktivitas,<br>dan<br>evaluasi|tersedia dan<br>digunakan|dapat||
|7|_Social_<br>_Accountabili_<br>_ty Protocol_|Persetujuan<br>Pendamping dan<br>jalur_emergency_<br>melalui<br>Administrator|Jalur utama da<br>_emergency_<br>berfungsi<br>mekanisme<br>persetujuan|n jalur<br>telah<br>sesuai|Tercapai|



# **BAB 5. POTENSI HASIL** 

Gamblock-AI berpotensi dikembangkan sebagai sistem _Digital Wellbeing_ untuk membantu pengguna membatasi akses konten judi online. Perlindungan Android dan Windows serta pemrosesan _On-Device AI_ mendukung penggunaan lintas perangkat dengan data perambanan tetap diproses lokal. Laman pemulihan dan _Social Accountability Protocol_ melengkapi pembatasan akses melalui kegiatan pengendalian diri dan keterlibatan Pendamping sesuai izin pengguna. 

Pengembangan Gamblock-AI dapat diperluas dari mahasiswa menuju perguruan tinggi, institusi pendidikan, dan keluarga. Perluasan penerapan memerlukan peningkatan ketepatan klasifikasi, kestabilan sistem, kompatibilitas perangkat, serta pengujian pengguna yang lebih luas. Paten Sederhana, artikel ilmiah, dan Hak Cipta/Karya Cipta mendukung keberlanjutan pengembangan setelah PKM-KC berakhir. 

Gamblock-AI berpotensi mendukung SDG 3 melalui dukungan awal terhadap perilaku digital berisiko, SDG 4 melalui lingkungan pendidikan yang lebih aman, dan SDG 9 melalui pengembangan teknologi digital yang menjaga privasi pengguna. 

# **BAB 6. RENCANA TAHAPAN BERIKUTNYA** 

Rencana tahapan berikutnya diarahkan untuk menyelesaikan sisa kegiatan hingga mencapai 100% paling lambat 10 September 2026. 

- a. Menyempurnakan prototipe Gamblock-AI berdasarkan hasil pengujian, terutama pada kestabilan Android dan Windows, kompatibilitas peramban, serta alur _emergency_ . 

- b. Melengkapi dokumentasi prototipe, bukti pengujian, dan lampiran pendukung sebagai dasar penyusunan Laporan Akhir PKM-KC. 

- c. Menyelesaikan Laporan Akhir PKM-KC Gamblock-AI berdasarkan hasil pengujian, evaluasi, dan penyempurnaan prototipe. 

- d. Menyelesaikan publikasi media massa serta memantau perkembangan pengajuan Paten Sederhana, artikel ilmiah, dan Hak Cipta/Karya Cipta. 

10 

# **DAFTAR PUSTAKA** 

- Chandrakumar, D. _et al._ (2026) “User Experiences with Blocking Software and Gambling Recovery: Exploring Motivation, Perceptions & Recovery Supports,” _Journal of Gambling Studies_ [Preprint]. Available at: https://doi.org/10.1007/s10899-026-10543-x. 

- Hamid, M.W., Nawir, N. and Amahoru, N.M. (2023) “Jurnal dunia pendidikan,” _Jurnal Dunia Pendidikan_ , 3(November), pp. 67–78. 

- Kemdiktisaintek (2024) _Kemdiktisaintek siap berkolaborasi dalam upaya pencegahan dan penanganan dampak perjudian online_ . Available at: https://kemdiktisaintek.go.id/en/news/article/kemdiktisaintek-siapberkolaborasi-dalam-upaya-pencegahan-dan-penanganan-dampakperjudian-online (Accessed: August 12, 2026). 

- Komdigi (2025) _Sejak awal januari 2025 komdigi telah menindak 43 ribu konten judol_ , _Komdigi_ . Available at: https://www.komdigi.go.id/berita/rilisgpr/detail/sejak-awal-januari-2025-komdigi-telah-menindak-43-ribukonten-judol (Accessed: August 12, 2026). 

- PPATK (2025) _Promensisko 2025: Menjawab ancaman judi online dan kejahatan digital lewat aksi_ , _Pusat Pelaporan dan Analisis Transaksi Keuangan_ . Available at: https://www.ppatk.go.id/siaran_pers/read/1474/promensisko-2025menjawab-ancaman-judi-online-dan-kejahatan-digital-lewat-aksi-.html (Accessed: July 3, 2026). 

- Sriyana (2025) “Judi Online : Dampak Sosial, Ekonomi,” _Sociopolitico_ , 7, pp. 27–34. 

- We Are Social (2025) _Digital 2025: Global overview report_ , _We Are Social_ . Available at: https://wearesocial.com/id/blog/2025/07/digital-2025-julyglobal-statshot-report/ (Accessed: July 12, 2026). 

- Wirareja, Y. and Sa’adah, N. (2024) “Dampak Judi Online terhadap Kesehatan 

   - Mental Mahasiswa,” _Al-Isyraq: Jurnal Bimbingan, Penyuluhan, dan Konseling Islam_ , 7(1), pp. 103–118. Available at: https://jurnal.pabki.org/index.php/alisyraq/article/view/382. 

11 

# **LAMPIRAN** 

# **Lampiran 1. Penggunaan Dana** 

Lampiran 1. 1 Rekap Penerimaan Dana 

|**No.**<br>**Sumber**<br>**Pemasukan**<br>**Jenis**<br>**Dana**|**Jumlah (R**|**p)**|
|---|---|---|
|1.<br>Belmawa<br>_In-cash_|8.000.000|(jumlah|
|sesu|aiperolehanpen|danaan)|
|2.<br>PT (UTY)<br>_In-cash_|1.000.000 – 2.|000.000|
|+_In-kind_<br>(bis|a disesuaikan de|ngan tim|
||masing-|masing)|
|Lampiran 1. 2 Rincianpenggunaan dana(tota|l_in-cash_Belma|wa)<br>|
|||**T**|
|**N**<br>**o.**<br>**Jenis Pengeluaran**<br>**Vol**<br>**ume**|**Harga**<br>**Satuan (Rp)**|**otal**<br>|
|||**(Rp)**|
|1<br>.<br>Belanja Bahan (maks. 60%)|||
|Kabel/engsel/mur/baut dan<br>sejenisnya|||
|Bahan kimia lab/bahan<br>logam/kayu dan sejenisnya|||
|Pakaian tari/kanvas dan cat|||
|Bibit tanaman/simplisia/pupuk|||
|Alat ukir/alat Lukis|||
|Suku<br>cadang/microcontroller/sensor/kit|||
|Bahan lainnya sesuai program<br>PKM-KC|||
|**SUB TOTAL**|||
|2|||
|.<br>Belanja Sewa (maks. 15%)|||
|Sewa alat|||
|Sewa<br>server/hosting/domain/SSL/akses<br>jurnal(maksimal 6 bulan)|||
|Sewa lab (termasuk<br>penggunaan alat lab)|||
|Sewa lainnya sesuai program<br>PKM-KC|||
|**SUB TOTAL**|||



12 

|3<br>.<br>Perjalanan lokal (maks. 30%)<br>|
|---|
|Kegiatanpenyiapan bahan|
|Kegiatanpendampingan|
|Kegiatan lainnya sesuai<br>program PKM-KC|
|**SUB TOTAL**|
|4<br>.<br>Lain-lain (maks. 15 %)|
|_Adsense_akun media sosial<br>(maks. 500.000)|
|Percetakanproduk|
|Lainnya sesuai program<br>PKM-KC|
|**SUB TOTAL**|
|**GRAND TOTAL**|
|**GRAND TOTAL(Contoh: Satu Juta Lima Ratus Empat Puluh Ribu**<br>**Rupiah)**|



Lampiran 1. 3 Bukti Penggunaan Dana 

<mark>Menunjukkan bukti transaksi, seperti kuitansi, nota, e-receipt, dan lain-lain beserta keterangan penggunaannya dan atas nama siapa. (maksimal 6-10 gambar dalam 2-3 halaman).</mark> 

13 

# **Lampiran 2. Bukti-bukti Pendukung Kegiatan** 

<mark>Lampiran 2.1 Bukti aktivitas (foto). Foto menunjukkan proses pembuatan produk/prototipe dan terlihat dengan jelas (maksimal 6-10 gambar dalam 2-3 halaman)</mark> 

1. 

2. 

Lampiran 2.2 Screenshoot gambar pengisian log book <mark>(kegiatan dan keuangan, cukup 1 foto saja masing-masing)</mark> 

1. 

2. 

Lampiran 2.3 Dapat ditambahkan: 

<mark>1. Tautan berkas atau data yang mendukung justifikasi proses riset seperti berkas Ethical Clearence (jika menggunakan EC), Formulir Inform Consent (jika data berupa wawancara), Hasil perolehan data (survei, wawancara, dsb), surat bukti izin penelitian dari lokasi penelitian, hasil olah data, dan sebagainya</mark> 

<mark>2. Hasil Luaran (bukti submit atau publikasi artikel ilmiah ke jurnal/prosiding, publikasi konten di media sosial, dapat ditambahkan performa akun media sosial (jumlah pengikut, jumlah pemirsa konten, jumlah like dan komentar pemirsa pada konten). Dapat ditambahkan pula liputan media massa atau publikasi media cetak/online (Jika ada).</mark> 

14 

# **Lampiran 3. Rincian Target dan Protokol Pengujian Gamblock-AI** 

Lampiran ini memuat rincian target spesifikasi dan protokol pengujian yang dirujuk pada Bab 2 dan Bab 3. 

Tabel 2. 1 Target Luaran Produk Karsa Cipta Gamblock-AI 

|**No.**|**Komponen**|**Target Spesifikasi**|**Justifikasi**|
|---|---|---|---|
|1|Sistem<br>klasifikasi lokal|Hybrid<br>Analysis<br>mengklasifikasikan URL dan<br>teks halaman. Artefak Hybrid<br>yang dimuat prototipe berukuran<br>gabungan di bawah 5 MB dan<br>berjalan lokal.|Analisis URL dan teks<br>halaman<br>mengurangi<br>ketergantungan<br>pada<br>daftar<br>domain<br>serta<br>menjaga<br>data<br>perambanan.|
|2|Aplikasi multi-<br>platform|Mendukung<br>perlindungan<br>pada Android, Windows, dan<br>perambanyangkompatibel.|Dukungan<br>lintas<br>perangkat<br>memperluas<br>penggunaanperlindungan.|
|3|Pembatasan<br>akses|Membatasi akses konten judi<br>online dalam waktu respons<br>di bawah 200 ms.|Respons<br>singkat<br>membantu<br>pembatasan<br>berlangsung<br>segera<br>setelah indikasi dikenali.|
|4|Intervensi<br>dan<br>layanan<br>pemulihan|Menampilkan<br>Pattern<br>Interrupt selama 5-10 detik<br>dan menyediakan layanan<br>pemulihan.|Intervensi<br>menghubungkan<br>pembatasan akses dengan<br>tindak lanjut pengendalian<br>diri.|
|5|Social<br>Accountability<br>Protocol|Menerapkan<br>persetujuan<br>Pendamping, jalur emergency<br>Administrator,<br>dan<br>data<br>agregat sesuai izin pengguna.|Mekanisme<br>persetujuan<br>memberi<br>hambatan<br>prosedural<br>tanpa<br>mengabaikan kendali data<br>pribadi.|



# Tabel 3. 1 Protokol Pengujian Sistem Gamblock-AI 

|**Jenis/Komponen**<br>**yang Diuji **|**Parameter Uji**|**Metode Uji**|**Kriteria Lulus**|
|---|---|---|---|
|_Hybrid Analysis_|_Accuracy_,<br>_precision_,_recall_,<br>_F1-score_, dan_false_<br>_positive rate_|Evaluasi<br>menggunakan 2.592<br>data uji historis dan evaluasi<br>terpisah dengan split bebas leakage|Target laporan current: _Accuracy_,<br>_precision_,_recall_,<br>dan_F1-score_ minimal 90%;<br>_false positive rate_ maksimal 5% pada split bebas leakage|
|_On-Device_<br>_Artificial_<br>_Intelligence_|Ukuran artefak Hybrid<br>yang dimuat dan<br>klasifikasi lokal|Pemeriksaan ukuran gabungan,<br>hash/provenance, dan pelaksanaan<br>klasifikasi pada prototipe|Artefak Hybrid yang dipakai<br>prototipe berukuran di bawah<br>5 MB dan klasifikasi berjalan<br>secara lokal|
|Perlindungan<br>Android,|Keberhasilan<br>klasifikasi dan<br>pembatasan akses|Pengujian fungsi<br>pada Android dan<br>Windows melalui|Perlindungan<br>berjalan pada|



15 

|**Jenis/Komponen**<br>**yang Diuji **|**Parameter Uji**|**Metode Uji**|**Kriteria Lulus**|
|---|---|---|---|
|Windows, dan<br>peramban||peramban yang<br>didukung|lingkungan<br>pengujian|
|Pembatasan akses<br>(checkpoint laporan kemajuan)|Waktu respons<br>input-ke-intervensi terlihat|Pengukuran terkontrol pada APK<br>Research _release_, Android, Chrome,<br>dan skenario _warm foreground online_|P95 waktu respons<br>secara ketat di bawah 200 ms,<br>minimal 30 sampel berhasil,<br>dan tanpa kegagalan aksi blok/visibilitas|
|Regresi dukungan peramban lintas platform|Kesesuaian alur perlindungan pada peramban yang didukung|Satu perangkat Android wajib dengan Chrome, Edge, Brave, dan Firefox; Windows dengan Chrome, Edge, Brave, Opera, dan Firefox bersifat opsional; masing-masing 5 sampel judi dan 5 non-judi|Sampel non-judi menghasilkan _allow_ dan sampel judi menghasilkan _intervention_; evidence Android tercatat, Windows opsional|
|_Pattern Interrupt_,<br>layanan<br>pemulihan, dan<br>_Social_<br>_Accountability_<br>_Protocol_|Durasi interupsi,<br>pengalihan<br>pemulihan,<br>persetujuan<br>Pendamping, dan<br>jalur_emergency_|Pengujian setiap alur<br>fungsi pada prototipe|Setiap fungsi<br>berjalan sesuai<br>rancangan|
|Keseluruhan<br>prototipe|Temuan fungsi dan<br>pengalaman<br>penggunaan|Uji formatif bersama<br>sembilan mahasiswa; studi<br>tugas terstruktur + SUS direncanakan<br>setelah tata kelola disetujui|Kendala formatif<br>terdokumentasi sebagai dasar<br>penyempurnaan; skor SUS hanya<br>dilaporkan dari studi terstruktur|
