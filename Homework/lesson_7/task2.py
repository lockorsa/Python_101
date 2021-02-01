"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма).

Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property."""
from abc import abstractmethod


class Cloth:

    @abstractmethod
    def calculate_expence(self):
        pass


class Coat(Cloth):

    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def calculate_expence(self):
        resource = (self.size / 6.5 + 0.5)
        return f'На вышивку {self.name}, необходимо {int(resource)} ткани'


class Costume(Cloth):

    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def calculate_expence(self):
        resource = (2 * self.height + 0.3)
        return f'На вышивку {self.name}, необходимо {int(resource)} ткани'


if __name__ == '__main__':
    my_coat = Coat('черный плащ', 250)
    print(my_coat.calculate_expence)

    my_costume = Costume('костюм тройка', 190)
    print(my_costume.calculate_expence)
