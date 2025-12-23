from telegram import Update
from telegram.ext import ContextTypes, PrefixHandler, CommandHandler

from bot.constants.commands import SIGNUP_COMMNADS
from bot.constants.filters import BASIC_COMMAND_FILTER, PREFIX_COMMANDS
from functions.bot.user import get_user_name
from pocketgram.trainer import Trainer
from repository.mongo.models.trainer import TrainerModel


async def signup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_name = get_user_name(update=update)
    trainer_model = TrainerModel()
    trainer = Trainer(user_id=user_id, user_name=user_name)
    trainer_model.save(trainer)
    new_trainer = trainer_model.get_by_id(user_id)

    await update.message.reply_text(
        f"Olá {user_name}! Você foi cadastrado com sucesso!\n\n{new_trainer}"
    )


SIGNUP_HANDLERS = [
    PrefixHandler(
        PREFIX_COMMANDS, SIGNUP_COMMNADS, signup, BASIC_COMMAND_FILTER
    ),
    CommandHandler(SIGNUP_COMMNADS, signup, BASIC_COMMAND_FILTER),
]
