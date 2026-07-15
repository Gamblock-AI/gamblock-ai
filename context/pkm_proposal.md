1 

# **BAB 1 PENDAHULUAN** 

# **1.1 Latar Belakang** 

Indonesia menghadapi darurat judi online dengan skala kerugian ekonomi yang luar biasa. Sepanjang tahun 2025, nilai perputaran dana judi online mencapai Rp286,84 triliun dengan 12,3 juta orang tercatat melakukan deposit judi online (PPATK, 2026). Kelompok yang rentan terdampak juga mencakup generasi muda, termasuk pelajar dan mahasiswa. Pada periode sebelumnya, PPATK mencatat sekitar 440.000 pemain berusia 10-20 tahun dan 520.000 pemain berusia 21-30 tahun terlibat dalam aktivitas judi online (PPATK, 2025). Dampak pada kelompok mahasiswa bersifat destruktif dan berlapis, mulai dari penyalahgunaan uang kuliah, keterlibatan pinjaman online ilegal, hingga gangguan psikologis berat berupa stres, kecemasan, dan depresi akibat kerugian finansial. Kementerian Komunikasi dan Digital (Kemkomdigi) telah menangani lebih dari 5,5 juta konten judi online sejak 2017 hingga Januari 2025 (Kemkomdigi, 2025), namun siklus perjudian tidak kunjung putus karena operator situs judi secara masif mengganti domain dan _Uniform Resource Locator (URL)_ segera setelah pemblokiran berlaku. Operator bahkan kerap membajak domain instansi pemerintahan dan pendidikan yang sulit terdeteksi oleh sistem pemblokiran berbasis _Domain Name System (DNS)_ konvensional. Mahasiswa berada dalam fase perkembangan yang rentan, di mana kontrol impuls belum sepenuhnya matang, sehingga pemblokiran akses tanpa tindak lanjut psikologis sering memicu efek reaktansi berupa pencarian jalur alternatif melalui _Virtual Private Network (VPN)_ atau _proxy_ . 

Permasalahan judi online di kalangan mahasiswa memerlukan solusi yang lebih dari sekedar pemblokiran teknis konvensional. Deteksi berbasis daftar ( _blacklist_ ) domain atau URL statis tidak lagi efektif menghadapi situs judi yang bersifat dinamis dan berkamuflase di balik konten situs legal. Analisis lebih mendalam hingga ke konten halaman ( _Document Object Model/DOM_ ) menjadi kebutuhan mendesak agar sistem mampu mengenali situs judi online secara akurat. Sistem memerlukan mekanisme intervensi psikologis yang bekerja secara otomatis pada momen kritis, yaitu ketika pengguna sedang aktif mengakses situs judi online. Belum ada sistem yang mengintegrasikan deteksi cerdas berbasis konten dengan intervensi psikologis otomatis dalam satu platform yang tahan manipulasi. Tujuan pengembangan yang ditargetkan adalah terciptanya prototipe aplikasi _multiplatform_ yang mampu mendeteksi dan memblokir konten judi online secara akurat, memberikan intervensi psikologis _real-time_ , serta mencegah pencopotan aplikasi secara sepihak oleh pengguna. 

Tim Pengusul mengusulkan pengembangan sistem pemblokiran cerdas berbasis aplikasi _multi-platform_ ( _mobile_ dan _desktop_ ) yang memadukan pendekatan teknologi _Artificial Intelligence (AI)_ dan psikologi perilaku. Berbeda dengan pemblokiran konvensional, aplikasi _multi-platform_ beroperasi di latar belakang sistem ( _background service_ ) menggunakan arsitektur _On-Device Artificial Intelligence (On-Device AI)_ untuk menjamin privasi pengguna. Sistem 

2 

menggabungkan metode _Rule-Based_ dan _Logistic Regression_ guna menganalisis karakteristik URL serta konten halaman (DOM) secara _real-time_ untuk mendeteksi situs judi online yang berkamuflase. Keunggulan utama sistem terletak pada mekanisme pertahanan ganda berupa integrasi fitur _Accountability Partner_ yang mencegah penghapusan aplikasi tanpa persetujuan pendamping yang terdaftar. Selain fitur _Accountability Partner_ , sistem menerapkan intervensi bertingkat yang memadukan _shock therapy visual (Pattern Interrupt)_ dengan rehabilitasi psikologis berbasis web sebagai tindak lanjut pascapemblokiran. Sistem pemblokiran diproyeksikan menjadi alat bantu kontrol diri ( _self-control tool_ ) yang komprehensif dan tahan manipulasi guna menekan prevalensi judi online di kalangan mahasiswa. 

