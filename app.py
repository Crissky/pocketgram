'''Arquivo principal que executa o telegram-bot.
'''


import logging

from decouple import config

from telegram.ext import Application

from bot.conversations.signup import SIGNUP_HANDLERS


TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")
MY_GROUP_ID = config('MY_GROUP_ID', cast=int)
ENVIRONMENT = config('ENVIRONMENT', default='PRODUCTION')

# Logging Config
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Run the bot."""
    # Logging
    if TELEGRAM_TOKEN is None:
        logger.warning('Variável TELEGRAM_TOKEN não definida.')
    else:
        logger.info('Variável TELEGRAM_TOKEN definida.')
    if MY_GROUP_ID is None:
        logger.warning('Variável MY_GROUP_ID não definida.')
    else:
        logger.info('Variável MY_GROUP_ID definida.')
    logger.info(f'Environment: {ENVIRONMENT}')

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add Single Handler ======================================================
    # application.add_handler()

    # Add Multiple Handlers ===================================================
    application.add_handlers(SIGNUP_HANDLERS)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
