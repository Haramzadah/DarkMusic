import os
from VCPlayBot.config import SOURCE_CODE
from VCPlayBot.config import ASSISTANT_NAME
from VCPlayBot.config import PROJECT_NAME
from VCPlayBot.config import SUPPORT_GROUP
from VCPlayBot.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**salam bro 👋 [{}](tg://user?id={})!**\n\n💀 Saya adalah bot canggih yang dibuat untuk memutar musik di obrolan suara Grup & Saluran Telegram.\n\n✅ Send me /help for more info.\n\n Join @Update_Grouppp"
      HELP_MSG = [
        ".",
f"""
**Salam Bro 👋 Selamat datang kembali di {PROJECT_NAME}

⚪️ {PROJECT_NAME} dapat memutar musik di obrolan suara grup Anda serta obrolan suara saluran

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nKlik berikutnya untuk petunjuk**

""",

f"""
**Pengaturan**

1) Jadikan bot admin (Grup dan di saluran jika menggunakan cplay)
2) Mulai obrolan suara
3) Mencoba /play [nama lagu] pertama kali oleh admin
*) Jika userbot bergabung nikmati musik , Jika tidak tambahkan @{ASSISTANT_NAME} ke grup Anda dan coba lagi

**Untuk Putar Musik Saluran**
1) Jadikan saya admin saluran Anda
2) Kirim /userbotjoinchannel di grup tertaut
3) Sekarang kirim perintah di grup tertaut

""",
f"""
**Commands**

**=>> Memutar Lagu 🎧**

- /play: Memutar lagu yang diminta
- /play [yt url] : Memutar url yt yang diberikan
- /play [balas audio yo]: Putar audio yang dibalas
- /splay: Memutar lagu melalui jio saavn
- /ytplay: Memutar lagu secara langsung melalui Youtube Music

**=>> Pemutaran ⏯**

- /player: Buka menu Pengaturan pemain
- /skip: Melewati trek saat ini
- /jeda: Jeda trek
- /resume: Melanjutkan trek yang dijeda
- /end: ​​Menghentikan pemutaran media
- / saat ini: Menampilkan trek yang sedang diputar
- /playlist: Menampilkan daftar putar

*Player cmd dan semua cmd lainnya kecuali /play, /current  dan /playlist  hanya untuk admin grup.
""",

f"""
**=>> Putar Musik Saluran 🛠**

⚪️ Hanya untuk admin grup tertaut:

- /cplay [nama lagu] - putar lagu yang Anda minta
- /csplay [nama lagu] - putar lagu yang Anda minta melalui jio saavn
- /cplaylist - Tampilkan daftar yang sedang diputar
- /cccurrent - Tampilkan sedang diputar
- /cplayer - buka panel pengaturan pemutar musik
- /cpause - jeda pemutaran lagu
- /cresume - melanjutkan pemutaran lagu
- /cskip - putar lagu berikutnya
- /cend - hentikan pemutaran musik
- /userbotjoinchannel - undang asisten ke obrolan Anda

saluran juga dapat digunakan sebagai pengganti c ( /cplay = /channelplay )

⚪️ Jika Anda tidak suka bermain di grup tertaut:

1) Dapatkan ID saluran Anda.
2) Buat grup dengan judul: Channel Music: your_channel_id
3) Tambahkan bot sebagai admin Saluran dengan izin penuh
4) Tambahkan @{ASSISTANT_NAME} ke saluran sebagai admin.
5) Cukup kirim perintah di grup Anda. (ingat untuk menggunakan /ytplay sebagai gantinya /play)

""",

f"""
**=>> Lebih banyak alat 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
Join @Update_Grouppp
""",
f"""
**=>> Unduh Lagu🎶 **

- /video [lagu name]: Download video lagu dari youtube
- /song [nama lagu]: Unduh audio lagu dari youtube
- /saavn [nama lagu]: Unduh lagu dari saavn
- /deezer [nama lagu]: Unduh lagu dari deezer

**=>> Alat pencari 📄**

- /search [nama lagu]: Cari youtube untuk lagu
- /lyrics [nama lagu]: Dapatkan lirik lagu
""",

f"""
**=>> Perintah untuk Pengguna Sudo ✏️**

 - /userbotleaveall - hapus asisten dari semua obrolan
 - /broadcast <reply to message> - global brodcast membalas pesan ke semua obrolan
 - /pmpermit [on/off] - enable/disable pmpermit message
*Pengguna Sudo dapat menjalankan perintah apa pun di grup mana pun
"""
      ]