# **1.2 Gagasan Karsa Cipta** 

Tim Pengusul menggagas pengembangan sistem pertahanan digital lintas platform ( _multi-platform system_ ) berbasis aplikasi _mobile_ (Android) dan _desktop_ (Windows) untuk mendeteksi serta memblokir akses situs judi online secara mandiri dan berkelanjutan. Berbeda dengan pemblokir konvensional yang hanya bekerja pada level peramban, sistem pertahanan digital beroperasi di latar belakang perangkat ( _background service_ ) sehingga memberikan perlindungan menyeluruh terhadap seluruh aktivitas jaringan pengguna. Inti kecerdasan sistem terletak pada arsitektur _On-Device AI_ yang memproses seluruh data secara lokal tanpa mengirimkan informasi pengguna ke server eksternal. Arsitektur _On-Device AI_ menjamin keamanan data pribadi sesuai prinsip minimalisasi data dalam UndangUndang Perlindungan Data Pribadi (UU PDP), sekaligus menjawab hambatan adopsi aplikasi pengawasan konvensional yang selama ini dianggap mengancam privasi pengguna. Sistem pertahanan digital diproyeksikan menjadi solusi kontrol diri pertama yang menggabungkan kecerdasan buatan _on-device_ dengan intervensi psikologis otomatis dalam satu ekosistem aplikasi terpadu. 

Kebaruan pertama sistem terletak pada kedalaman analisis deteksi yang melampaui pendekatan _blacklist_ konvensional melalui metode _Hybrid Analysis_ . Metode _Hybrid Analysis_ menggabungkan _Rule-Based System_ untuk mengenali pola alamat situs judi online yang eksplisit, dengan model _Machine Learning_ berbasis _Logistic Regression_ yang diperkuat melalui analisis konten halaman ( _DOM Analysis_ ). Pada tahap analisis DOM, sistem mengekstrak teks dari elemen kunci halaman seperti _title_ , _heading_ , dan _anchor text_ , kemudian merepresentasikan teks tersebut menggunakan _Bag-of-Words (BoW)_ menjadi vektor fitur numerik yang dapat diproses model. Kombinasi fitur URL dan fitur konten halaman memungkinkan sistem membedakan secara akurat antara situs legal dan situs judi online yang melakukan kamuflase, misalnya situs yang menumpang pada domain pemerintah atau lembaga pendidikan. Pendekatan berlapis _Hybrid Analysis_ meminimalkan risiko pemblokiran keliru ( _false positive_ ) yang selama ini menjadi kelemahan utama sistem deteksi berbasis daftar statis. 

Kebaruan kedua terletak pada integrasi mekanisme kontrol sosial dan intervensi psikologis singkat ( _micro-intervention_ ) yang bekerja secara otomatis 

3 

pascadeteksi. Sistem menerapkan fitur _Accountability Partner_ , di mana proses penghapusan aplikasi memerlukan persetujuan eksplisit dari pendamping yang terdaftar, baik orang tua maupun rekan sebaya. Mekanisme _Accountability Partner_ menjadikan proses pencopotan aplikasi kompleks secara prosedural ( _high friction_ ) dibandingkan ekstensi peramban biasa, tanpa melanggar batasan sistem operasi yang berlaku. Selain itu, saat indikasi judi terdeteksi, sistem secara otomatis menayangkan animasi grafis singkat berdurasi 5-10 detik yang dirancang untuk memutus respons impulsif pengguna melalui mekanisme _Pattern Interrupt_ . Target fungsional program adalah terciptanya prototipe aplikasi _mobile_ dan _desktop_ yang stabil, mampu melakukan pemblokiran konten judi secara _real-time_ dengan akurasi tinggi, tahan terhadap upaya manipulasi sepihak oleh pengguna, serta memberikan dampak psikologis preventif melalui intervensi visual yang terukur. 

# **1.3 Kemutakhiran Iptek yang Diadopsi** 

