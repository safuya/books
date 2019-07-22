from pathlib import Path
from logbook import Logger, RotatingFileHandler


RotatingFileHandler(Path.home() / '.audio2book.log').push_application()
log = Logger('Book')
