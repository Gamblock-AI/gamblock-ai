# Privacy and Security


Jika ada pertentangan antara dokumen ini dengan `pkm_proposal.md`, proposal PKM
adalah sumber mutlak.

## Apa yang dikatakan proposal

Proposal PKM (Bab 2.2.4) menyatakan:

> Dengan melakukan seluruh proses klasifikasi dan inferensi di perangkat
> pengguna, sistem tidak perlu mengirimkan data mentah ke server, sehingga
> risiko kebocoran data dapat diminimalkan.

Ini berarti:
- Klasifikasi dan inferensi AI dilakukan di perangkat pengguna (on-device).
- Data mentah browsing tidak dikirim ke server.

## Implikasi engineering

1. URL, DOM text, judul halaman, heading, anchor text, riwayat browsing, dan
   screenshot diproses secara lokal dan tidak dikirim ke backend, website, atau
   layanan pihak ketiga.
2. Yang boleh dikirim ke server hanyalah data non-browsing yang secara sukarela
   dimasukkan pengguna untuk fitur recovery (akun, partner, jurnal terenkripsi,
   dll), plus agregat proteksi dan metadata proteksi yang dihasilkan sistem
   (lihat poin 7-8).
3. Browser extension hanya bertindak sebagai sensor pasif berbasis loopback
   lokal. Extension tidak melakukan klasifikasi, blocking, atau redirect.
4. Blocking dan Pattern Interrupt dilakukan oleh Android/Windows client.
5. Anti-tamper hanya menggunakan mekanisme OS yang didukung (Accessibility
   Service di Android, LocalSystem + SCM recovery di Windows). Tidak menggunakan
   `RtlSetProcessIsCritical` atau mekanisme critical-process lainnya.
6. Pengingat harian opt-in: preferensi waktu + timezone dan endpoint Web Push
   (VAPID) adalah data pengiriman non-browsing yang dikirim pengguna secara
   sukarela. Notifikasi lokal di Android/Windows tetap on-device; tidak ada
   token FCM/APNs, dan pesan notifikasi tidak memuat data penjelajahan.
7. Timestamp peristiwa blokir adalah metadata proteksi yang dihasilkan sistem,
   bukan konten yang dikunjungi pengguna. Peristiwa blokir itu sendiri adalah
   sinyal sistem (situs terdeteksi sebagai judi dan diblokir); timestamp hanya
   mencatat kapan sinyal itu terjadi. Konsekuensinya, timestamps peristiwa
   blokir boleh dikirim dan disimpan di backend untuk mendukung deteksi pola
   jam rawan (SPK time-pattern). Data ini tetap tidak pernah memuat URL, domain,
   DOM, screenshot, atau isi halaman. Interpretasi ini disepakati eksplisit
   sebagai re-scope terbatas dari batas privasi; jangan melebarkannya ke data
   penjelajahan lain.
8. Personalisasi AI (LLM DeepSeek) bersifat default-on di tingkat pengguna,
   dengan kontrol privasi per-kategori yang jelas di halaman Pengaturan
   (`/settings`) dan gate operasional `SPK_LLM_ENRICHMENT` di server. Mahasiswa
   dapat mematikan rekomendasi SPK secara penuh, mematikan penggunaan kategori
   data tertentu (perlindungan / aktivitas pemulihan / konteks pribadi), atau
   mematikan personalisasi AI. Saat aktif, hanya hasil keputusan SPK (kategori
   intervensi, level dukungan, reason code) dan konteks yang dilaporkan sendiri
   pengguna (niat perubahan, dampak pendidikan/finansial, screen time, upaya
   berhenti) yang dikirim ke layanan LLM untuk menyusun pesan/penjelasan
   personal. Timestamps peristiwa blokir, URL, DOM, dan agregat halus tidak
   pernah dikirim ke LLM. Toggle hanya mengatur penggunaan data untuk
   rekomendasi/AI, bukan menghapus atau menghentikan penyimpanan data.
9. Public key perangkat dan RFC 7638 JWK thumbprint boleh dikirim ke backend
   hanya untuk mengikat grant approval ke native authority. Keduanya adalah
   metadata keamanan pseudonim dan tidak boleh berisi atau dikorelasikan dengan
   URL, domain, DOM, screenshot, riwayat browsing, maupun skor klasifikasi.
10. Grant approval harus ditandatangani backend, memiliki action allowlist dan
    expiry singkat, serta diverifikasi ulang oleh Android/Windows. Enkripsi
    Keystore/DPAPI melindungi penyimpanan lokal tetapi tidak menggantikan
    verifikasi keaslian grant.

## Interpretasi engineering (bukan dari proposal)

Semua poin di bawah adalah keputusan engineering, bukan persyaratan proposal:

- Klasifikasi data (D0-D6) adalah kategorisasi engineering untuk memudahkan
  desain sistem.
- Enkripsi AES-256-GCM untuk jurnal/refleksi adalah pilihan implementasi.
- Threat model dan abuse cases adalah analisis engineering tambahan.
- Aturan field rejection dan PrivacyGuard adalah implementasi defensif.
- Aturan logging, retensi, dan consent detail adalah keputusan operasional.

Poin-poin tersebut boleh berubah tanpa mengubah kepatuhan terhadap proposal,
selama prinsip "klasifikasi on-device, data mentah tidak ke server" tetap
terjaga.
