from datetime import timedelta
from book import convert
from book.__main__ import parse_time


def test_convert_time():
    completed = timedelta(hours=1, minutes=30)
    overall = timedelta(hours=3)
    result = convert.time_to_pages(completed, overall, pages=100)
    assert result == 50


def test_parse_time():
    assert parse_time(time='1:30') == timedelta(hours=1, minutes=30)
