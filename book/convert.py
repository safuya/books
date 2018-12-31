from datetime import timedelta


def time_to_pages(completed: timedelta, overall: timedelta, pages: int) -> float:
    return (completed / overall) * pages
