from aiogram import Router
from aiogram.types import Message, ChatMemberUpdated
from aiogram.filters import Command
import types
from database import add_group, get_stats

router = Router()

rules_text = "📜 ʀᴇɢʟᴇs ᴅᴜ ɢʀᴏᴜᴘᴇ:\n1. Pas de spam\n2. Respectez tout le monde\n3. Pas de contenu interdit\n\nMerci de respecter ces règles."
hierarchie_text = "👑 ʜɪᴇʀᴀʀᴄʜɪᴇ ᴅᴜ ɢʀᴏᴜᴘᴇ:\n• Oyabun - Propriétaire\n• Wakagashira - Modérateur\n• Kyodai - Membre senior\n• Shatei - Membre"

@router.message(Command("rules"))
async def send_rules(message: Message):
    await message.reply(rules_text)

@router.message(Command("setrules"))
async def set_rules(message: Message):
    args = message.text.split()[1:]
    new_rules = ' '.join(args) if args else None
    global rules_text
    if new_rules:
        rules_text = f"📜 ʀᴇɢʟᴇs ᴅᴜ ɢʀᴏᴜᴘᴇ:\n{new_rules}"
        await message.reply("✅ Règles mises à jour.")
    else:
        await message.reply("⚠️ Utilisation : /setrules [nouveau texte des règles]")

@router.message(Command("hierarchy"))
async def send_hierarchie(message: Message):
    await message.reply(hierarchie_text)

@router.message(Command("sethierarchy"))
async def set_hierarchie(message: Message):
    args = message.text.split()[1:]
    new_hierarchie = ' '.join(args) if args else None
    global hierarchie_text
    if new_hierarchie:
        hierarchie_text = f"👑 ʜɪᴇʀᴀʀᴄʜɪᴇ ᴅᴜ ɢʀᴏᴜᴘᴇ:\n{new_hierarchie}"
        await message.reply("✅ Hiérarchie mise à jour.")
    else:
        await message.reply("⚠️ Utilisation : /sethierarchie [nouveau texte de hiérarchie]")

honor_code = (
    "⚔️ ᴄᴏᴅᴇ ᴅ'ʜᴏɴɴᴇᴜʀ ʏᴀᴋᴜᴢᴀ:\n"
    "• Fᴀɪʀᴛʀᴀɴs ᴅɪsᴄʀᴇᴛ ᴇᴛ ʟᴏʏᴀʟ\n"
    "• Jᴀᴍᴀɪs ʟᴇᴠᴇʀ ʟᴀ ᴍᴀɪɴ sᴜʀ ᴜɴ ᴄᴏᴍᴘʟɪᴄᴇ\n"
    "• Pʀᴏᴛᴇɢᴇʀ ʟᴇ ɢʀᴏᴜᴘᴇ ᴇᴛ ᴄᴇʟᴇʙʀᴇʀ ʟᴀ ʜᴏɴɴᴇᴜʀ\n"
)

@router.message(Command("code"))
async def show_code(message: Message):
    await message.reply(honor_code)

@router.message(Command("setcode"))
async def set_code(message: Message):
    args = message.text.split()[1:]
    new_code = ' '.join(args) if args else None
    global honor_code
    if new_code:
        honor_code = f"⚔️ ᴄᴏᴅᴇ ᴅ'ʜᴏɴɴᴇᴜʀ ʏᴀᴋᴜᴢᴀ:\n{new_code}"
        await message.reply("✅ Code d'honneur mis à jour avec succès.")
    else:
        await message.reply("⚠️ Utilisation : /setcode [nouveau code d'honneur]")

missions_text = (
    "🎯 ᴍɪssɪᴏɴs ʏᴀᴋᴜᴢᴀ:\n"
    "• Pʀᴏᴛᴇɢᴇʀ ʟᴇ ᴄʟᴀɴ ᴀᴠᴇᴄ ʜᴏɴɴᴇᴜʀ\n"
    "• Eᴋsᴇ́ᴄᴜᴛᴇʀ ʟᴇs ᴛᴀᴄᴛɪqᴜᴇs ᴇᴛ ᴅᴇs ᴍɪssɪᴏɴs ᴅᴇ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ\n"
    "• ʙᴀᴛᴛʀᴇ ʟᴇs ɪɴғʀᴀᴄᴛᴇᴜʀs ᴇᴛ ᴍᴀɪɴᴛᴇɴɪʀ ʟᴏʀᴅʀᴇ\n"
)

@router.message(Command("missions"))
async def show_missions(message: Message):
    await message.reply(missions_text)

@router.message(Command("setmissions"))
async def set_missions(message: Message):
    args = message.text.split()[1:]
    new_missions = ' '.join(args) if args else None
    global missions_text
    if new_missions:
        missions_text = f"🎯 ᴍɪssɪᴏɴs ʏᴀᴋᴜᴢᴀ:\n{new_missions}"
        await message.reply("✅ Missions mises à jour avec succès.")
    else:
        await message.reply("⚠️ Utilisation : /setmissions [nouvelles missions]")