Berbeda dengan sistem keamanan berbasis _cloud_ yang mengirimkan data pengguna ke server eksternal, sistem yang dikembangkan menerapkan arsitektur _On-Device AI_ dengan paradigma _Edge Computing_ . Seluruh proses komputasi, mulai dari ekstraksi fitur hingga inferensi keputusan blokir, dieksekusi secara lokal dengan memanfaatkan _Accessibility Service_ pada platform _mobile_ dan _System Service_ pada platform _desktop_ . Kedua antarmuka layanan tersebut dipilih secara khusus karena memungkinkan inspeksi elemen layar secara _real-time_ yang tidak dapat dilakukan oleh aplikasi standar, dengan distribusi aplikasi yang disesuaikan dengan mekanisme instalasi pada tiap platform untuk mendukung akses fitur intervensi secara optimal. Arsitektur _On-Device AI_ memastikan kepatuhan terhadap prinsip minimalisasi data sesuai Undang-Undang Perlindungan Data Pribadi, karena tidak ada data riwayat penelusuran maupun tangkapan layar yang dikirimkan keluar dari perangkat pengguna. Penggunaan algoritma _Logistic Regression_ dipilih secara spesifik karena karakteristiknya yang ringan ( _lightweight_ ) dengan kompleksitas komputasi rendah, sehingga mampu berjalan efisien di latar belakang perangkat _mobile_ maupun _desktop_ tanpa membebani kinerja sistem. 

Kemutakhiran berikutnya terletak pada pembaruan mekanisme intervensi pascapemblokiran yang menggantikan halaman peringatan statis dengan pendekatan _Pattern Interrupt_ berbasis stimulus visual mendadak. Saat situs judi terdeteksi, sistem secara otomatis menayangkan animasi grafis singkat berdurasi 5- 10 detik yang dirancang secara psikologis untuk memutus respons impulsif pengguna sebelum dorongan perjudian menguat. Mekanisme _Pattern Interrupt_ menggantikan pendekatan edukasi konvensional yang cenderung bersifat pasif dan tidak memberikan koreksi perilaku pada momen kritis. Selain mekanisme _Pattern Interrupt_ , sistem juga mengadopsi _Social Accountability Protocol_ sebagai lapisan deterensi psikologis dengan memanfaatkan _Accessibility API_ untuk memantau menu pengaturan dan memicu verifikasi ganda saat sistem mendeteksi indikasi penghapusan aplikasi. Kombinasi _Pattern Interrupt_ dan _Social Accountability Protocol_ menjadikan sistem tahan terhadap upaya manipulasi sepihak oleh 

4 

pengguna, sekaligus memberikan penanganan komprehensif yang mencakup dimensi teknis dan psikologis secara bersamaan. 

# **1.4 Potensi Program** 

Potensi utama program terletak pada terwujudnya instrumen _Digital Wellbeing_ yang efektif menurunkan prevalensi kecanduan judi online di kalangan mahasiswa melalui pendekatan kuratif dan preventif secara bersamaan. Arsitektur aplikasi _multi-platform_ yang fleksibel memungkinkan sistem diadaptasi sebagai standar keamanan jaringan di lingkungan institusi pendidikan, sekaligus berfungsi sebagai alat pengawasan parental di lingkungan keluarga dengan cakupan yang lebih luas. Fitur keamanan _anti-uninstall_ melalui mekanisme _Social Accountability Protocol_ menjadikan sistem memiliki ketahanan penggunaan jangka panjang yang tidak dimiliki oleh aplikasi pemblokiran konvensional. Selain dampak sosial, program turut berkontribusi pada pengembangan ilmu pengetahuan terkait penerapan _On-Device AI_ untuk analisis konten web berbasis DOM yang efisien dalam penggunaan sumber daya komputasi. Program juga membuka peluang pembuktian empiris efektivitas intervensi psikologis berbasis _Pattern Interrupt_ dalam merekayasa perilaku digital pengguna, yang dapat menjadi landasan penelitian lanjutan di bidang psikologi siber dan keamanan digital. 

# **1.5 Luaran PKM Karsa Cipta** 

Luaran yang dihasilkan meliputi: 

- a. Laporan Kemajuan, 

- b. Laporan Akhir, 

- c. Prototipe, 

- d. Akun Media Sosial. 

# **1.6 Kesesuaian Proposal dengan Tema PKM** 

Proposal berjudul “Gamblock-AI: Sistem Pemblokiran Judi Online Berbasis On-Device Artificial Intelligence dengan Mekanisme Pattern Interrupt dan Social Accountability Protocol untuk Mahasiswa” sesuai dengan Tema PKM 2026, yaitu Penguatan Pendidikan, Sains, dan Teknologi, karena memanfaatkan teknologi informasi dalam menghasilkan solusi preventif terhadap permasalahan judi online dalam ranah pendidikan. 

# **BAB 2 TINJAUAN PUSTAKA** 

# **2.1 Kajian Hasil Penelitian** 

