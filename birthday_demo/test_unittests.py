import datetime

from . import utils

today = datetime.date.today()
next_week = today.replace(day=today.day + 7)
next_year = today.replace(year=today.year + 1, day=today.day - 1)


def test_birthday_is_today():
    assert utils.get_days_to_next_birthday(today.strftime("%Y-%m-%d")) == 0


def test_birthday_is_next_week():
    assert utils.get_days_to_next_birthday(next_week.strftime("%Y-%m-%d")) == 7


def test_birthday_is_next_year():
    '''This test will fail if a leap year is in play'''
    assert utils.get_days_to_next_birthday(next_year.strftime("%Y-%m-%d")) == 365