@router.message(Command("honneur"))
async def rendre_honneur(message: types.Message):
    args = message.text.split()[1:]
    nom = ' '.join(args) if args else None
    if not nom:
        await message.reply("⚠️ ᴠᴇᴜɪʟʟᴇᴢ ᴍᴇᴛᴛʀᴇ ʟᴇ ɴᴏᴍ ᴅᴜ ᴍᴇᴍʙʀᴇ.\n\n🗡️ ᴇxᴇᴍᴘʟᴇ : /honneur + nom_de_la_personne")
        return
    texte = (
        f"⚔️✨ ʜᴏɴɴᴇᴜʀ ᴇᴛ ᴘʀɪᴅᴇ ᴀ ʟ'ᴇ́ʟɪᴛᴇ ʏᴀᴋᴜᴢᴀ ✨⚔️\n\n"
        f"🈶 ᴀᴜᴅᴀᴄɪᴇᴜx ᴇᴛ ɪɴᴛʀᴇᴘɪᴅᴇ, ʟᴇ ᴛʀᴜᴇ ʏᴀᴋᴜᴢᴀ :\n"
        f"🈯️ ʟ'ɪɴᴠɪɴᴄɪʙʟᴇ ᴀᴍɪ  『 {nom} 』\n\n"
        "╔══════════════════╗\n"
        "║  🔥 ɢʀᴀɴᴅ ʀᴇᴄᴏɴɴᴀɪssᴀɴᴄᴇ 🔥 ║\n"
        "║  ʟ'ᴜɴɪǫᴜᴇ ᴄʜᴀᴍᴘɪᴏɴ ᴅᴜ ᴄʟᴀɴ  ║\n"
        "║  ᴠᴀʟᴇᴜʀ ᴇᴛ ʜᴏɴɴᴇᴜʀ ɪɴᴄᴀʀɴᴇ́s ║\n"
        "╚══════════════════╝\n\n"
        "⚜️ ʟ'ᴏʀᴅʀᴇ ᴅᴜ ʏᴀᴋᴜᴢᴀ ʀᴇᴄᴏɴɴᴀɪᴛ ᴛᴏɴ ᴄᴏᴜʀᴀɢᴇ ᴇᴛ ᴛᴀ ʟᴏʏᴀᴜᴛᴇ́.\n"
        "⚜️ ᴛᴜ ᴇs ᴜɴ ᴍᴀɪᴛʀᴇ ᴅᴜ ᴄʜᴀᴏs ᴇᴛ ᴅᴜ ʜᴏɴɴᴇᴜʀ.\n"
        "⚜️ ʀᴇsᴛᴇ ᴛʀᴀɴsᴄᴇɴᴅᴀɴᴛ ᴇᴛ ᴛᴜ ʀᴇɢɴᴇʀᴀs ᴇɴ ᴍᴀîtʀᴇ ɪɴᴠɪsɪʙʟᴇ.\n\n"
        "👊 ᴘᴏᴜʀ ʟ'ʜᴏɴɴᴇᴜʀ ᴇᴛ ʟᴀ ɢʟᴏɪʀᴇ ᴅᴜ ʏᴀᴋᴜᴢᴀ 👊"
    )
    await message.reply(texte)

@router.message(Command("report"))
async def report_user(message: Message):
    if not message.reply_to_message:
        return await message.reply("🔁 Réponds au message de l'utilisateur que tu veux signaler.")

    reported_user = message.reply_to_message.from_user
    await message.reply(
        f"⚠️ <b>Signalement envoyé</b>\n"
        f"L'utilisateur <a href='tg://user?id={reported_user.id}'>{reported_user.full_name}</a> "
        f"a été signalé aux admins.",
        parse_mode="HTML"
    )

    admins = await message.bot.get_chat_administrators(message.chat.id)
    for admin in admins:
        try:
            await message.bot.send_message(
                admin.user.id,
                f"👮 Signalement dans {message.chat.title} :\n"
                f"Utilisateur signalé : {reported_user.full_name} ({reported_user.id})\n"
                f"Par : {message.from_user.full_name} ({message.from_user.id})"
            )
        except:
            continue

@router.message(Command("setpp"))
async def set_group_photo(message: Message):
    if not message.chat.type in ["group", "supergroup"]:
        return await message.reply("❌ Cette commande fonctionne uniquement dans un groupe.")
    
    if not message.photo:
        return await message.reply("🖼️ Envoie une image avec la commande pour la définir comme photo de groupe.")

    photo = await message.bot.get_file(message.photo[-1].file_id)
    photo_path = await message.bot.download_file(photo.file_path)

    with open("group_photo.jpg", "wb") as f:
        f.write(photo_path.read())

    with open("group_photo.jpg", "rb") as photo_file:
        try:
            await message.bot.set_chat_photo(chat_id=message.chat.id, photo=photo_file)
            await message.reply("✅ Photo du groupe mise à jour avec succès.")
        except:
            await message.reply("❌ Impossible de modifier la photo. Vérifie les permissions.")

