from aiogram import Router, F
from aiogram.types import Message, ChatPermissions
from aiogram.filters import Command
from aiogram.types import BotCommand as CommandObject
from aiogram.exceptions import TelegramBadRequest

router = Router()
warns = {}

#⚠️ WARN
@router.message(Command("warn"))
async def warn_user(message: Message):
    if not message.reply_to_message:
        return await message.reply("⚠️ Réponds au message de l'utilisateur à avertir.")
    
    user_id = message.reply_to_message.from_user.id
    warns[user_id] = warns.get(user_id, 0) + 1
    count = warns[user_id]

    await message.reply(
        f"⚠️ Avertissement #{count} pour "
        f"<a href='tg://user?id={user_id}'>{message.reply_to_message.from_user.full_name}</a>.",
        parse_mode="HTML"
    )

    if count >= 3:
        try:
            await message.bot.ban_chat_member(message.chat.id, user_id)
            await message.reply("🚫 Utilisateur banni après 3 avertissements.")
            warns[user_id] = 0
        except:
            await message.reply("❌ Impossible de bannir l'utilisateur.")


# ============= Commandes clearwarn =============
@router.message(Command("clearwarn"))
async def clear_warns(message: Message):
    if not message.reply_to_message:
        return await message.reply("ℹ️ Réponds à l'utilisateur pour réinitialiser ses avertissements.")
    
    user_id = message.reply_to_message.from_user.id
    warns[user_id] = 0
    await message.reply(f"🧹 Avertissements effacés pour {message.reply_to_message.from_user.full_name}.")



# =============== Commandes ban && unban ===========
@router.message(Command("ban"))
async def ban_user(message: Message):
    if not message.reply_to_message:
        return await message.reply("Réponds au message de l'utilisateur à bannir.")
    try:
        await message.bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply("🔨 Utilisateur banni.")
    except:
        await message.reply("❌ Impossible de bannir l'utilisateur.")


@router.message(Command("unban"))
async def unban_user(message: Message):
    if not message.reply_to_message:
        return await message.reply("Réponds à l'utilisateur à débannir.")
    try:
        await message.bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply("♻️ Utilisateur débanni.")
    except:
        await message.reply("❌ Impossible de débannir.")


# ================= Mute && Unmute =================
@router.message(Command("mute"))
async def mute_user(message: Message):
    if not message.reply_to_message:
        return await message.reply("Réponds à l'utilisateur à mute.")
    try:
        await message.bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions={"can_send_messages": False}
        )
        await message.reply("🔇 Utilisateur réduit au silence.")
    except:
        await message.reply("❌ Impossible de mute.")

@router.message(Command("unmute"))
async def unmute_user(message: Message):
    if not message.reply_to_message:
        return await message.reply("Réponds à l'utilisateur à unmute.")
    try:
        await message.bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=ChatPermissions(can_send_messages=True)
        )
        await message.reply("🔊 Utilisateur peut de nouveau parler.")
    except:
        await message.reply("❌ Impossible de unmute.")


# ------------- Kick ----------
@router.message(F.text.startswith("/kick"))
async def kick_user(message: Message):
    if not message.reply_to_message:
        return await message.reply("🚫 ʀᴇ́ᴘᴏɴᴅs ᴀᴜ ᴍᴇssᴀɢᴇ ᴅᴇ ʟ'ᴜᴛɪʟɪsᴀᴛᴇᴜʀ ᴀ ᴇxᴘᴜʟsᴇʀ.")
    
    user_id = message.reply_to_message.from_user.id
    try:
        await message.bot.ban_chat_member(chat_id=message.chat.id, user_id=user_id)
        await message.bot.unban_chat_member(chat_id=message.chat.id, user_id=user_id)
        await message.reply(f"👢 <a href='tg://user?id={user_id}'>{message.reply_to_message.from_user.full_name}</a> ᴀ éᴛé ᴇxᴘᴜʟsᴇ́ ᴅᴜ ɢʀᴏᴜᴘᴇ.")
    except TelegramBadRequest:
        await message.reply("❌ ɪᴍᴘᴏssɪʙʟᴇ ᴅ'ᴇxᴘᴜʟsᴇʀ ᴄᴇᴛ ᴜᴛɪʟɪsᴀᴛᴇᴜʀ.")





 
# -------------------- Promotion ---------------
@router.message(Command("promotion"))
async def promotion_handler(message: Message, command: CommandObject):
    if not command.args:
        return await message.reply("🥇 Spécifie un nom pour la promotion.")
    await message.answer(f"🥇 {command.args} est promu au rang supérieur.\n🎖️ Le clan reconnaît sa valeur.")



