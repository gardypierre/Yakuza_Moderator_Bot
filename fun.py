import random
import types
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import CallbackQuery

router = Router()

@router.message(Command("dice"))
async def dice_handler(message: Message):
    await message.answer_dice(emoji="🎲")  # Dé classique

@router.message(Command("dart"))
async def dart_handler(message: Message):
    await message.answer_dice(emoji="🎯")  # Fléchette

@router.message(Command("basket"))
async def basket_handler(message: Message):
    await message.answer_dice(emoji="🏀")  # Basket-ball

@router.message(Command("bowling"))
async def bowling_handler(message: Message):
    await message.answer_dice(emoji="🎳")  # Bowling

@router.message(Command("slot"))
async def slot_handler(message: Message):
    await message.answer_dice(emoji="🎰")  # Machine à sous

@router.message(Command("football"))
async def football_handler(message: Message):
    await message.answer_dice(emoji="⚽")  # Football

@router.message(Command("baseball"))
async def baseball_handler(message: Message):
    await message.answer_dice(emoji="⚾")  # Baseball


@router.message(Command("compliment"))
async def compliment(message: Message):
    compliments = [
        "✨ 𝕋𝕦 𝕖𝕤 𝕦𝕟𝕖 𝕡𝕖𝕣𝕝𝕖 𝕣𝕒𝕣𝕖! ✨",
        "🌟 𝕋𝕒 𝕓𝕖𝕒𝕦𝕥é 𝕡𝕒𝕣𝕒𝕤𝕤𝕖 𝕝𝕖𝕤 𝕣𝕠𝕔𝕙𝕖𝕤! 🌟",
        "🔥 𝕋𝕦 𝕖𝕤 𝕦𝕟 𝕪𝕒𝕜𝕦𝕫𝕒 𝕕𝕦 𝕔𝕠𝕕𝕖! 🔥"
    ]
    await message.answer(random.choice(compliments))

@router.message(Command("fortune"))
async def fortune(message: Message):
    fortunes = [
        "🔮 𝕋𝕒 𝕛𝕠𝕦𝕣𝕟é𝕖 𝕤𝕖𝕣𝕒 𝕝𝕦𝕞𝕚𝕟𝕖𝕦𝕤𝕖 𝕖𝕥 𝕡𝕝𝕖𝕚𝕟𝕖 𝕕'𝕖𝕟𝕖𝕣𝕘𝕚𝕖! 🔮",
        "🍀 𝕃𝕒 𝕔𝕙𝕒𝕟𝕔𝕖 𝕤𝕠𝕦𝕤 𝕝𝕖 𝕤𝕚𝕘𝕟𝕖 𝕕𝕖 𝕝𝕒 𝕝𝕦𝕟𝕖 𝕥'𝕒𝕔𝕔𝕠𝕞𝕡𝕒𝕘𝕟𝕖! 🍀",
        "🔥 𝕋𝕠𝕟 𝕔𝕠𝕦𝕣𝕒𝕘𝕖 𝕥'𝕣𝕖𝕟𝕕 𝕚𝕟𝕧𝕚𝕟𝕔𝕥𝕖! 🔥"
    ]
    await message.answer(random.choice(fortunes))


jokes = [
    "😂 ᴘᴏᴜʀǫᴜᴏɪ ʟᴇs ᴘᴏɪssᴏɴs ᴅᴇ́ᴛᴇsᴛᴇɴᴛ ʟ’ᴏʀᴅɪɴᴀᴛᴇᴜʀ ? ᴘᴀʀᴄᴇ ǫᴜ’ɪʟs ᴏɴᴛ ᴘᴇᴜʀ ᴅᴜ ɴᴇᴛ.",
    "😹 ᴘᴏᴜʀǫᴜᴏɪ ʟᴇs ᴄᴀɴᴀʀᴅs sᴏɴᴛ ᴛᴏᴜᴊᴏᴜʀs ᴀ ʟ’ʜᴇᴜʀᴇ ? ᴘᴀʀᴄᴇ ǫᴜ’ɪʟs sᴏɴᴛ ᴅᴀɴs ʟ’ᴇ́ᴛᴀɴɢ.",
    "🤣 ǫᴜᴇ ᴅɪᴛ ᴜɴᴇ ɪᴍᴘʀɪᴍᴀɴᴛᴇ ᴅᴀɴs ʟ’ᴇ́ᴀᴜ ? ᴊ’ᴀɪ ᴘᴀᴘɪᴇʀ !",
    "😆 ᴘᴏᴜʀǫᴜᴏɪ ʟᴇs ᴍᴀᴛʜs sᴏɴᴛ ᴛʀɪsᴛᴇs ? ᴘᴀʀᴄᴇ ǫᴜ’ᴇʟʟᴇs ᴏɴᴛ ᴛʀᴏᴘ ᴅᴇ ᴘʀᴏʙʟᴇ̀ᴍᴇs."
]

