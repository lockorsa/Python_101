"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
    Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна.
    Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, weight, depth=1):
        return f'Масса асфальта составляет: {self._length * self._width * weight * depth}'


print('Проложим новую дорогу')
while True:
    user = input('Введите длинну, ширину и вес асфальта через пробел\n>>> ')
    if user.replace(' ', '').isdigit():
        if len(parameters := [int(i) for i in user.split()]) == 3:
            new_road = Road(parameters[0], parameters[1])
            print(new_road.calculate_mass(parameters[2]))
            break
        else:
            print('Ошибка ввода, больше или меньше 3 параметров, попробуйте еще раз')
    else:
        print('Ошибка ввода, не все значения числа, попробуйте еще раз')
