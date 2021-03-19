import datetime
import random

from django.utils import timezone

# Time constants
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY
MONTH = 30 * DAY
YEAR = 365 * DAY


def time_to_int(time: datetime.time) -> int:
    """Casts time to number of seconds since 00:00"""
    return time.second * SECOND + time.minute * MINUTE + time.hour * HOUR


def int_to_time(seconds: int) -> datetime.time:
    """Casts number of seconds since 00:00 to datetime.time"""
    return datetime.time(
        seconds // HOUR,
        seconds // MINUTE % (HOUR // MINUTE),
        seconds % (MINUTE // SECOND)
    )


def today() -> datetime.date:
    """Today's date"""
    return timezone.now().date()


def yesterday() -> datetime.date:
    """Yesterday's date"""
    return today() - timezone.timedelta(days=1)


def seconds_ago(seconds: float) -> datetime.datetime:
    """
    Shortcut. Frequently used for query filtering.
    For example, all users created within 24 hours:
    `qs = User.objects.filter(created_at__gte=seconds_ago(DAY))`.
    """
    return timezone.now() - timezone.timedelta(seconds=seconds)


def random_time(time_from: datetime.time, time_to: datetime.time
                ) -> datetime.time:
    """
    Random time between time_from and time_to.
    If time_from <= time_to returns time between them: 06:00 - 12:00 -> 08:42.
    If time_from > time_to returns time between today's time_from
    and tomorrow's time_to: 20:00 - 03:00 -> 01:24.
    """
    seconds_from = time_to_int(time_from) % DAY
    seconds_to = time_to_int(time_to) % DAY

    if seconds_from <= seconds_to:
        seconds = random.randint(seconds_from, seconds_to)
    else:
        seconds_to += DAY
        seconds = random.randint(seconds_from, seconds_to) % DAY

    return int_to_time(seconds)