@router.message(Command("joke"))
async def send_joke(message: types.Message):
    joke = random.choice(jokes)
    await message.answer(joke)


# ----------------------- 8ball ----------------------

answers = [
    "✨ ʏᴇs, ᴅᴇғɪɴɪᴛᴇʟʏ!",
    "❌ ɴᴏ, ɴᴇᴠᴇʀ ɪɴ ʏᴏᴜʀ ʟɪғᴇ.",
    "🤔 ᴍᴀʏʙᴇ ᴡʜᴇɴ ᴛʜᴇ ᴍᴏᴏɴ ɪs ʜɪɢʜ.",
    "🌟 ᴀʙsᴏʟᴜᴛᴇʟʏ ɴᴏᴛ!",
    "🔮 ᴛʜᴇ ᴛʀᴜᴛʜ ɪs ʙʟᴜʀʀᴇᴅ.",
    "💫 ᴀs ɪ  sᴇᴇ ɪᴛ, ʏᴇs."
]
@router.message(Command("8ball"))
async def magic_8ball(message: types.Message):
    response = random.choice(answers)
    await message.reply(f"🎱 8-ʙᴀʟʟ ᴄʜᴀʀᴍ: {response}")



@router.message(Command("hug"))
async def hug_cmd(message: Message):
    if not message.reply_to_message:
        return await message.reply("🤗 ʀᴇ́ᴘᴏɴᴅs ᴀ ᴜɴ ᴍᴇssᴀɢᴇ ᴘᴏᴜʀ ғᴀɪʀᴇ ᴜɴ ᴄᴀʟɪɴ.")
    
    user = message.reply_to_message.from_user
    await message.reply(
        f"🤗 <b>{message.from_user.full_name}</b> ᴀ sᴇʀʀᴇ́ <b>{user.full_name}</b> ᴅᴀɴs sᴏɴs ʙʀᴀs. ✨",
        parse_mode="HTML"
    )

@router.message(Command("slap"))
async def slap_cmd(message: Message):
    if not message.reply_to_message:
        return await message.reply("👋 ʀᴇ́ᴘᴏɴᴅs ᴀ ᴜɴ ᴍᴇssᴀɢᴇ ᴘᴏᴜʀ ɢɪғʟᴇʀ ǫᴜᴇʟǫᴜ'ᴜɴ.")
    
    user = message.reply_to_message.from_user
    await message.reply(
        f"👋 <b>{message.from_user.full_name}</b> ᴀ ɢɪғʟᴇ́ <b>{user.full_name}</b> ᴘᴀʀ ᴘᴜʀ ʀᴇsᴘᴇᴄᴛ ʏᴀᴋᴜᴢᴀ.",
        parse_mode="HTML"
    )


@router.message(Command("kill"))
async def kill_cmd(message: Message):
    if not message.reply_to_message:
        return await message.reply("🔪 ʀᴇ́ᴘᴏɴᴅs ᴀ ᴜɴ ᴍᴇssᴀɢᴇ ᴘᴏᴜʀ 'ᴇ́ʟɪᴍɪɴᴇʀ' ǫᴜᴇʟǫᴜ'ᴜɴ.")

    user = message.reply_to_message.from_user
    await message.reply(
        f"🔪 <b>{message.from_user.full_name}</b> ᴀ 'éʟɪᴍɪɴᴇ́' <b>{user.full_name}</b> ᴘᴏᴜʀ ʟ'ʜᴏɴɴᴇᴜʀ ᴅᴇ ʟᴀ ғᴀᴍɪʟʟᴇ.",
        parse_mode="HTML"
    )


