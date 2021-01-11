"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режим: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод."""
from time import sleep


class TrafficLight:
    __color = 'красный'

    def switch_light(self):
        alert = f'Сигнал светофора: {self.__color}'
        if self.__color == 'красный':
            self.__color = 'желтый'
            print(alert)
            sleep(7)
        elif self.__color == 'желтый':
            self.__color = 'зелёный'
            print(alert)
            sleep(2)
        elif self.__color == 'зелёный':
            self.__color = 'красный'
            print(alert)
            sleep(5)


my_tl = TrafficLight()

while True:
    my_tl.switch_light()

    user = input('q - для выхода, enter - продолжить\n> ')
    if user == 'q':
        break

