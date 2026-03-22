import logging

from datetime import timedelta
from random import randint
from time import sleep
from typing import Any, Callable, Union

from bson import ObjectId
from telegram import Message
from telegram.error import RetryAfter, TimedOut
from telegram.ext import ContextTypes, ConversationHandler


logger = logging.getLogger(__name__)
BASE_JOB_KWARGS = {"misfire_grace_time": None}


# CALL TELEGRAM FUNCTIONs
async def call_telegram_message_function(
    function_caller: str,
    function: Callable,
    context: ContextTypes.DEFAULT_TYPE,
    need_response: bool = True,
    skip_retry: bool = False,
    auto_delete_message: Union[bool, int, timedelta] = True,
    **kwargs,
) -> Union[Any, Message]:
    """Função que chama qualquer função de mensagem do telegram.
    Caso ocorra um erro do tipo RetryAfter ou TimedOut, a função agurdará
    alguns segundos tentará novamente com um número máximo de 3 tentativas.
    Caso a função retorne um objeto do tipo Message, a mensagem será excluída
    em "HOURS_DELETE_MESSAGE_FROM_CONTEXT" horas.

    Se need_response for True, a função aguardará para realizar uma nova
    tentativa, caso contrário, a função será agendada em um job para ser
    executada posteriormente.

    Se skip_retry for True, a função não tentará novamente e nem agendará uma
    nova tentativa.

    Se auto_delete_message for igual a False, a exclusão automática da
    mensagem será ignorada. Caso seja igual a True, a mensagem será excluída
    em "HOURS_DELETE_MESSAGE_FROM_CONTEXT" horas.
    Mas se for um valor inteiro positivo, a mensagem será excluída em uma
    quantidade de horas igual ao valor passado.
    E se for um timedelta, a mensagem será excluída de acordo com o tempo
    passado no timedelta.
    """

    logger.info(f"{function_caller}->CALL_TELEGRAM_MESSAGE_FUNCTION()")
    job_call_telegram_kwargs = dict(
        function_caller=function_caller,
        function=function,
        context=context,
        **kwargs,
    )
    response = None
    is_error = True
    catched_error = None
    for i in range(3):
        try:
            response = await function(**kwargs)
            is_error = False
            break
        except (RetryAfter, TimedOut) as error:
            catched_error = error
            error_name = error.__class__.__name__
            if skip_retry is True:
                break

            if isinstance(error, RetryAfter):
                sleep_time = error.retry_after + randint(1, 3)
            elif isinstance(error, TimedOut):
                sleep_time = 5

            if need_response is False:
                logger.warning(
                    f"{error_name}{i}({sleep_time}): "
                    f'creating JOB "{function.__name__}" '
                )
                job_name = (
                    f"{function_caller}->"
                    "CALL_TELEGRAM_MESSAGE_FUNCTION->"
                    f"JOB_CALL_TELEGRAM-{ObjectId()}"
                )
                context.job_queue.run_once(
                    callback=job_call_telegram,
                    when=timedelta(seconds=sleep_time),
                    data=job_call_telegram_kwargs,
                    name=job_name,
                    job_kwargs=BASE_JOB_KWARGS,
                )
                return ConversationHandler.END

            logger.warning(
                f'{error_name}{i}: RETRYING activate "{function.__name__}" '
                f"from {function_caller} in {sleep_time} seconds."
            )
            sleep(sleep_time)
            continue

    if is_error is True:
        logger.warning(f"ERROR: {function_caller}")
        if catched_error:
            raise catched_error
        raise Exception(f"Error in {function_caller}")

    return response


async def delete_message_from_context(
    function_caller: str,
    context: ContextTypes.DEFAULT_TYPE,
    message_id: int,
):
    """Deleta a mensagem usando context, mas ignora ação caso
    ocorra um erro BadRequest (Mensagem não encontrada).
    """

    chat_id = context._chat_id
    function_caller = f"{function_caller}->DELETE_MESSAGE_FROM_CONTEXT()"
    try:
        logger.info("DELETE_MESSAGE_FROM_CONTEXT() TRYING DELETE_MESSAGE")
        delete_message_kwargs = dict(chat_id=chat_id, message_id=message_id)
        await call_telegram_message_function(
            function_caller=function_caller,
            function=context.bot.delete_message,
            context=context,
            need_response=False,
            **delete_message_kwargs,
        )
    except BadRequest as e:
        logger.warning("DELETE_MESSAGE_FROM_CONTEXT() BADREQUEST EXCEPT")
        if "Message to delete not found" in e.message:
            logger.warning(f'\tError Message: "{e.message}"')
        elif "Message can't be deleted" in e.message:
            logger.warning(f'\tError Message: "{e.message}" (Sem Permissão)')
        else:
            raise e


# JOB FUNCTIONs
# Funções usandas no callback de agendamentos do context.job_queue
async def job_call_telegram(context: ContextTypes.DEFAULT_TYPE):
    """Job que chama a função call_telegram_message_function caso ocorra um
    erro do tipo RetryAfter, TimedOut e o need_response seja False
    """

    logger.info("JOB_CALL_TELEGRAM()")
    job = context.job
    call_telegram_kwargs = job.data
    call_telegram_kwargs["function_caller"] += " and JOB_CALL_TELEGRAM()"
    logger.info(call_telegram_kwargs["function_caller"])

    await call_telegram_message_function(**call_telegram_kwargs)


async def job_delete_message_from_context(context: ContextTypes.DEFAULT_TYPE):
    """Job que exclui a mensagem após um tempo pré determinado."""

    logger.info("JOB_DELETE_MESSAGE_FROM_CONTEXT()")
    job = context.job
    data = job.data
    message_id = data["message_id"]
    function_caller = data["function_caller"]

    await delete_message_from_context(
        function_caller=function_caller, context=context, message_id=message_id
    )


