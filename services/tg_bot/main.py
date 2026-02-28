"""
Telegram bot entry point (aiogram 3).

Run from this directory:
    pip install -r requirements.txt
    python main.py

Loads BOT_TOKEN from .env. Handles /start (welcome) and any other message (in development notice).
"""

import asyncio
import os
import sys

from dotenv import load_dotenv

# Load .env from the same directory as this script.
_load_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(_load_dir, ".env"))

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    print("BOT_TOKEN is not set. Add it to services/tg_bot/.env", file=sys.stderr)
    sys.exit(1)


async def main() -> None:
    from aiogram import Bot, Dispatcher
    from aiogram.client.default import DefaultBotProperties
    from aiogram.enums import ParseMode
    from aiogram.filters import CommandStart
    from aiogram.types import Message

    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    WELCOME = (
        "Hello! This is a <b>tourists agency</b> service bot.\n\n"
        "Right now we are <i>in development</i> — more features will appear soon."
    )
    IN_DEVELOPMENT = "There is nothing here yet. Everything is in development."

    @dp.message(CommandStart())
    async def cmd_start(message: Message) -> None:
        await message.answer(WELCOME)

    @dp.message()
    async def any_other(message: Message) -> None:
        await message.answer(IN_DEVELOPMENT)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
