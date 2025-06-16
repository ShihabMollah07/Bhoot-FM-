class script(object):
    START_TXT = """<b><blockquote>ʜᴇʟʟᴏ {} 👋,</blockquote>
    
ɪ ᴀᴍ ʟᴀᴛᴇꜱᴛ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ. ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴇᴀʀɴ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏɴᴇʏ...💸</b>"""

    CLONE_START_TXT = """<b><blockquote>ʜᴇʟʟᴏ {}, ᴍʏ ɴᴀᴍᴇ <a href=https://t.me/{}>{}</a></blockquote>
    
ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇ ᴀɴᴅ ᴘᴏᴡᴇʀғᴜʟʟ ᴀᴜᴛᴏғɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴀᴍᴀᴢɪɴɢ ғᴇᴀᴛᴜʀᴇs. ᴊᴜsᴛ ᴛʏᴘᴇ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ, ᴛʜᴇɴ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ. 💘</b>"""
    
    HELP_TXT = """<b>ʜᴇʟʟᴏ {}
ʜᴇʀᴇ ɪs ᴀʟʟ ᴍʏ ᴜsᴇғᴜʟʟ ғᴇᴀᴛᴜʀᴇs.</b>"""

    ABOUT_TXT = """<b><blockquote>⍟───[ ᴍʏ ᴅᴇᴛᴀɪʟꜱ ]───⍟</blockquote>
    
‣ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/{}>{}</a>
‣ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 
‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href={}>ᴏᴡɴᴇʀ</a> 
‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> 
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/'>ᴘʏᴛʜᴏɴ 3</a> 
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a> 
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]</b>"""

    CLONE_ABOUT_TXT = """<b><blockquote>⍟───[ ᴍʏ ᴀʙᴏᴜᴛ ]───⍟</blockquote>
    
‣ ᴍʏ ɴᴀᴍᴇ : {}
‣ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 
‣ ᴄʟᴏɴᴇᴅ ғʀᴏᴍ : <a href=https://t.me/{}>{}</a>
‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> 
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/'>ᴘʏᴛʜᴏɴ 3</a> 
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]</b>"""

    CLONE_TXT = """<b>🌟 <u>CLONE MODE</u>

- Yᴏᴜ Cᴀɴ Cʀᴇᴀᴛᴇ Yᴏᴜʀ Oᴡɴ Cʟᴏɴᴇ Bᴏᴛ Bʏ /clone Cᴏᴍᴍᴀɴᴅ.
- Yᴏᴜ Cᴀɴ Bʀᴏᴀᴅᴄᴀsᴛ Iɴ Yᴏᴜʀ Cʟᴏɴᴇ Bᴏᴛs.
- Mɪʟʟɪᴏɴs Oғ Fɪʟᴇs Aʀᴇ Aʟʀᴇᴀᴅʏ Iɴᴅᴇxᴇᴅ, Nᴏ Nᴇᴇᴅ Tᴏ Aᴅᴅ Aɴʏ Fɪʟᴇ.

👨‍💻 Cᴏᴍᴍᴀɴᴅ : /clone</b>"""

    SUBSCRIPTION_TXT = """
<b>ʀᴇғᴇʀʀᴀʟ ʟɪɴᴋ - https://telegram.me/{}?start=ref-{}

ɪғ {} ᴜɴɪǫᴜᴇ ᴜsᴇʀs sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜ ʏᴏᴜʀ ʀᴇғᴇʀᴀʟ ʟɪɴᴋ, ʏᴏᴜ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ɢᴇᴛ ᴀ ғʀᴇᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ ғᴏʀ {}.

ʙᴜʏ ᴀ ᴘᴀɪᴅ ᴘʟᴀɴ ʙʏ ᴛʏᴘɪɴɢ - /plan</b>"""

    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡʜᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ, ᴀɴᴅ ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴛʜᴀᴛ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ.