Berdasarkan tinjauan pustaka yang dilakukan terhadap penelitian terdahulu dengan tema serupa, Tim Pengusul mengintegrasikan temuan-temuan yang relevan untuk mendukung fokus utama produk yang dikembangkan. Kajian terdahulu dikelompokkan dalam dua domain utama, yaitu domain deteksi teknis dan domain dampak sosial judi online. Pada domain deteksi teknis, Nurseno et al., (2024) mendeteksi situs judi online tersembunyi pada domain pemerintah menggunakan algoritma _web scraping_ berbasis kata kunci statis, namun pendekatan tersebut rentan terhadap situs yang secara aktif memodifikasi konten dan struktur URL. 

5 

Zhang et al., (2025) meningkatkan akurasi deteksi pada URL dinamis menggunakan _Logistic Regression_ , sementara Herrera dan Téllez (2025) membuktikan bahwa representasi teks berbasis BoW efektif digunakan sebagai fitur pendukung klasifikasi konten terkait judi online. Pada domain dampak sosial, Sahputra et al., (2022) dan Lubis et al., (2023) mengonfirmasi bahwa intervensi hukum dan pemblokiran teknis semata gagal menekan adiksi judi pada remaja tanpa disertai rehabilitasi perilaku yang terstruktur. 

Kajian terdahulu menunjukkan bahwa belum ada penelitian yang mengintegrasikan deteksi cerdas berbasis konten halaman ( _DOM Analysis_ ) dengan intervensi psikologis otomatis dalam satu sistem terpadu. Produk yang dikembangkan Tim Pengusul mengisi kekosongan tersebut melalui arsitektur _OnDevice AI_ yang tidak hanya memblokir akses situs judi secara akurat, tetapi sekaligus memberikan koreksi perilaku _real-time_ melalui mekanisme _Pattern Interrupt_ pada momen kritis saat akses berlangsung. 

# **2.2 Landasan Teori** 

# **2.2.1 Psikoedukasi dan Modifikasi Perilaku sebagai Dasar Tindak Lanjut** 

Pencegahan kecanduan judi online tidak cukup hanya dengan pemblokiran akses secara teknis, tetapi juga memerlukan penguatan perilaku penggunanya secara paralel. Konseling behavioral dengan pendekatan modifikasi perilaku menekankan pengendalian stimulus, peningkatan pengendalian diri, dan pembentukan perilaku alternatif yang lebih adaptif. Pendekatan psikologis terbukti membantu menurunkan intensitas perilaku judi online pada kelompok mahasiswa (Duran et al., 2024). Tindak lanjut pascapemblokiran berupa edukasi singkat dan penguatan pencegahan menjadi rasional karena membantu pengguna mengelola dorongan impulsif dan mengurangi peluang akses ulang ke situs judi. 

# **2.2.2 Dukungan Intervensi Psikologis dan Intervensi Berbasis Internet** 

Bukti meta-analitik menunjukkan bahwa intervensi psikologis mampu memberikan dampak signifikan pada gangguan judi, sehingga aspek edukasi dan dukungan perilaku relevan diintegrasikan sebagai penguatan pencegahan pascapemblokiran (Eriksen et al., 2023). Intervensi berbasis internet juga terbukti memiliki efektivitas pada sejumlah luaran perilaku, meskipun tingkat keberhasilannya dipengaruhi oleh keterlibatan aktif pengguna selama proses intervensi berlangsung (Diaz-Sanahuja et al., 2024). Kedua temuan tersebut memperkuat relevansi laman web psikoedukasi sebagai komponen intervensi lanjutan dalam sistem yang dikembangkan. 

# **2.2.3** **_Integrasi Pattern Interrupt_ dan** **_Self-Regulation Theory_ pada Web Psikoedukasi** 

Sistem pemblokiran judi online menerapkan konsep _Pattern Interrupt_ , yaitu teknik pemutusan pola pikir otomatis melalui stimulus visual mendadak berupa video animasi singkat untuk menghentikan dorongan impulsif pada momen situs judi pertama kali diakses. Setelah impuls terputus, sistem mengarahkan pengguna ke laman web psikoedukasi yang dirancang berlandaskan _Self-Regulation Theory_ 

6 

(Carver dan Scheier, 1998), yakni teori yang menjelaskan regulasi diri sebagai proses pengendalian perilaku siklikal mencakup penetapan tujuan, pemantauan diri, evaluasi, dan penyesuaian perilaku secara berkelanjutan. Laman web psikoedukasi mengadaptasi teori tersebut melalui fitur penetapan niat perubahan diri, konten edukasi kesadaran impulsif, _mood tracker_ , misi harian pengendalian diri, dan rekomendasi pengembangan keterampilan sebagai satu ekosistem rehabilitasi mandiri. 

