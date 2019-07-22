import os
from book import logging
from pathlib import Path


def test_log_is_named_correctly():
    assert logging.log(path='tests').name == 'Book'


def test_log_location():
    if Path(Path.cwd() / 'tests' / '.audio2book.log').exists():
        os.remove(Path.cwd() / 'tests' / '.audio2book.log')

    log = logging.log(path='tests')
    log.info('Hi')

    assert Path(Path.cwd() / 'tests' / '.audio2book.log').exists()
