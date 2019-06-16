from datetime import timedelta
from book import convert


def test_convert_time():
    completed = timedelta(hours=1, minutes=30, seconds=0)
    overall = timedelta(hours=3, minutes=0, seconds=0)
    result = convert.time_to_pages(completed, overall, pages=100)
    assert result == 50


def test_two_long_str_conversion():
    time = '01:02'
    assert convert.str_to_time(time) == timedelta(minutes=1, seconds=2)


def test_three_long_str_conversion():
    time = '1:2:3'
    assert convert.str_to_time(time) == timedelta(hours=1, minutes=2, seconds=3)
