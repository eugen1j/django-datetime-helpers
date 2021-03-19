from datetime import time, datetime, date
from unittest.mock import patch

from django_datetime_helpers.helpers import (
    time_to_int, today, yesterday, random_time, seconds_ago)


def fake_now():
    return datetime(year=2020, month=2, day=24, hour=19, minute=1, second=26)


def test_time_to_int():
    assert time_to_int(time(hour=1, minute=2, second=3)) == 3600 + 60 * 2 + 3


@patch('django.utils.timezone.now', fake_now)
def test_today():
    assert today() == date(2020, 2, 24)


@patch('django.utils.timezone.now', fake_now)
def test_yesterday():
    assert yesterday() == date(2020, 2, 23)


@patch('django.utils.timezone.now', fake_now)
def test_seconds_ago_one_second():
    assert seconds_ago(seconds=1) == datetime(
        year=2020, month=2, day=24, hour=19, minute=1, second=25)


@patch('django.utils.timezone.now', fake_now)
def test_seconds_ago_million_second():
    assert seconds_ago(seconds=1_000_000) == datetime(
        year=2020, month=2, day=13, hour=5, minute=14, second=46)


def test_random_time_for_day_time():
    time_from = time(hour=10)
    time_to = time(hour=15)

    assert time_from <= random_time(time_from, time_to) <= time_to


def test_random_time_for_night_time():
    time_from = time(hour=22)
    time_to = time(hour=3)

    random_t = random_time(time_from, time_to)

    assert random_t <= time_to or time_from <= random_t


def test_random_time_for_equal_times():
    time_from = time_to = time(hour=22, minute=12, second=16)
    assert random_time(time_from, time_to) == time_from