<b>ɴᴏᴛᴇ:</b>
1. Tʜᴇ ʙᴏᴛ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇs.
2. Oɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. Aʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴀʟʟ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    BUTTON_TXT = """ʜᴇʟᴘ: <b>ʙᴜᴛᴛᴏɴꜱ</b>
- ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.
<b>ɴᴏᴛᴇ:</b>
1. Tᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴄᴏɴᴛᴇɴᴛ; ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. Tʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ Tᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. Bᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ɪɴ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ.
<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ (ᴇxᴀᴍᴘʟᴇ):</b>
<code>[Button Text](buttonurl:https://telegram.org/)</code>
<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ (ᴇxᴀᴍᴘʟᴇ):</b>
<code>[Button Text](buttonalert:This is an alert message!)</code>"""

    AUTOFILTER_TXT = """ʜᴇʟᴘ: <b>ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ</b>
<b>ɴᴏᴛᴇ: Fɪʟᴇ Iɴᴅᴇxɪɴɢ</b>
1. Mᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
2. Mᴀᴋᴇ ꜱᴜʀᴇ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ, ᴏʀ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
3. Fᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ Qᴜᴏᴛᴇꜱ. I'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ.

<b>Nᴏᴛᴇ: AᴜᴛᴏFɪʟᴛᴇʀ Sᴇᴛᴜᴘ</b>
1. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
2. Usᴇ /connect ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
3. Usᴇ /settings ɪɴ ᴛʜᴇ ʙᴏᴛ's PM ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ɪɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    CONNECTION_TXT = """ʜᴇʟᴘ: <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>
- Usᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ PM ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ.
- Iᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.
<b>ɴᴏᴛᴇ:</b>
1. Oɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. Sᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ.
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /connect  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ</code>
• /disconnect  - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""

    EXTRAMOD_TXT = """ʜᴇʟᴘ: Exᴛʀᴀ Mᴏᴅᴜʟᴇs
<b>ɴᴏᴛᴇ:</b>
 <b>✯ Maintained by : <a href={}>Owner</a></b>
 <b>✯ Join here : <a href={}>Update Channel</a></b> 
  
 • /id - <code>ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.</code> 
 • /info  - <code>ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.</code> 
 • /song - Download any song [<code>e.g., /song song name</code>] 
 • /telegraph - <code>Upload photo/video under 5MB to get a Telegraph link.</code> 
 • /tts - <code>Convert text to voice.</code> 
 • /video - Download any YouTube video [<code>e.g., /video youtube_link</code>]
 • /font - Generate stylish fonts [<code>e.g., /font hello</code>]"""

    ADMIN_TXT = """ʜᴇʟᴘ: Aᴅᴍɪɴ Mᴏᴅs
<b>ɴᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs.
Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ (usable by anyone)</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ᴀ ʟɪꜱᴛ ᴏꜰ ᴜꜱᴇʀꜱ</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ᴀ ʟɪꜱᴛ ᴏꜰ ᴄʜᴀᴛꜱ</code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ᴀ ᴄʜᴀᴛ</code>
• /disable  -  <code>ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ᴀ ʟɪꜱᴛ ᴏꜰ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>
• /grp_broadcast - <code>Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs</code>
• /gfilter - <code>ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /gfilters - <code>ᴛᴏ ᴠɪᴇᴡ ᴛʜᴇ ʟɪsᴛ ᴏғ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /request - <code>Tᴏ sᴇɴᴅ ᴀ Mᴏᴠɪᴇ/Sᴇʀɪᴇs ʀᴇǫᴜᴇsᴛ (usable by anyone in the support group)</code>
• /delallg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /deletefiles - <code>Tᴏ ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ/PʀᴇDVD ғɪʟᴇs</code>"""

    SEC_STATUS_TXT = """<b>★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code></b>"""
    
    STATUS_TXT = """<b>Total Files From All DBs: <code>{}</code>

USERS DB:
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>

FILE DB 1:
★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>

FILE DB 2:
★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>

OTHER DB:
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code></b>"""
    
    LOG_TEXT_G = """#NewGroup
Gʀᴏᴜᴘ: {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs: <code>{}</code>
Aᴅᴅᴇᴅ Bʏ: {}"""

    LOG_TEXT_P = """#NewUser
ID: <code>{}</code>
Nᴀᴍᴇ: {}"""

    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ. Pʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ ᴏᴡɴ ʀᴇǫᴜᴇsᴛ."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ. Pʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""

    CUDNT_FND = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    I_CUDNT = """<b>Sᴏʀʀʏ, ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ: {} 😕

Pʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ.

Movie Request Format:
Example: Uncharted or Uncharted 2022

Series Request Format:
Example: Loki S01 or Loki S01E04

🚯 ᴅᴏɴ'ᴛ ᴜꜱᴇ ➠ ':(!,./)</b>"""

    I_CUD_NT = """ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
Pʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ Gᴏᴏɢʟᴇ ᴏʀ IMDb."""

    MVE_NT_FND = """ᴍᴏᴠɪᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ..."""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ ғᴏʀ ᴍᴏᴠɪᴇ ɪɴ ᴅᴀᴛᴀʙᴀsᴇ..."""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""

    SHORTLINK_INFO = """Select your language and get started! 💰"""

    REQINFO = """⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠
ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀꜰᴛᴇʀ 5 ᴍɪɴᴜᴛᴇꜱ.
ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ғɪʟᴇ, ᴄʜᴇᴄᴋ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ."""

    SELECT = """sᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘʀᴇғᴇʀʀᴇᴅ ʟᴀɴɢᴜᴀɢᴇ, ǫᴜᴀʟɪᴛʏ, sᴇᴀsᴏɴ, ᴀɴᴅ ᴇᴘɪsᴏᴅᴇ."""

    SINFO = """🫣 For the movie, please join first, then click the 'Try Again' button. 😅"""

    NORSLTS = """★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★