@router.message(Command("delpp"))
async def delete_group_photo(message: Message):
    if not message.chat.type in ["group", "supergroup"]:
        return await message.reply("❌ Cette commande fonctionne uniquement dans un groupe.")

    try:
        await message.bot.delete_chat_photo(chat_id=message.chat.id)
        await message.reply("🗑️ Photo du groupe supprimée avec succès.")
    except:
        await message.reply("❌ Impossible de supprimer la photo. Vérifie les permissions.")

@router.message(Command("pin"))
async def pin_message(message: Message):
    if not message.reply_to_message:
        return await message.reply("📌 ʀᴇ́ᴘᴏɴᴅs ᴀ̀ ᴜɴ ᴍᴇssᴀɢᴇ ᴘᴏᴜʀ ʟ'ᴇ́ᴘɪɴɢʟᴇʀ.")
    try:
        await message.bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        await message.reply("✅ ᴍᴇssᴀɢᴇ ᴇ́ᴘɪɴɢʟᴇ́ ᴀᴠᴇᴄ sᴜᴄᴄᴇ̀s.")
    except:
        await message.reply("❌ ᴇ́ᴄʜᴇᴄ ᴅᴇ ʟ'ᴇ́ᴘɪɴɢʟᴀɢᴇ. ᴘᴇʀᴍɪssɪᴏɴs ?")

@router.message(Command("unpin"))
async def unpin_message(message: Message):
    try:
        await message.bot.unpin_chat_message(message.chat.id)
        await message.reply("📍 ᴍᴇssᴀɢᴇ ᴅᴇ́sᴇ́ᴘɪɴɢʟᴇ́.")
    except:
        await message.reply("❌ ɪᴍᴘᴏssɪʙʟᴇ ᴅᴇ ᴅᴇ́sᴇ́ᴘɪɴɢʟᴇʀ.")

@router.message(Command("unpinall"))
async def unpin_all_messages(message: Message):
    try:
        await message.bot.unpin_all_chat_messages(message.chat.id)
        await message.reply("📍 ᴛᴏᴜs ʟᴇs ᴍᴇssᴀɢᴇs ᴏɴᴛ ᴇ́ᴛᴇ́ ᴅᴇ́sᴇ́ᴘɪɴɢʟᴇ́s.")
    except:
        await message.reply("❌ ɪᴍᴘᴏssɪʙʟᴇ ᴅᴇ ᴅᴇ́sᴇ́ᴘɪɴɢʟᴇʀ ᴛᴏᴜs ʟᴇs ᴍᴇssᴀɢᴇs.")


# ------------ Tagall && Tagadmin ----------------

@router.message(Command("tagadmin"))
async def tag_admins(message: Message):
    chat = await message.bot.get_chat(message.chat.id)
    admins = await message.bot.get_chat_administrators(message.chat.id)

    tags = ""
    for admin in admins:
        if not admin.user.is_bot:
            tags += f"⎆ <a href='tg://user?id={admin.user.id}'>{admin.user.full_name}</a>\n"

    if tags:
        await message.reply(
            "⛩️ <b>ʏᴀᴋᴜᴢᴀ ᴀᴅᴍɪɴs ᴛᴀɢɢᴇᴅ :</b>\n\n" + tags,
            parse_mode="HTML"
        )
    else:
        await message.reply("❌ ɴᴏ ᴀᴅᴍɪɴs ғᴏᴜɴᴅ.")



@router.message(Command("tagall"))
async def tag_all(message: Message):
    chat = message.chat

    if not chat.type in ("group", "supergroup"):
        return await message.reply("❌ Cette commande ne peut être utilisée que dans un groupe.")

    members = await message.bot.get_chat_administrators(chat.id)  # Remplace par ta logique si tu veux tous les membres
    mentions = []

    for member in members:
        if member.user.is_bot:
            continue
        mention = f"<a href='tg://user?id={member.user.id}'>{member.user.full_name}</a>"
        mentions.append(mention)

    text = "📢 ᴛᴀɢɢɪɴɢ ᴀᴅᴍɪɴs:\n" + "\n".join(mentions)

    await message.reply(text, parse_mode="HTML", disable_web_page_preview=True)

@router.my_chat_member()
async def on_bot_added_to_group(update: ChatMemberUpdated):
    if update.new_chat_member.status in ["member", "administrator"]:
        add_group(update.chat.id, update.chat.title or "Unknown Group")

@router.message(Command("stats"))
async def stats_command(message: Message):
    unique_users, total_interactions, total_groups = get_stats()
    await message.reply(
        f"📊 <b>Statistiques Yakuza Bot</b>\n\n"
        f"👥 Utilisateurs uniques : {unique_users}\n"
        f"💬 Interactions totales : {total_interactions}\n"
        f"🏠 Groupes : {total_groups}",
        parse_mode="HTML"
    )

