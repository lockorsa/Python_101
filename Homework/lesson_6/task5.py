"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки,')


class Pen(Stationery):

    def draw(self):
        print(f'** представьте звук пишущей ручки, {self.title} **')


class Pencil(Stationery):

    def draw(self):
        print(f'** представьте звук пишущего карандаша, {self.title} **')


class Handler(Stationery):

    def draw(self):
        print(f'** представьте звук пишущего маркера, {self.title} **')


my_stationery = Stationery('Абстракция')
my_stationery.draw()

my_pen = Pen('Шариковая ручка')
my_pen.draw()

my_pencil = Pencil('Обычный карандаш')
my_pencil.draw()

my_handler = Handler('Синий маркер')
my_handler.draw()
