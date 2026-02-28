"""
Telegram bot entry point (aiogram 3).

Run from repo root with PYTHONPATH so shared is importable:
    PYTHONPATH=. python services/tg_bot/main.py
Or from this directory: pip install -r requirements.txt && python main.py (PYTHONPATH=..).

Loads BOT_TOKEN from .env. /start stays in bot; other text messages go to orchestrator (when wired).
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

    from shared.messages import IN_DEVELOPMENT, MSG_ENTER_TEXT, WELCOME
    from shared.utils import is_text_empty

    @dp.message(CommandStart())
    async def cmd_start(message: Message) -> None:
        await message.answer(WELCOME)

    @dp.message()
    async def any_other(message: Message) -> None:
        if is_text_empty(message.text):
            await message.answer(MSG_ENTER_TEXT)
            return
        await message.answer(IN_DEVELOPMENT)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
