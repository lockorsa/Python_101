"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».

В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год ипреобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).

Проверить работу полученной структуры на реальных данных."""


class Date:

    def __init__(self, data: str):
        if len([i for i in data.split('-')]) == 3:
            self.data = data
        else:
            raise ValueError('Not enough values to initialize object')

    def __str__(self):
        return f"Day: {self.data.split('-')[0]}, Month: {self.data.split('-')[1]}, Year: {self.data.split('-')[2]}"

    @classmethod
    def reformat_date(cls, data):
        return [int(i) for i in data.split('-')]

    @staticmethod
    def is_valid_date(data):
        data = [int(i) for i in data.split('-')]                                   # только даты нашей эры до 9999 года
        if 1 <= data[0] <= 31 and 1 <= data[1] <= 12 and 1 <= data[2] <= 9999:     # поверхностная проверка
            return True
        else:
            return False


if __name__ == '__main__':
    date1 = Date('06-10-2000')
    date2 = Date('23-08-1220')
    date3 = Date('15-01-8030')
    date4 = Date('65-08-1220')
    date5 = Date('23-89-1220')
    print(date1)
    print(date2)
    print(date3)
    print(date4)
    print(date5)
    print(Date.is_valid_date('06-10-2000'))
    print(Date.is_valid_date('23-08-1220'))
    print(Date.is_valid_date('15-01-8030'))
    print(Date.is_valid_date('65-08-1220'))
    print(Date.is_valid_date('23-89-1220'))

    print(Date.reformat_date('23-08-1220'))       # какой-то бесполезный метод получился имхо
    print(Date.reformat_date('65-08-1220'))
