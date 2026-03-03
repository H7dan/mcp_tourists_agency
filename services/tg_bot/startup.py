
from aiogram import Bot


async def log_startup(bot: Bot) -> None:
    """
    Print a confirmation message once the bot is connected and ready.

    Called automatically by aiogram on dispatcher startup
    (registered in `main.py` via `dp.startup.register(log_startup)`).
    """
    me = await bot.get_me()
    print(
        f"[tg_bot] Connected as @{me.username} (id={me.id}). "
        "Bot is ready to receive updates."
    )