# ------------ Reunion --------------
@router.message(Command("reunion"))
async def reunion_handler(message: Message, command: CommandObject):
    if not command.args:
        return await message.reply("📝 Fournis un message à envoyer : /reunion [texte]")

    admins = await message.chat.get_administrators()
    count = 0

    for admin in admins:
        try:
            if not admin.user.is_bot:
                await message.bot.send_message(
                    admin.user.id,
                    f"📣 𝗥𝗲́𝘂𝗻𝗶𝗼𝗻 𝗱'𝘂𝗿𝗴𝗲𝗻𝗰𝗲 𝗱𝗮𝗻𝘀 『{message.chat.title}』\n\n"
                    f"🔻 Message : {command.args}"
                )
                count += 1
        except:
            continue

    await message.reply(f"📨 Message envoyé à {count} administrateur(s).")



# -------------- Trahison + nom   --------------------------
@router.message(Command("trahison"))
async def trahison_handler(message: Message, command: CommandObject):
    if not command.args:
        return await message.reply("🗡️ Spécifie le nom du traître : /trahison [nom]")

    nom = command.args

    # Message dans le groupe
    await message.answer(
        f"⚠️ 𝙰𝙻𝙴𝚁𝚃𝙴 𝙳𝙴 𝚃𝚁𝙰𝙷𝙸𝚂𝙾𝙽 ⚠️\n"
        f"Le membre « {nom} » est accusé de trahison.\n"
        f"Le conseil des anciens est convoqué immédiatement."
    )

    # Message privé aux admins
    admins = await message.chat.get_administrators()
    for admin in admins:
        try:
            if not admin.user.is_bot:
                await message.bot.send_message(
                    admin.user.id,
                    f"🗡️ 𝗧𝗥𝗔𝗛𝗜𝗦𝗢𝗡 : Le membre « {nom} » est suspecté de trahison dans 『{message.chat.title}』.\n"
                    f"🛑 Action urgente requise."
                )
        except:
            continue


# -------------- Hommages + nom ---------------
@router.message(Command("hommage"))
async def hommage_handler(message: Message, command: CommandObject):
    if not command.args:
        return await message.reply("⚰️ Spécifie un nom : /hommage [nom]")

    nom = command.args

    await message.answer(
        f"⚰️ 𝙷𝙾𝙼𝙼𝙰𝙶𝙴 𝙰̀ {nom.upper()} ⚰️\n\n"
        f"Une prière silencieuse s'élève pour l'âme de {nom}.\n"
        f"Le clan s'incline dans le respect et la mémoire éternelle."
    )



# ---------------------- Initiation +  nom ---------------------------
@router.message(Command("initiation"))
async def initiation_handler(message: Message, command: CommandObject):
    if not command.args:
        return await message.reply("🥷 Spécifie un nom : /initiation [nom]")
    
    nom = command.args.strip()
    
    # Message public dans le groupe
    await message.answer(
        f"🥷 𝙲𝙴́𝚁𝙴𝙼𝙾𝙽𝙸𝙴 𝙳'𝙸𝙽𝙸𝚃𝙸𝙰𝚃𝙸𝙾𝙽 🥷\n\n"
        f"Le membre *{nom}* est convoqué devant le clan.\n"
        f"🔥 L’heure est venue de prouver ta loyauté et ta valeur.\n"
        f"📜 Une nouvelle page s'écrit dans l'histoire du clan..."
    )



