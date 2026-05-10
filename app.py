"""Arquivo principal que executa o telegram-bot."""

import logging

from decouple import config

from telegram.ext import Application

from bot.conversations.signup import SIGNUP_HANDLERS

TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")
MY_GROUP_ID = config("MY_GROUP_ID", cast=int)
IS_PRODUCTION = config("IS_PRODUCTION", cast=bool, default=True)

# SET LOGGING ================================================================
if IS_PRODUCTION:
    level = logging.INFO
else:
    level = logging.DEBUG

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

file_handler = logging.FileHandler(
    "pocketgram.log", mode="w", encoding="utf-8"
)
console_handler = logging.StreamHandler()
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.setLevel(level)

root_logger.addHandler(file_handler)
root_logger.addHandler(console_handler)
# SET LOGGING ================================================================

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the bot."""

    logger.info("Iniciando o PocketGram.")
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    logger.info("Adicionando handlers.")
    # Add Single Handler ======================================================
    # application.add_handler()

    # Add Multiple Handlers ===================================================
    application.add_handlers(SIGNUP_HANDLERS)

    logger.info("PocketGram iniciado com sucesso!")
    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
