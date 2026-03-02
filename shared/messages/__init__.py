"""
User-facing messages (сообщения для пользователя).

Central place for all copy shown to users: welcome, placeholders, errors.
"""

# Telegram bot: /start welcome
MSG_WELCOME = (
    "Hello! This is a <b>tourists agency</b> service bot.\n\n"
    "Right now we are <i>in development</i> — more features will appear soon."
)

# Telegram bot: placeholder when orchestrator is not used yet
MSG_IN_DEVELOPMENT = "There is nothing here yet. Everything is in development."

# Error / edge-case messages (bot shows these; details logged in orchestrator)
MSG_ENTER_TEXT = "Введите, пожалуйста, текст."
MSG_SERVICE_UNAVAILABLE = "Сервис временно недоступен"
MSG_TECHNICAL_WORK = "Что-то сломалось — идут технические работы"

__all__ = [
    "MSG_WELCOME",
    "MSG_IN_DEVELOPMENT",
    "MSG_ENTER_TEXT",
    "MSG_SERVICE_UNAVAILABLE",
    "MSG_TECHNICAL_WORK",
]