𝗜𝗗: <b>{}</b>
𝗡𝗮𝗺𝗲: <b>{}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲: <b>{}</b>"""

    CAPTION = """<b>📂 ғɪʟᴇɴᴀᴍᴇ: {file_name}
⚙️ sɪᴢᴇ: {file_size}</b>""" 

    IMDB_TEMPLATE_TXT = """
<b>Query: {qurey}

IMDb Data:

<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings)
☀️ Languages: <code>{languages}</code>
📀 RunTime: {runtime} Minutes
📆 Release Info: {release_date}
🎛 Countries: <code>{countries}</code>

⏰ Result shown in: {remaining_seconds} <i>seconds</i> 🔥
Requested by: {message.from_user.mention}</b>"""
    
    ALL_FILTERS = """<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ғɪʟᴛᴇʀ ᴛʏᴘᴇs.</b>"""
    
    GFILTER_TXT = """<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴀɴᴅ ᴡᴏʀᴋ ɪɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ</code>"""
    
    FILE_STORE_TXT = """<b>Fɪʟᴇ sᴛᴏʀᴇ ᴄʀᴇᴀᴛᴇs ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ғᴏʀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ ʟɪɴᴋ</code>
• /pbatch - <code>Sᴀᴍᴇ ᴀs /batch, ʙᴜᴛ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs</code>
• /plink - <code>Sᴀᴍᴇ ᴀs /link, ʙᴜᴛ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ</code>"""

    SONG_TXT = """<b>ꜱᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ</b>
<b>Usᴇ ᴛʜɪꜱ ғᴇᴀᴛᴜʀᴇ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴy ꜱᴏɴɢ ᴡɪᴛʜ sᴜᴘᴇʀ-ғᴀꜱᴛ sᴘᴇᴇᴅ.</b>
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> 𝄟⃝ /song [song name]</b>""" 
  
    YTDL_TXT = """<b>Hᴇʟᴘs ʏᴏᴜ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏs ꜰʀᴏᴍ YᴏᴜTᴜʙᴇ.</b>
