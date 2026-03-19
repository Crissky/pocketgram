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


async def call_telegram_message_function(
    function_caller: str,
    function: Callable,
    context: ContextTypes.DEFAULT_TYPE,
    need_response: bool = True,
    skip_retry: bool = False,
    auto_delete_message: Union[bool, int, timedelta] = True,
    **kwargs
) -> Union[Any, Message]:
    '''Função que chama qualquer função de mensagem do telegram.
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
    '''

    logger.info(f'{function_caller}->CALL_TELEGRAM_MESSAGE_FUNCTION()')
    job_call_telegram_kwargs = dict(
        function_caller=function_caller,
        function=function,
        context=context,
        **kwargs
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

    return response