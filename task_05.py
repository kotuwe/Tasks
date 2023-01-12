from datetime import timedelta, datetime


def date_in_future(integer):
    if isinstance(integer, int):
        any_day = datetime.now() + timedelta(days=integer)
        return any_day.strftime("%d-%m-%Y %H:%M:%S")
    else:
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


print(date_in_future([]))       # => текущая дата
print(date_in_future(2))        # => текущая дата + 2 дня