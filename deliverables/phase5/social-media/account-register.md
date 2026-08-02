# Register Kanal Media Sosial Gamblock-AI

Status: link dikonfigurasi pada production seeder; ownership, publication, dan
continuity harus diverifikasi oleh pemilik akun.

| Platform  | URL konfigurasi                                          | Status repository                                                  | Bukti yang belum tersedia                                     |
| --------- | -------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------- |
| Instagram | `https://www.instagram.com/gamblockai.pkmkc/`            | Diaktifkan oleh `site_social_link_seed.go` pada konfigurasi kosong | Login ownership, 2FA/recovery owner, publication archive      |
| Facebook  | `https://web.facebook.com/profile.php?id=61591544143202` | Diaktifkan oleh `site_social_link_seed.go` pada konfigurasi kosong | Page/admin ownership, 2FA/recovery owner, publication archive |
| TikTok    | `https://www.tiktok.com/@gamblockai.pkmkc`               | Diaktifkan oleh `site_social_link_seed.go` pada konfigurasi kosong | Login ownership, 2FA/recovery owner, publication archive      |

Website menampilkan hanya link non-null yang aktif dari endpoint publik.
Karena handle tidak sama pada semua platform, teks publik tidak boleh menyebut
satu handle generik. Gunakan frasa “tautan media sosial resmi pada footer” atau
nama platform + URL yang berasal dari konfigurasi.

## Prosedur verifikasi kepemilikan

1. Pemilik masuk ke kanal melalui perangkat resmi tanpa membagikan password.
2. Pemilik mencatat platform, URL kanonik, account/page ID, continuity owner,
   recovery channel yang telah diuji, status 2FA, dan tanggal verifikasi pada
   salinan privat `account-ownership.template.json`.
3. Reviewer membandingkan URL terhadap konfigurasi seeder/admin dan halaman
   publik.
4. Bukti publik yang aman dapat berupa post verifikasi atau metadata page;
   screenshot yang memuat email, nomor telepon, backup code, session, atau
   security setting tidak boleh masuk repository.
5. Record final di-hash dan direferensikan oleh evidence manifest Phase 5.