<b>Usᴀɢᴇ:</b> ᴛyᴩᴇ /video or /mp4 ғᴏʟʟᴏᴡᴇᴅ ʙʏ ᴛʜᴇ YᴏᴜTᴜʙᴇ ʟɪɴᴋ.
<b>ᴇxᴀᴍᴩʟᴇ:</b> <code>/mp4 https://youtu.be/example...</code>""" 
  
    TTS_TXT = """<b>ᴛᴛꜱ 🎤 ᴍᴏᴅᴜʟᴇ: ᴛʀᴀɴꜱʟᴀᴛᴇ ᴛᴇxᴛ ᴛᴏ ꜱᴩᴇᴇᴄʜ</b>
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /tts [text]""" 
  
    GTRANS_TXT = """<b>ʜᴇʟᴩ: Gᴏᴏɢʟᴇ ᴛʀᴀɴꜱʟᴀᴛᴇʀ</b>
Tʀᴀɴꜱʟᴀᴛᴇ ᴛᴇxᴛ ᴛᴏ ᴀɴy ʟᴀɴɢᴜᴀɢᴇ.
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /tr [language code]
<b>ɴᴏᴛᴇ:</b> Rᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ.
<b>ᴇxᴀᴍᴩʟᴇ:</b> /tr ml
 • en = English
 • ml = Malayalam
 • hi = Hindi""" 
  
    TELE_TXT = """<b>ʜᴇʟᴘ: ᴛᴇʟᴇɢʀᴀᴘʜ</b>
<b>ᴜꜱᴀɢᴇ:</b> /telegraph
Rᴇᴘʟʏ ᴛᴏ ᴀ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ (ᴜɴᴅᴇʀ 5MB) ᴛᴏ ɢᴇᴛ ᴀ Tᴇʟᴇɢʀᴀ.ph ʟɪɴᴋ.""" 
  
    CORONA_TXT = """<b>ʜᴇʟᴩ: ᴄᴏᴠɪᴅ</b>
Gᴇᴛ ᴅᴀɪʟy ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ Cᴏᴠɪᴅ-19.
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /covid [country name]
<b>ᴇxᴀᴍᴩʟᴇ:</b> <code>/covid India</code>
⚠️ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ᴍᴀʏ ɴᴏ ʟᴏɴɢᴇʀ ʙᴇ ᴀᴄᴛɪᴠᴇ.</b>""" 

    PROGRESS_BAR = """
╭━━━━❰ Renaming File... ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """
  
    ABOOK_TXT = """<b>ʜᴇʟᴩ: ᴀᴜᴅɪᴏʙᴏᴏᴋ</b>
Cᴏɴᴠᴇʀᴛ ᴀ PDF ғɪʟᴇ ᴛᴏ ᴀɴ ᴀᴜᴅɪᴏ ғɪʟᴇ.
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /audiobook
Rᴇᴘʟʏ ᴛᴏ ᴀ PDF ғɪʟᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴇ ᴀᴜᴅɪᴏ.</b>""" 
  
    PINGS_TXT = """<b>Pɪɴɢ Tᴇꜱᴛɪɴɢ</b>
<b>ᴄᴏᴍᴍᴀɴᴅꜱ:</b>
 • /alive - Cʜᴇᴄᴋ ɪғ ᴛʜᴇ ʙᴏᴛ ɪs ᴏɴʟɪɴᴇ.
 • /help - Gᴇᴛ ʜᴇʟᴘ.
 • /ping - Cʜᴇᴄᴋ ᴛʜᴇ ʙᴏᴛ's ʟᴀᴛᴇɴᴄʏ.</b>""" 
  
    STICKER_TXT = """<b>Fɪɴᴅ ᴀ sᴛɪᴄᴋᴇʀ's ID.</b>
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /stickerid
Rᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴛᴏ ɢᴇᴛ ɪᴛs ID.</b>""" 
  
    FONT_TXT = """<b>Usᴀɢᴇ:</b>
Cʜᴀɴɢᴇ ᴛʜᴇ ғᴏɴᴛ sᴛyʟᴇ ᴏғ ʏᴏᴜʀ ᴛᴇxᴛ.
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /font [your text]
<b>ᴇxᴀᴍᴩʟᴇ:</b> /font hello""" 
  
    PURGE_TXT = """<b>Pᴜʀɢᴇ</b>
Dᴇʟᴇᴛᴇ ᴍᴜʟᴛɪᴘʟᴇ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ɢʀᴏᴜᴘs (for admins).
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /purge
Rᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ᴛʜᴀᴛ ᴘᴏɪɴᴛ.""" 
  
    WHOIS_TXT = """<b>ᴡʜᴏɪꜱ ᴍᴏᴅᴜʟᴇ</b>
Gᴇᴛ ᴅᴇᴛᴀɪʟᴇᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /whois [user id or username or reply]""" 
  
    JSON_TXT = """<b>ᴊsᴏɴ:</b>
Gᴇᴛ ᴛʜᴇ JSON ᴅᴀᴛᴀ ᴏғ ᴀ ᴍᴇssᴀɢᴇ.
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /json
Rᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ.""" 
  
    URLSHORT_TXT = """<b>ʜᴇʟᴩ: ᴜʀʟ ꜱʜᴏʀᴛɴᴇʀ</b>
Sʜᴏʀᴛᴇɴ ᴀ ʟᴏɴɢ URL.
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /short [your link]
<b>ᴇxᴀᴍᴩʟᴇ:</b> <code>/short https://example.com/very/long/link</code>""" 
  
    CARB_TXT = """<b>ʜᴇʟᴩ: ᴄᴀʀʙᴏɴ</b>
Cʀᴇᴀᴛᴇ ᴀ sᴛʏʟɪᴢᴇᴅ ɪᴍᴀɢᴇ ᴏғ ʏᴏᴜʀ ᴛᴇxᴛ.
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /carbon
Rᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ.""" 

    GEN_PASS = """<b>Hᴇʟᴘ: Pᴀꜱꜱᴡᴏʀᴅ Gᴇɴᴇʀᴀᴛᴏʀ</b>
Gᴇɴᴇʀᴀᴛᴇ ᴀ sᴇᴄᴜʀᴇ ᴘᴀssᴡᴏʀᴅ.
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /genpassword [length]
<b>ᴇxᴀᴍᴩʟᴇ:</b> /genpassword 16
<b>ɴᴏᴛᴇ:</b> Mᴀxɪᴍᴜᴍ ʟᴇɴɢᴛʜ ɪs 84.""" 
  
    SHARE_TXT = """<b>Gᴇᴛ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ғᴏʀ ʏᴏᴜʀ ᴛᴇxᴛ.</b>
<b>ᴄᴏᴍᴍᴀɴᴅ:</b> /share
Rᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ.""" 
  
    PIN_TXT = """<b>Pɪɴ Mᴏᴅᴜʟᴇ</b>
Mᴀɴᴀɢᴇ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ (for admins).
<b>ᴄᴏᴍᴍᴀɴᴅꜱ:</b>
 • /pin: Rᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘɪɴ ɪᴛ.
 • /unpin: Uɴᴘɪɴ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛʟʏ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ."""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ!</b>