# **2.2.4** **_On-Device AI_ dan** **_Edge Computing_ untuk Perlindungan Privasi** 

_On-Device Artificial Intelligence (On-Device AI)_ atau _Edge AI_ adalah paradigma komputasi di mana pemrosesan data dan inferensi model dilakukan secara lokal pada perangkat pengguna, bukan di server awan ( _cloud_ ) (Wang et al., 2025). Paradigma _On-Device AI_ meminimalkan ketergantungan pada koneksi internet, menurunkan latensi pemrosesan, dan meningkatkan keamanan privasi karena data riwayat penelusuran tidak perlu ditransmisikan keluar dari perangkat. Dalam konteks pemblokiran judi online, penggunaan algoritma _Logistic Regression_ sangat relevan karena karakteristiknya yang ringan ( _lightweight_ ) dengan kompleksitas komputasi rendah, sehingga mampu berjalan efisien di latar belakang perangkat _mobile_ maupun _desktop_ tanpa membebani kinerja sistem. 

# **BAB 3 TAHAP PELAKSANAAN** 

# **3.1 Alat dan Bahan** 

# **3.1.1 Alat yang Digunakan** 

Pengembangan sistem menggunakan alat bantu perangkat keras dan perangkat lunak sebagai berikut: 

- a. Perangkat Keras: Laptop/PC (spesifikasi min. prosesor Intel Core i5/AMD Ryzen 5, RAM 8GB) untuk _coding_ dan pelatihan model, serta Smartphone (Android) sebagai media pengujian aplikasi _mobile_ . 

- b. Perangkat lunak: Sistem Operasi (Windows), Editor Kode (Webstorm/Android Studio), Framework _Multi-platform_ (Flutter) untuk membangun aplikasi _background service_ , Bahasa Python dengan pustaka Scikit-learn untuk pelatihan model AI, Figma untuk desain UI/UX, serta Git/GitHub untuk manajemen versi. 

# **3.1.2 Bahan yang Digunakan** 

Bahan pengembangan bersifat non-fisik dan mencakup: 

- a. Dataset Latih: Kumpulan URL dan data halaman (DOM) yang terlabeli kategori "Judi" dan "Non-Judi" untuk melatih model _Logistic Regression_ . 

- b. Konten Intervensi: Aset video animasi grafis singkat (durasi 5-10 detik) sebagai materi _Pattern Interrupt_ dan elemen visual antarmuka aplikasi. 

- c. Dokumen Pendukung: Algoritma protokol keamanan ( _Accountability Partner Logic_ ) dan referensi literatur terkait psikologi siber. 



<!-- Start of picture text -->
PENGEMBANGAN INTEGRASI<br>MODEL Al DAN<br>oe PENGUJIAN<br>SISTEM<br>PERSIAPANPENGUMPULANDATA DAN Boric PELAPORANFINALISASIDAN<br><!-- End of picture text -->

8 

yang mengimplementasikan _Pattern Interrupt_ visual dan _Accountability Protocol_ sebagai hambatan prosedural ( _friction_ ) berupa otorisasi pendamping saat interaksi menu pengaturan terdeteksi. 

# **3.2.4 Fase 4: Integrasi dan Pengujian Sistem (** **_System Hardening_ )** 

Fase 4 bertujuan memverifikasi performa seluruh komponen sistem menggunakan standar metrik yang terukur. Tim Pengusul mengevaluasi model AI menggunakan _Precision_ , _Recall_ , dan _F1-Score_ dengan fokus pada minimalisasi _False Positive Rate_ agar sistem tidak memblokir situs akademik atau pemerintah secara keliru. Tim Pengusul juga mengukur latensi pemblokiran dengan target di bawah 200ms dan _retention rate_ pengguna sebagai indikator awal keberhasilan intervensi psikologis, serta melakukan _stress testing_ terhadap upaya _kill process_ paksa untuk memastikan fitur _anti-uninstall_ berjalan konsisten. 

# **3.2.5 Fase 5: Finalisasi dan Pelaporan** 

Fase 5 bertujuan mendokumentasikan seluruh hasil program dan mendiseminasikan luaran kepada khalayak luas. Tim Pengusul menyusun Laporan Kemajuan, Laporan Akhir, serta dokumentasi teknis penggunaan aplikasi sebagai pertanggungjawaban pelaksanaan program. Selain luaran wajib, Tim Pengusul memproduksi video edukasi dan artikel ilmiah sebagai bentuk kontribusi akademik terhadap perkembangan riset di bidang keamanan digital dan intervensi psikologis berbasis teknologi 