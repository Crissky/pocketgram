from datetime import datetime, timedelta
from random import randint

import pytz


UTC = pytz.UTC
BRAZIL_TIMEZONE = pytz.timezone('America/Sao_Paulo')
MIN_ADD_MINUTES = 5
MAX_ADD_MINUTES = 10


def get_utc_time_now() -> datetime:
    dt = datetime.now(tz=UTC)

    return dt


def get_brazil_time_now() -> datetime:
    dt = get_utc_time_now()
    dt = utc_to_brazil_datetime(dt)

    return dt


def datetime_to_string(dt: datetime) -> str:
    if isinstance(dt, datetime):
        dt = dt.strftime("%d/%m/%Y %H:%M:%S")

    return dt


def utc_to_brazil_datetime(dt: datetime) -> datetime:
    dt = dt.astimezone(BRAZIL_TIMEZONE)

    return dt


def brazil_to_utc_datetime(dt: datetime) -> datetime:
    dt = replace_tzinfo(dt)
    delta = timedelta(hours=3)

    return dt + delta