📅 Dᴀᴛᴇ: <code>{}</code>
⏰ Tɪᴍᴇ: <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ: <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code>"""

    LOGO = """
BOT IS STARTING...
██████╗  ██████╗ ████████╗
██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝██║   ██║   ██║   
██╔══██╗██║   ██║   ██║   
██████╔╝╚██████╔╝   ██║   
╚═════╝  ╚═════╝    ╚═╝ 
"""
 
    TAMIL_INFO = """
வணக்கம் <a href='tg://settings'>நண்பரே</a>,

இந்த பாட் மூலம் நீங்கள் பணம் சம்பாதிக்கலாம். உங்கள் குழுவில் இந்த ஃபில்டர் பாட்-ஐ நிர்வாகியாக சேர்த்து, உங்கள் ஷார்ட்னர் இணையதளம் மற்றும் API-ஐ இணைக்கவும்.

வழிமுறை:
1. இந்த ஃபில்டர் பாட்டை உங்கள் குழுவில் நிர்வாகியாக்குங்கள்.
2. உங்கள் ஷார்ட்னர் விவரங்களைச் சேர்க்கவும்: `/shortlink your_domain your_api`
3. பயிற்சி வீடியோவைச் சேர்க்க: `/set_tutorial [video_link]`
"""

    ENGLISH_INFO = """