# ------------- /retrogradation + Nom   ---------------
@router.message(Command("retrogradation"))
async def retrogradation_handler(message: Message, command: CommandObject):
    if not command.args:
        return await message.reply("🥀 𝚂𝙿𝙴́𝙲𝙸𝙵𝙸𝙴 𝚄𝙽 𝙽𝙾𝙼 : /retrogradation [nom]")

    nom = command.args.strip()

    # Message dans le groupe
    await message.answer(
        f"🥀 𝚁𝙴𝚃𝚁𝙾𝙶𝚁𝙰𝙳𝙰𝚃𝙸𝙾𝙽 𝙴𝙽 𝙴𝙵𝙵𝙴𝙲𝚃 🥀\n\n"
        f"𝙻𝙴 𝙼𝙴𝙼𝙱𝚁𝙴 « {nom} » 𝙰 𝚃𝙴́𝚃𝙴́ 𝚁𝙴́𝚃𝚁𝙾𝙶𝚁𝙰𝙳𝙴́ 𝙰𝚄 𝚂𝙴𝙸𝙽 𝙳𝚄 𝙲𝙻𝙰𝙽.\n"
        f"⚖️ 𝙻'𝙷𝙾𝙽𝙽𝙴𝚄𝚁 𝙽𝙴 𝚂𝙴 𝙼𝙴́𝚁𝙸𝚃𝙴 𝙿𝙰𝚂, 𝙸𝙻 𝚂𝙴 𝙿𝚁𝙾𝚅𝙴."
    )

    # Message privé aux admins
    admins = await message.chat.get_administrators()
    for admin in admins:
        if not admin.user.is_bot:
            try:
                await message.bot.send_message(
                    admin.user.id,
                    f"⚠️ 𝙰𝙻𝙴𝚁𝚃𝙴 : 𝚁𝙴𝚃𝚁𝙾𝙶𝚁𝙰𝙳𝙰𝚃𝙸𝙾𝙽\n\n"
                    f"𝙻𝙴 𝙼𝙴𝙼𝙱𝚁𝙴 « {nom} » 𝙰 𝙴́𝚃𝙴́ 𝙳𝙴𝙼𝙾𝚃𝙴́ 𝙳𝙰𝙽𝚂 𝙻𝙴 𝙶𝚁𝙾𝚄𝙿𝙴 : « {message.chat.title} »."
                )
            except:
                continue


# ----------- retraite + nom ------------
@router.message(Command("retraite"))
async def retraite_handler(message: Message, command: CommandObject):
    if not command.args:
        return await message.reply("🧘 𝚂𝙿𝙴́𝙲𝙸𝙵𝙸𝙴 𝚄𝙽 𝙽𝙾𝙼 : /retraite [nom]")

    nom = command.args.strip()

    # Message dans le groupe
    await message.answer(
        f"🧘 𝚁𝙴𝚃𝚁𝙰𝙸𝚃𝙴 𝙰𝙽𝙽𝙾𝙽𝙲𝙴́𝙴\n\n"
        f"« {nom} » 𝙰 𝙳𝙴́𝙲𝙸𝙳𝙴́ 𝙳𝙴 𝚁𝙰𝙽𝙶𝙴𝚁 𝚂𝙴𝚂 𝙰𝚁𝙼𝙴𝚂.\n"
        f"🍂 𝚄𝙽 𝙼𝙴𝙼𝙱𝚁𝙴 𝙵𝙸𝙳𝙴̀𝙻𝙴 𝚀𝚄𝙸 𝙼𝙴𝚁𝙸𝚃𝙴 𝚂𝙾𝙽 𝚁𝙴𝙿𝙾𝚂."
    )

    # Message privé aux admins
    admins = await message.chat.get_administrators()
    for admin in admins:
        if not admin.user.is_bot:
            try:
                await message.bot.send_message(
                    admin.user.id,
                    f"📩 𝙽𝙾𝚃𝙸𝙵 : 𝚁𝙴𝚃𝚁𝙰𝙸𝚃𝙴\n\n"
                    f"𝙻𝙴 𝙼𝙴𝙼𝙱𝚁𝙴 « {nom} » 𝙰 𝙰𝙽𝙽𝙾𝙽𝙲𝙴́ 𝚂𝙾𝙽 𝙳𝙴𝙿𝙰𝚁𝚃 𝙳𝙴 𝙻𝙰 𝚂𝙲𝙴̀𝙽𝙴.\n"
                    f"👤 𝙶𝚁𝙾𝚄𝙿𝙴 : {message.chat.title}"
                )
            except:
                continue




# ------------ Lock et Unlock -----------------
@router.message(Command("lock"))
async def lock_command(message: Message):
    chat_member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in ("administrator", "creator"):
        return await message.reply("⛔ Tu dois être administrateur pour verrouiller le chat.")

    await message.bot.set_chat_permissions(
        chat_id=message.chat.id,
        permissions=ChatPermissions(can_send_messages=False)
    )
    await message.reply("🔒 Le chat a été verrouillé. Silence total.")


@router.message(Command("unlock"))
async def unlock_command(message: Message):
    chat_member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in ("administrator", "creator"):
        return await message.reply("⛔ Tu dois être administrateur pour déverrouiller le chat.")

    await message.bot.set_chat_permissions(
        chat_id=message.chat.id,
        permissions=ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True
        )
    )
    await message.reply("🔓 Le chat est maintenant ouvert. Reprise des activités.")
