
class DataError(Exception):

    def __init__(self, text):
        self.text = text


class Data():

    def __init__(self, string):
        day, mounth, year = self.convert(string)

        self.day = day
        self.mounth = mounth
        self.year = year

    @classmethod
    def convert(cls, string):
        day, mounth, year = [int(d) for d in string.split('-')]

        cls.validate(day, mounth, year)

        return day, mounth, year

    @staticmethod
    def validate(day, mounth, year):

        if day < 1 or day > 31:
            raise DataError('Value Erorr: День должен быть от 1 до 31!')

        if mounth < 1 or mounth > 12:
            raise DataError('Value Erorr: Месяц должен быть от 1 до 12!')


data = Data(input('Введите дату (день-месяц-год): '))
