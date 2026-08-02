# Prosedur Kontinuitas Akses Media Sosial

Tujuan prosedur ini adalah menjaga akun luaran PKM tetap dapat diakses oleh tim
yang berwenang tanpa menyimpan credential di repository atau bergantung pada
satu perangkat/pribadi.

## Peran minimum

- **Account owner:** pemilik formal kanal dan keputusan perubahan admin.
- **Continuity owner:** pihak kedua yang dapat memulihkan akses sesuai mandat.
- **Publisher:** mengunggah konten yang sudah disetujui; tidak otomatis menjadi
  account owner.
- **Reviewer/archivist:** memeriksa klaim dan menyimpan metadata/hash; tidak
  memerlukan akses ke password atau DM.

Nama, nomor, email, backup code, dan credential dicatat pada penyimpanan privat
yang disetujui tim, bukan di Git, laporan publik, screenshot, atau chat umum.

## Baseline

1. Aktifkan 2FA dengan metode yang dapat dipulihkan tim.
2. Simpan password unik dan backup code di password manager tim yang disetujui.
3. Tetapkan dua pemilik akses berbeda dan hindari shared plaintext password.
4. Verifikasi email/nomor recovery serta tanggal uji pemulihan.
5. Inventarisasikan perangkat/sesi aktif dan keluarkan sesi lama setelah
   pergantian anggota.
6. Berikan publisher permission minimum bila platform mendukung role terpisah.
7. Catat perubahan ownership/admin sebagai audit metadata tanpa credential.

## Continuity drill

Dilakukan sebelum laporan akhir dan setiap pergantian personel:

1. account owner memastikan akses normal;
2. continuity owner menguji jalur pemulihan non-destruktif;
3. tim mengonfirmasi bahwa satu anggota keluar tidak menghilangkan akses;
4. 2FA/recovery code dirotasi bila drill atau pergantian menuntutnya;
5. ownership record diperbarui dengan tanggal, status lulus/gagal, dan reviewer;
6. kegagalan diperbaiki sebelum publikasi berikutnya.

## Insiden

- Bekukan publikasi bila akun diduga diambil alih.
- Gunakan recovery resmi platform; jangan meminta credential melalui kanal
  dukungan Gamblock-AI.
- Cabut sesi/perangkat yang tidak dikenal, rotasi password/2FA, dan review post.
- Arsipkan timeline insiden yang telah direduksi; jangan menyimpan token,
  recovery code, DM, atau data pribadi followers.
- Publikasikan koreksi bila konten tidak sah sempat terlihat.

## Handover akhir program

Account owner dan continuity owner meninjau tujuan retensi kanal, siapa yang
bertanggung jawab setelah PKM, kebijakan komentar/DM, jadwal review link, dan
prosedur penutupan jika kanal tidak lagi dipelihara. Akun tidak boleh dibiarkan
aktif tanpa pemilik yang dapat dihubungi atau diubah menjadi kanal pribadi.
