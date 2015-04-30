class Calendar:
    def __init__(self, year=2015):
        self.year = year  # TODO get current year
        self.dates = []
        for month in range(1, 13):
            self.insert_dates(month)

    def insert_dates(self, month):
        days = 28
        if month in [1, 4, 6, 9, 11]:
            days = 30
        if month in [3, 5, 7, 8, 10, 12]:
            days = 31
        print days
        self.create_dates(days, month)

    def create_dates(self, days, month):
        for day in range(1, days + 1):
            date = Date(day=day, month=month)
            date.write_into(self.dates)


class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date


class BirthDate:
    def __init__(self, year, date):
        self.year = year
        self.date = date


class Date:
    def __init__(self, day, month):
        self.day = day
        self.month = month

    def write_into(self, list):
        list.append(self)
