# Panduan Instalasi dan Penggunaan Prototipe Gamblock-AI

Versi panduan: 1.0

Target: mahasiswa Universitas Teknologi Yogyakarta, pendamping, dan evaluator

Platform prototipe: Android dan Windows

Status rilis: prototipe code-complete; gunakan hanya artefak yang identitas,
checksum, dan status signing-nya tercatat pada release record

## 1. Sebelum memasang

Gamblock-AI adalah alat bantu kontrol diri dan pencegahan, bukan layanan klinis
atau jaminan bahwa seluruh konten judi akan terdeteksi. Perlindungan lokal saat
ini ditargetkan untuk:

- Android: Chrome dan Microsoft Edge yang dapat dibaca melalui Accessibility
  Service;
- Windows: Chrome dan Microsoft Edge dengan ekstensi Gamblock-AI serta service
  lokal;
- website: akun, psikoedukasi, regulasi diri, bantuan, dan pendampingan; website
  tidak melakukan klasifikasi atau pemblokiran real-time.

Sebelum instalasi, siapkan:

1. perangkat Android atau Windows uji yang dapat dipulihkan;
2. akun mahasiswa dengan email aktif;
3. orang tua/rekan sebaya yang bersedia menjadi pendamping;
4. koneksi internet untuk autentikasi dan sinkronisasi fitur akun—perlindungan
   lokal dan Pattern Interrupt dirancang tetap berjalan ketika koneksi terputus;
5. release record resmi yang menyebut versi, platform, URL, checksum SHA-256,
   konfigurasi API/site, status signing, dan status evaluasi.

Jangan memasang file yang diklaim sebagai production-signed apabila release
record menyebut debug, unsigned, atau `evaluated: false`.

## 2. Instalasi Android

### 2.1 Memasang artefak demo

1. Unduh APK dari release URL yang tercatat.
2. Bandingkan SHA-256 APK dengan release record menggunakan alat checksum
   perangkat/komputer yang tepercaya.
3. Aktifkan izin pemasangan dari sumber yang digunakan hanya untuk proses ini.
4. Pasang APK, lalu nonaktifkan kembali izin sumber tersebut bila tidak lagi
   diperlukan.
5. Buka Gamblock-AI dan selesaikan onboarding.

### 2.2 Mengaktifkan perlindungan

1. Masuk atau daftar sebagai mahasiswa.
2. Buka tugas **Siapkan perlindungan** pada Dashboard.
3. Baca disclosure Accessibility Service. Gamblock-AI menggunakan akses ini
   untuk membaca input yang didukung, mengambil keputusan lokal, menavigasi
   kembali, menampilkan Pattern Interrupt, dan memberi friksi pada pengaturan.
4. Buka pengaturan aksesibilitas Android dan aktifkan layanan Gamblock-AI.
5. Kembali ke aplikasi dan jalankan **Self-test**.
6. Pastikan status menunjukkan layanan aktif, artefak lokal valid, dan tidak
   ada permission yang perlu dipulihkan.

Gamblock-AI tidak mengunggah URL, domain, DOM, riwayat, screenshot, feature
vector, atau skor halaman. Bila disclosure pada artefak yang dipasang berbeda,
hentikan penggunaan dan laporkan ke tim.

## 3. Instalasi Windows

### 3.1 Memasang aplikasi dan service

1. Unduh bundle Windows dari release URL resmi dan verifikasi SHA-256.
2. Periksa status Authenticode pada release record. Unsigned/debug hanya boleh
   digunakan sebagai prototipe uji yang diberi label jelas.
3. Ekstrak bundle pada direktori uji yang stabil.
4. Jalankan `windows/scripts/install-service.ps1` sebagai Administrator dari
   bundle resmi. Skrip memasang `gamblock_ai_service.exe` dan mengaktifkan SCM
   recovery.
5. Jalankan aplikasi Gamblock-AI pada sesi pengguna biasa, bukan sebagai
   LocalSystem.
6. Masuk sebagai mahasiswa dan buka Settings untuk melihat health serta pairing.

### 3.2 Memasang ekstensi Chrome/Edge

Untuk paket demo yang telah disetujui, ikuti instruksi release record. Untuk
evaluasi unpacked:

1. Buka `chrome://extensions` atau `edge://extensions`.
2. Aktifkan **Developer mode**.
3. Pilih **Load unpacked** dan arahkan ke direktori ekstensi Gamblock-AI yang
   diverifikasi.
4. Buka halaman Options ekstensi.
5. Salin pairing token yang dihasilkan aplikasi desktop, tempel pada Options,
   lalu simpan.
6. Kembali ke aplikasi dan pastikan sensor lokal berstatus terhubung.

Pairing token hanya untuk koneksi WebSocket `127.0.0.1:9090`. Jangan mengirim
token kepada pendamping, admin, atau kanal dukungan.

## 4. Menambahkan pendamping

1. Buka menu **Partner/Pendamping**.
2. Pilih membuat atau bergabung pada grup sesuai alur yang tersedia.
3. Tinjau identitas dan tujuan hubungan sebelum mengonfirmasi.
4. Pendamping menerima undangan menggunakan akun mereka sendiri.
5. Mahasiswa meninjau dan menyimpan empat kategori agregat yang boleh dibagikan.
6. Pastikan status hubungan aktif sebelum menguji permintaan pelepasan.

Pendamping tidak memperoleh URL, riwayat, jurnal, mood, detail niat, isi misi
pribadi, atau rekonstruksi timeline. Mahasiswa dapat menggunakan unsafe exit
ketika hubungan tidak aman; emergency recovery tersedia sebagai jalur
operasional yang dibatasi dan diaudit.

