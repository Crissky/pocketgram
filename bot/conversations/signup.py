from telegram import Update
from telegram.ext import ContextTypes, PrefixHandler, CommandHandler

from bot.constants.commands import SIGNUP_COMMNADS
from bot.constants.filters import BASIC_COMMAND_FILTER, PREFIX_COMMANDS


async def signup(update: Update, context: ContextTypes.DEFAULT_TYPE): ...


SIGNUP_HANDLERS = [
    PrefixHandler(
        PREFIX_COMMANDS, SIGNUP_COMMNADS, signup, BASIC_COMMAND_FILTER
    ),
    CommandHandler(SIGNUP_COMMNADS, signup, BASIC_COMMAND_FILTER),
]
