# KENZO ADMIN BOT — Premium V4

Telegram admin bot production-ready untuk Railway 24/7.

## V4 Production Hardening

- Owner lock: pengaturan sensitif hanya bisa diubah oleh creator/pemilik grup.
- `/status`: uptime, environment, database, persistent volume, error count.
- `/version`: versi bot, Python, dan python-telegram-bot.
- `/audit`: 20 audit log terakhir dengan ID actor/target.
- `/backup`: snapshot database SQLite untuk global owner.
- Global error handler lebih kuat dan dapat mengirim alert ke owner bot.
- Perubahan setting penting dicatat ke audit log.
- Warn, mute, ban, anti-link, anti-spam, welcome, whitelist, panel admin tetap tersedia.

## Railway Variables

Wajib:

```text
BOT_TOKEN=TOKEN_DARI_BOTFATHER
```

Disarankan untuk V4:

```text
BOT_OWNER_ID=USER_ID_KAMU
```

Gunakan `/id` di Telegram untuk melihat User ID. `BOT_OWNER_ID` diperlukan untuk `/backup` dan notifikasi error owner.

## Persistent Database

Attach Railway Volume ke service dengan mount path:

```text
/data
```

Bot otomatis menggunakan `/data/bot_data.db` melalui `RAILWAY_VOLUME_MOUNT_PATH`.

## Tes Setelah Deploy

```text
/version
/status
/panel
/audit
```

Jangan menjalankan bot lokal dan Railway pada waktu yang sama karena Telegram polling hanya boleh memiliki satu instance aktif untuk token yang sama.
