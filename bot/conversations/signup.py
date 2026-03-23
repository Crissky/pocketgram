from telegram import Update
from telegram.ext import ContextTypes, PrefixHandler, CommandHandler

from bot.constants.commands import SIGNUP_COMMNADS
from bot.constants.filters import BASIC_COMMAND_FILTER, PREFIX_COMMANDS
from bot.functions.messages import call_telegram_message_function
from functions.bot.user import get_user_name
from pocketgram.trainer import Trainer
from repository.mongo.functions.trainer import save_trainer, exists_trainer


async def signup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_name = get_user_name(update=update)
    trainer = Trainer(user_id=user_id, user_name=user_name)

    if exists_trainer(trainer.user_id):
        reply_text = (
            f"Trainer com USER ID: '{trainer.user_id}', já está cadastrado."
        )
    else:
        new_trainer = save_trainer(trainer)
        reply_text = (
            f"Olá {user_name}! "
            f"Você foi cadastrado com sucesso!\n\n{new_trainer}"
        )

    reply_text_kwargs = dict(text=reply_text)
    await call_telegram_message_function(
        function_caller='SIGNUP()',
        function=update.message.reply_text,
        context=context,
        need_response=False,
        skip_retry=False,
        auto_delete_message=True,
        **reply_text_kwargs
    )


SIGNUP_HANDLERS = [
    PrefixHandler(
        PREFIX_COMMANDS, SIGNUP_COMMNADS, signup, BASIC_COMMAND_FILTER
    ),
    CommandHandler(SIGNUP_COMMNADS, signup, BASIC_COMMAND_FILTER),
]
