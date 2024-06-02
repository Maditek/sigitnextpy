def gen_secs():
    for sec in range(60):
        yield sec


def gen_minutes():
    for min in range(60):
        yield min


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02}:{minute:02}:{second:02}"


def gen_years(start=2019):
    while True:
        yield start
        start += 1


def gen_months():
    for month in range(12):
        yield month


def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if leap_year and month == 2:
        days = 29
    else:
        days = days_in_month[month]

    for day in range(1, days + 1):
        yield day


def gen_date(start_year=None):
    years_gen = gen_years(start_year)

    while True:
        year = next(years_gen)
        for month in range(1, 13):
            leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            days_gen = gen_days(month, leap_year)
            for day in days_gen:
                hours_gen = gen_hours()
                for hour in hours_gen:
                    minutes_gen = gen_minutes()
                    for minute in minutes_gen:
                        seconds_gen = gen_secs()
                        for second in seconds_gen:
                            yield f"{day:02}/{month:02}/{year} {hour:02}:{minute:02}:{second:02}"


date_gen = gen_date(2019)
for _ in range(100):
    print(next(date_gen))