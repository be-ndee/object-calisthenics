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
