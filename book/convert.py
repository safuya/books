from datetime import timedelta


def time_to_pages(completed: timedelta, overall: timedelta, pages: int) -> float:
    return (completed / overall) * pages


def str_to_time(time: str) -> timedelta:
    hours, minutes = map(lambda x: float(x), time.split(':'))
    return timedelta(hours=hours, minutes=minutes)


def run(completed: str, overall: str, pages: int):
    completed_td = str_to_time(time=completed)
    overall_td = str_to_time(time=overall)
    return time_to_pages(completed_td, overall_td, pages)
