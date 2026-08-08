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
   dll).
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
