from telegram import Update, User


def get_user_name(update: Update = None, user: User = None) -> str:
    if not update and not user:
        raise ValueError("Nenhum update ou user válido foi passado.")

    if update:
        user = update.effective_user

    user_name = user.name
    if not user_name.startswith("@"):
        user_name = ""

    return user_name
