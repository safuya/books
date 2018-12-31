from datetime import timedelta
from book import convert


def test_convert_time():
    completed = timedelta(hours=1, minutes=30)
    overall = timedelta(hours=3)
    result = convert.time_to_pages(completed, overall, pages=100)
    assert result == 50
