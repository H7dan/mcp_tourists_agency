"""
Telegram bot entry point (aiogram 3).

Run from repo root with PYTHONPATH so shared is importable:
    PYTHONPATH=. python services/tg_bot/main.py
Or from this directory: pip install -r requirements.txt && python main.py (PYTHONPATH=..).

Loads BOT_TOKEN and ORCHESTRATOR_URL from .env. /start stays in bot; other text
messages go to orchestrator. If ORCHESTRATOR_URL is not set, shows IN_DEVELOPMENT.
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

ORCHESTRATOR_URL = os.getenv("ORCHESTRATOR_URL", "").rstrip("/")
ORCHESTRATOR_TIMEOUT = 60.0


async def main() -> None:
    from aiogram import Bot, Dispatcher
    from aiogram.client.default import DefaultBotProperties
    from aiogram.enums import ParseMode
    from aiogram.filters import CommandStart
    from aiogram.types import Message
    import httpx

    from shared.constants import ORCHESTRATOR_CHAT_ENDPOINT
    from shared.messages import MSG_IN_DEVELOPMENT, MSG_ENTER_TEXT, MSG_TECHNICAL_WORK, MSG_WELCOME
    from shared.models import OrchestratorRequest, OrchestratorResponse
    from shared.utils import is_text_empty

    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def cmd_start(message: Message) -> None:
        await message.answer(MSG_WELCOME)

    @dp.message()
    async def any_other(message: Message) -> None:
        if is_text_empty(message.text):
            await message.answer(MSG_ENTER_TEXT)
            return

        if not ORCHESTRATOR_URL:
            await message.answer(MSG_IN_DEVELOPMENT)
            return

        user_id = message.from_user.id if message.from_user else 0
        chat_id = message.chat.id
        text = (message.text or "").strip()

        req = OrchestratorRequest(user_id=user_id, chat_id=chat_id, text=text)
        url = f"{ORCHESTRATOR_URL}{ORCHESTRATOR_CHAT_ENDPOINT}"

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url,
                    json=req.to_dict(),
                    timeout=ORCHESTRATOR_TIMEOUT,
                )
        except (httpx.TimeoutException, httpx.ConnectError):
            await message.answer(MSG_TECHNICAL_WORK)
            return

        if not response.is_success:
            await message.answer(MSG_TECHNICAL_WORK)
            return

        try:
            data = response.json()
        except Exception:
            await message.answer(MSG_TECHNICAL_WORK)
            return

        resp = OrchestratorResponse.from_dict(data)
        if resp.text:
            await message.answer(resp.text)
        else:
            await message.answer(MSG_TECHNICAL_WORK)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
