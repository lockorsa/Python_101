"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name.title()} {self.surname.title()}\nЗанимает должность: {self.position}'

    def get_total_income(self):
        result = self._income['wage'] + self._income['bonus']
        return f'Зарплата сотрудника составляет: {result}'


print('Создадим новый экземпляр класса')
while True:
    user = input('Введите  данные через пробел: имя, фамилия, должность, оклад и премия\n>>> ').split(' ')
    if len(user) == 5:
        if user[0].isalpha() and user[1].isalpha() and user[2].isalpha() and user[3].isdigit() and user[4].isdigit():
            example_position = Position(user[0], user[1], user[2], user[3], user[4])
            break
        else:
            print('Ошибка ввода, цифры или буквы переданы в неправильном порядке')
    else:
        print('Ошибка ввода, недостаточно значений')

print(example_position.get_full_name())
print(example_position.get_total_income())


