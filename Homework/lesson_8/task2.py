"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой."""


class MyDivisionError(Exception):

    def __init__(self, alert=""):
        self.alert = alert


if __name__ == '__main__':

    def division(x,y):
        if y != 0 and x != 0:
            return x / y
        else:
            raise MyDivisionError('пытаетесь делить на ноль')


    while True:
        user = input('Веедите делимое и делитель через пробел, enter для завершения\n>>>')
        if user:
            try:
                user1, user2 = [int(i) for i in user.split()]
                print(division(user1, user2))
            except ValueError as e:
                print(e)
                continue
        else:
            break