## 5. Menggunakan perlindungan

### 5.1 Saat menjelajah

1. Gunakan browser yang didukung.
2. Sensor mengambil input terbatas dan menyerahkannya ke otoritas lokal.
3. Hybrid Analysis memproses aturan, fitur URL, dan teks DOM pada perangkat.
4. Jika keputusan positif, aplikasi native menjalankan tindakan blok dan
   Pattern Interrupt selama tujuh detik.
5. Setelah jeda, pilih grounding/help offline atau lanjutkan ke web pemulihan.

Handoff web hanya membawa locale dan kategori sumber tetap. Halaman yang
terdeteksi tidak ikut dikirim.

### 5.2 Bila terjadi false positive

1. Hentikan aktivitas yang terdampak dan catat versi aplikasi/model/rules dari
   Settings—jangan mencatat atau mengirim URL/domain pada kanal biasa.
2. Gunakan jalur bantuan/dukungan yang tersedia.
3. Ikuti instruksi redaksi; jangan lampirkan screenshot, DOM, history, token,
   password, atau data akademik sensitif.
4. Evaluator dataset hanya boleh menerima sampel melalui protokol riset
   terpisah yang memiliki consent, review, penyimpanan, dan penghapusan.

## 6. Menggunakan web pemulihan

- **Niat perubahan:** tuliskan arah dan langkah berikutnya; sinkronisasi akun
  bersifat opt-in sesuai pengaturan.
- **Check-in:** catat mood dan dorongan secara sadar; data ini bukan detail
  browsing dan tidak otomatis dibagikan kepada pendamping.
- **Edukasi:** pelajari kesadaran impuls dan respons adaptif.
- **Misi harian:** selesaikan langkah pengendalian diri yang kecil dan
  terukur; misi pribadi tetap privat.
- **Learning Hub:** pilih sumber belajar berdasarkan program studi, tujuan,
  tingkat, dan durasi; kursus/sertifikasi dilengkapi konteks manfaat serta
  aktivitas refleksi.
- **Evaluasi mingguan:** bandingkan tujuan, pemantauan, hasil, dan penyesuaian
  langkah berikutnya.
- **Bantuan:** gunakan kanal pendamping atau tim Gamblock-AI sesuai jenis
  dukungan dan hubungi layanan darurat/profesional ketika keselamatan terancam.

## 7. Analitik dan gamifikasi

Analitik native menampilkan agregat 7/30 hari, bukan timeline situs. Gamifikasi
website memberi EXP/level/badge pada tindakan pemulihan dan belajar yang
bermakna. Sistem tidak memberi hukuman, rasa malu, loot box, hadiah acak, atau
mekanisme yang menyerupai perjudian. EXP tidak menjadi bukti kesembuhan atau
efektivitas klinis.

## 8. Pengaturan, update, dan pelepasan

- Gunakan Settings untuk bahasa, haptics, health notification, pairing, versi
  artefak, privasi, bantuan, dan akun.
- Pasang pembaruan hanya dari release record resmi dan verifikasi checksum.
- Permintaan pelepasan perlindungan mengikuti state pending, approved, denied,
  expired, cancelled, atau emergency sesuai otoritas yang berlaku.
- Android sideloading tidak dapat menjadikan aplikasi mustahil dicopot;
  Gamblock-AI menambahkan friksi OS-supported, bukan device-owner tersembunyi.
- Windows menggunakan uninstall script resmi hanya setelah grant yang valid.
- Jika perangkat tidak dapat digunakan dengan aman, ikuti jalur emergency
  recovery dan dokumentasikan audit tanpa membocorkan browsing context.

## 9. Pemecahan masalah

| Gejala                           | Pemeriksaan aman                                                                                   |
| -------------------------------- | -------------------------------------------------------------------------------------------------- |
| Android tidak aktif              | Periksa Accessibility Service, battery restriction, browser yang didukung, lalu jalankan self-test |
| Windows sensor terputus          | Periksa service health, aplikasi sesi pengguna, ekstensi, dan pairing token lokal                  |
| Pattern Interrupt tidak terlihat | Catat versi/platform/skenario tanpa URL; jalankan self-test dan laporkan melalui dukungan          |
| Website tidak tersedia           | Gunakan grounding/help offline; perlindungan lokal tidak boleh dilemahkan                          |
| Artefak ditolak                  | Pertahankan last-known-good, periksa versi/manifest/checksum, jangan memaksa artefak korup         |
| Pendamping tidak tersedia        | Biarkan permintaan pada state yang transparan atau gunakan prosedur emergency yang diaudit         |
| Diduga false positive            | Gunakan alur redaksi pada §5.2; jangan mengirim halaman mentah ke backend                          |

## 10. Checklist evaluator

- [ ] Release record cocok dengan file dan SHA-256.
- [ ] Status signing/debug/production terlihat jelas.
- [ ] Android dan Windows dicatat pada device matrix yang disetujui.
- [ ] Browser, foreground/background, warm/cold, dan online/offline dicatat.
- [ ] Tidak ada URL/DOM/history/screenshot pada evidence output.
- [ ] Pattern Interrupt memiliki reduced-motion/non-visual alternative.
- [ ] Kill/recovery dijalankan hanya pada perangkat/VM yang dapat dipulihkan.
- [ ] Partner dan emergency state tidak menyebabkan lockout atau instability.
- [ ] Setiap temuan memiliki reviewer, tanggal, versi, limitation, dan hash.
