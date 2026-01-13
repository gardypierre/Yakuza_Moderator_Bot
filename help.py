from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
import os

router = Router()

@router.message(Command("help"))
async def help_command(message: Message):
    photo_path = os.path.join(os.path.dirname(__file__), "assets", "help-img.jpg")
    photo = FSInputFile(photo_path)  # Assure-toi que l'image existe à ce chemin
    text = ("""➲ ʙᴇʟᴏᴡ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ʏᴀᴋᴜᴢᴀs:

━━━━━━━━ ᴍᴀɪɴ ━━━━━━━━
⎆ /start – Wᴇʟᴄᴏᴍᴇ Mᴇssᴀɢᴇ
⎆ /help – Cᴏᴍᴍᴀɴᴅs Lɪsᴛ
⎆ /alive – Bᴏᴛ Sᴛᴀᴛᴜs
⎆ /settings – Vɪᴇᴡ Bᴏᴛ Sᴇᴛᴛɪɴɢs
⎆ /profile - ᴛᴏ sᴇᴇ ʏᴏᴜʀ ɪɴғᴏ ɪɴ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ

━━━━━━━━ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ ━━━━━━━━
⎆ /ban /unban – Bᴀɴ ᴏʀ Uɴʙᴀɴ Mᴇᴍʙᴇʀ
⎆ /warn /clearwarn – Wᴀʀɴ Mᴇᴍʙᴇʀ
⎆ /mute /unmute – Mᴜᴛᴇ Mᴇᴍʙᴇʀ
⎆ /kick – Rᴇᴍᴏᴠᴇ Mᴇᴍʙᴇʀ
⎆ /setpp /delpp – Aᴅᴅ 
⎆ /stats - stats bot
            
━━━━━━━━ ʀᴏʟᴇᴘʟᴀʏ ━━━━━━━━
⎆ /setcode /honneur – Sᴇᴛ ᴏʀ Vɪᴇᴡ Yᴀᴋᴜᴢᴀ Cᴏᴅᴇ
⎆ /sethierarchie /hierarchie – Yᴀᴋᴜᴢᴀ Rᴀɴᴋs
⎆ /setmissions /missions – Aᴅᴅ / Sʜᴏᴡ Mɪssɪᴏɴs

━━━━━━━━ ғᴜɴ ━━━━━━━━
⎆ /hug /slap /kill – RP Fᴜɴ Aᴄᴛɪᴏɴs
⎆ /tagall /tagadmin – Tᴀɢ ᴍᴇᴍʙᴇʀs

━━━━━━━━━━━━━━━━━━━━""")
    await message.answer_photo(photo=photo, caption=text)
