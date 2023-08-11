class TEXT:
    DASAR = """
**Perintah Dasar**

👮🏻 Tersedia untuk Admin & Moderator
🕵🏻 Tersedia untuk Admin

👮🏻 `/reload` memperbaru daftar Admin dan hak istimewanya

🕵🏻 `/settings` anda dapat mengelola semua pengaturan Bot di grup

🕵🏻 `/ban` anda dapat memblokir pengguna dari grup tanpa memberinya kemungkinan untuk bergabung kembali menggunakan tautan grup

👮🏻 `/mute` menempatkan pengguna dalam mode hanya-membaca. Dia bisa membaca tetapi tidak bisa mengirim pesan apapun

👮🏻 `/kick` menendang pengguna dari grup, memberinya kemungkinan untuk bergabung kembali menggunakan tautan grup

👮🏻 `/unban` menghapus blokiran pengguna dari grup dalam daftar blokiran, memberinya kemungkinan untuk bergabung kembali dengan tautan grup

👮🏻 `/info` memberikan informasi tentang pengguna

◽️ `/staff` memberikan Daftar lengkap Staf grup
"""

    LANJUT = """
**Perintah Lanjutan**

🕵🏻 Tersedia untuk Admin
👮🏻 Tersedia untuk Admin & Moderator
🛃 Tersedia untuk Admin & Pembersih Obrolan

**MANAJEMEN PERINGATAN**
👮🏻 `/warn` memberikan peringatan ke pengguna
👮🏻 `/resetwarn` menghapus 
👮🏻 `/warnlist` memungkinkan anda melihat dan mengelola peringatan pengguna
🕵🏻 `/dwarn` menghapus pesan dan memberikan peringatan ke pengguna

🛃 `/del` menghapus pesan yang dipilih
🛃 `/purge` sama seperti `/del` lebih efisien

◽️ `/report` atau @admin melaporkan pengguna ke admin
"""

    AHLI = """
**Perintah Ahli**

👥 Tersedia untuk semua pengguna
👮🏻 Tersedia untuk Admin & Moderator
🕵🏻 Tersedia untuk Admin

👥 `/admins` melihat daftar admin
👮🏻 `/admincache` memulai ulang cache admin

**Pesan Tersemat**
🕵🏻 `/pin` menyematkan pesan dengan membalas ke pesan.
🕵🏻 `/unpin` menghapus pesan sematan.
👥 `/pinned` melihat daftar pin yang ada di group
"""

    PRO = """
**Perintah pro**

👥 Tersedia untuk semua pengguna
👮🏻 Tersedia untuk admin & moderator
🕵🏻 Tersedia untuk admin

**Rules Group**
👥 `/rules` melihat rules group
👮🏻 `/setrules` pasang rules digroup
👮🏻 `/clearrules` menghapus rules

**Note group**
👮🏻 `/notes` melihat notes digroup
👮🏻 `/save [note name]` menyimpan note
👮🏻 `/get [note name]` menampilkan note
👮🏻 `/clear [note name]` hapus note name
👮🏻 `/removeallnotes` hapus semua notes
"""

    MUSIC = "♬ ʙᴀɴᴛᴜᴀɴ ᴘᴇʀɪɴᴛᴀʜ ᴍᴜꜱɪᴄ.\nᴘɪʟɪʜ ᴍᴇɴᴜ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ʙᴀɴᴛᴜᴀɴ ᴍᴜꜱɪᴄ."
    ADMIN = """
**✮ PERINTAH ADMIN.**

c singkatan dari pemutaran Channel
 ➣ /pause or /cpause - Jeda musik yang diputar.
 ➣ /resume or /cresume- Lanjutkan musik yang dijeda.
 ➣ /mute or /cmute- Matikan musik yang diputar.
 ➣ /unmute or /cunmute- Suarakan musik yang dibisukan.
 ➣ /skip or /cskip- Lewati musik yang sedang diputar.
 ➣ /musicstop or /cstop- Hentikan pemutaran musik.
 ➣ /shuffle or /cshuffle- Secara acak mengacak daftar putar yang antri.
 ➣ /seek or /cseek - Teruskan Cari musik sesuai durasi Anda.
 ➣ /seekback or /cseekback - Mundur Carilah musik sesuai durasi Anda.

**༊Lewati.**
 ➣ /skip or /cskip contoh 3 
 ➣ Melewati musik ke nomor antrian yang ditentukan. Contoh: /skip 3 akan melewatkan musik ke musik antrian ketiga dan akan mengabaikan musik 1 dan 2 dalam antrian.

**༊Loop.**
 ➣ /loop or /cloop [enable/disable] atau [Angka antara 1-10]
 ➣ Saat diaktifkan, bot memutar musik yang sedang diputar menjadi 1-10 kali pada obrolan suara. Default ke 10 kali.

**༊Pengguna Auth.**
Pengguna Auth dapat menggunakan perintah admin tanpa hak admin di Group Anda.
 ➣ /auth [Username] - Tambahkan pengguna ke AUTH LIST dari grup.
 ➣ /unauth [Username] - Hapus pengguna dari AUTH LIST grup.
 ➣ /authusers - Periksa DAFTAR AUTH grup
    """
    BOT = """
**✮ PERINTAH BOT**

 ➣ /mstats - Dapatkan 10 Trek Global Stats Teratas, 10 Pengguna Bot Teratas, 10 Obrolan Teratas di bot, 10 Teratas Dimainkan dalam obrolan, dll.

 ➣ /msudolist - Periksa Sudo Pengguna Music,

 ➣ /lyrics [Nama Musik] mencari Lirik untuk Musik tertentu di web.

 ➣ /song [Nama Trek] atau [Tautan YT] - Unduh trek apa pun dari youtube dalam format mp3 atau mp4.

 ➣ /player -  Dapatkan Panel Bermain interaktif.

 ➣ c singkatan dari pemutaran saluran.

 ➣ /queue or /cqueue- Periksa Daftar Antrian Musik
"""
    PLAY = """
**♬ PERINTAH PLAY.**
**༊Perintah Play.**

Perintah yang tersedia = play , vplay , cplay.

Perintah ForcePlay = playforce , vplayforce , cplayforce.

c singkatan dari pemutaran Channel.

v singkatan dari pemutaran video.
force singkatan dari force play.

 ➣ /play atau /vplay atau /cplay  - Bot akan mulai memainkan kueri yang Anda berikan di obrolan suara atau Streaming tautan langsung di obrolan suara.

 ➣ /playforce atau /vplayforce atau /cplayforce -  Force Play menghentikan trek yang sedang diputar pada obrolan suara dan mulai memutar trek yang dicari secara instan tanpa mengganggu/mengosongkan antrean.

 ➣ /channelplay [Nama pengguna atau id obrolan] atau [Disable] - Hubungkan saluran ke grup dan streaming musik di obrolan suara saluran dari grup Anda.

**༊Daftar Putar Server Bot.**
 ➣ /playlist  - Periksa Daftar Putar Tersimpan Anda Di Server.
 ➣ /deleteplaylist - Hapus semua musik yang disimpan di daftar putar Anda.
 ➣ /play  - Mulai mainkan Daftar Putar Tersimpan Anda dari Server
"""
