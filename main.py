from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging
from config import BOT_tOKEN
from handlers.start import router as start_router
from handlers.help import router as help_router
from handlers.moderation import router as moderation_router
from handlers.group import router as group_router
from handlers.fun import router as fun_router
from handlers.settings import router as settings_router
from database import init_db

bot = Bot(token=BOT_tOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher(storage=MemoryStorage())

# Enregistre tous les handlers
dp.include_router(start_router)
dp.include_router(help_router)
dp.include_router(moderation_router)
dp.include_router(group_router)
dp.include_router(fun_router)
dp.include_router(settings_router)

async def main():
    logging.basicConfig(level=logging.INFO)
    init_db()  # Initialize database
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Bot is running ...................")
    asyncio.run(main())
