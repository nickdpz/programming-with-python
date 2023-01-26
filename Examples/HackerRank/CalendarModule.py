import calendar
from datetime import datetime


def getWeekDay(s: str) -> str:
    # Write your code here
    datetime_object = datetime.strptime(s, '%m %d %Y')
    return calendar.day_name[
        calendar.weekday(datetime_object.year,
                         datetime_object.month, datetime_object.day)
    ].upper()


if __name__ == '__main__':
    n = str(input().strip())
    res = getWeekDay(n)
    print(res)
