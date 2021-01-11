"""4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.__speed = int(speed)                              # константа, private
        self.display_speed = 0                                 # изменяемый параметр, для использования в методах
        self.is_police = bool(is_police)
        print('С завода  выпущен новый экземпляр автомобиля')

    def move(self):
        self.display_speed = self.__speed
        print(f'{self.name} начал движение')

    def stop(self):
        self.display_speed = 0
        print(f'{self.name} остановился')

    def turn(self, direction: str):
        directions = {'left': 'лево', 'right': 'право', 'лево': 'лево', 'право': 'право'}
        if self.display_speed:
            if direction in directions:
                print(f'{self.name} повернул в{directions[direction]}')
            else:
                print(f'Невозможно повернуть в {direction}')
        else:
            print(f'{self.name} стоит на месте, повернуть невозможно')

    def show_speed(self):
        if self.display_speed:
            print(f'Скорость {self.name} составляет: {self.display_speed} км/ч')
        else:
            print(f'{self.name} припаркован, скорость: 0 км/ч')

    def check_is_police(self):
        if self.is_police:
            print(f'{self.name} зарегистрирован на государственные правоохранительные органы')
        else:
            print(f'{self.name} зарегистрирован на гражданское лицо')


class SportCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        self.is_police = True


class TownCar(Car):

    def show_speed(self):
        if self.display_speed:
            print(f'Скорость {self.name} составляет: {self.display_speed} км/ч')
            if self.display_speed > 60:
                print(f'Вы превысили скорость на {self.display_speed - 60} км/ч')
        else:
            print(f'{self.name} припаркован, скорость: 0 км/ч')


class WorkCar(Car):

    def show_speed(self):
        if self.display_speed:
            print(f'Скорость {self.name} составляет: {self.display_speed} км/ч')
            if self.display_speed > 40:
                print(f'Вы превысили скорость на {self.display_speed - 40} км/ч')
        else:
            print(f'{self.name} припаркован, скорость: 0 км/ч')


print('Поиграемся с экземплярами классов')

my_car = PoliceCar('Ласточка', 'white', 110, 1)
print(my_car.display_speed)
my_car.move()
print(my_car.display_speed)
my_car.check_is_police()
my_car.stop()
my_car.turn('лево')
my_car.move()
my_car.turn('right')
my_car.show_speed()


my_car = WorkCar('Автобус', 'white', 70, 0)
print(my_car.display_speed)
my_car.move()
print(my_car.display_speed)
my_car.check_is_police()
my_car.stop()
my_car.turn('лево')
my_car.move()
my_car.turn('right')
my_car.show_speed()

