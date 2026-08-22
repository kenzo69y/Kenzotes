# Openclose Admin Bot — Premium V3

Telegram admin bot siap Railway 24/7.

## Fitur utama
- `/panel` admin panel interaktif
- Warn permanen SQLite: `/warn`, `/warns`, `/unwarn`
- `/mute`, `/unmute`, `/kick`, `/ban`, `/unban`
- Anti-Link + whitelist domain
- Anti-Spam yang bisa dikonfigurasi
- Welcome / Goodbye custom
- `/purge`, `/pin`, `/unpin`
- `/stats` dan `/modlog`
- Settings per grup

## Deploy ke Railway
1. Buat project Railway dari repository ini.
2. Tambahkan variable `BOT_TOKEN` dengan token dari BotFather.
3. Tambahkan Railway Volume dengan mount path `/data` agar database SQLite permanen.
4. Railway membaca `railway.toml` dan menjalankan `python bootstrap.py`.
5. Pastikan bot versi lokal di PC dimatikan supaya tidak terjadi konflik `getUpdates`.

## Keamanan
File `.env` dan database lokal tidak disimpan di repository. Jangan pernah commit token bot ke GitHub.

## Catatan paket
Source V3 tersimpan sebagai package terkompresi yang dipecah di folder `package_parts/`. `bootstrap.py` menyatukan paket, mengekstraknya saat runtime, lalu menjalankan `OpencloseAdminBot/bot.py`. Ini menjaga paket V3 yang sudah diuji tetap identik saat dideploy.