Hey <a href='tg://settings'>my friend</a>,

You can earn money with this bot. Just make this filter bot an admin in your group and add your shortener website and API.

Instructions:
1. Make this filter bot an admin in your group.
2. Add your shortener details: `/shortlink your_domain your_api`
3. To set a tutorial video: `/set_tutorial [video_link]`
"""

    TELUGU_INFO = """
హలో <a href='tg://settings'>మిత్రమా</a>,

మీరు ఈ బాట్‌తో డబ్బు సంపాదించవచ్చు. మీ గుంపులో ఈ ఫిల్టర్ బాట్‌ను అడ్మిన్‌గా చేసి, మీ షార్ట్‌నర్ వెబ్‌సైట్ మరియు APIని జోడించండి.

సూచనలు:
1. మీ గుంపులో ఈ ఫిల్టర్ బాట్‌ను అడ్మిన్‌గా చేయండి.
2. మీ షార్ట్‌నర్ వివరాలను జోడించండి: `/shortlink your_domain your_api`
3. ట్యుటోరియల్ వీడియోను సెట్ చేయడానికి: `/set_tutorial [video_link]`
"""

    HINDI_INFO = """
नमस्ते <a href='tg://settings'>दोस्त</a>,

आप इस बॉट से पैसे कमा सकते हैं। बस इस फ़िल्टर बॉट को अपने ग्रुप में एडमिन बनाएं और अपनी शॉर्टनर वेबसाइट और एपीआई जोड़ें।

निर्देश:
1. इस फ़िल्टर बॉट को अपने ग्रुप में एडमिन बनाएं।
2. अपने शॉर्टनर विवरण जोड़ें: `/shortlink your_domain your_api`
3. ट्यूटोरियल वीडियो सेट करने के लिए: `/set_tutorial [video_link]`
"""

    MALAYALAM_INFO = """
ഹായ് <a href='tg://settings'>സുഹൃത്തേ</a>,

ഈ ബോട്ട് ഉപയോഗിച്ച് നിങ്ങൾക്ക് പണം സമ്പാദിക്കാം. നിങ്ങളുടെ ഗ്രൂപ്പിൽ ഈ ഫിൽട്ടർ ബോട്ടിനെ അഡ്മിൻ ആക്കി നിങ്ങളുടെ ഷോർട്ട്നർ വെബ്സൈറ്റും API-യും ചേർക്കുക.

നിർദ്ദേശങ്ങൾ:
1. ഈ ഫിൽട്ടർ ബോട്ടിനെ നിങ്ങളുടെ ഗ്രൂപ്പിൽ അഡ്മിൻ ആക്കുക.
2. നിങ്ങളുടെ ഷോർട്ട്നർ വിശദാംശങ്ങൾ ചേർക്കുക: `/shortlink your_domain your_api`
3. ഒരു ട്യൂട്ടോറിയൽ വീഡിയോ സജ്ജമാക്കാൻ: `/set_tutorial [video_link]`
"""

    # Other languages are similarly made generic.

    RENAME_TXT = """
🌌 <b><u>HOW TO SET THUMBNAIL</u></b>
• /set_thumb - Reply to an image to set it as a thumbnail.
• /del_thumb - Delete your current thumbnail.
• /view_thumb - View your current thumbnail.

📑 <b><u>HOW TO SET CUSTOM CAPTION</u></b>
• /set_caption - Set a custom caption.
• /see_caption - View your custom caption.
• /del_caption - Delete your custom caption.
Example: `/set_caption 📕 File Name: {filename}\n💾 Size: {filesize}`

✏️ <b><u>HOW TO RENAME A FILE</u></b>
• /rename - Reply to a file and type the new file name.
"""

    STREAM_TXT = """<b><u>HOW TO GET STREAM AND DOWNLOAD LINK:</u>
/stream - Reply to a file to get streamable and downloadable links.</b>"""
