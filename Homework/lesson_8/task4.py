""" Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП."""
from abc import abstractmethod


class Storage:
    __INVENTORY = {'computer': [], 'printer': [], 'cooler': []}

    @staticmethod
    def collect(tech_type, serial):
        Storage.__INVENTORY[tech_type].append(serial)

    @staticmethod
    def send_to_office(tech_type, serial):
        Office.collect(tech_type, serial)
        idx = Storage.__INVENTORY[tech_type].index(serial)
        del Storage.__INVENTORY[tech_type][idx]

    @staticmethod
    def send_all_to_office():
        [Office.collect('computer', serial) for serial in Storage.__INVENTORY['computer']]
        [Office.collect('printer', serial) for serial in Storage.__INVENTORY['printer']]
        [Office.collect('cooler', serial) for serial in Storage.__INVENTORY['cooler']]
        Storage.__INVENTORY["computer"].clear()
        Storage.__INVENTORY["printer"].clear()
        Storage.__INVENTORY["cooler"].clear()
        print('Вся техника со склада направлена в офис')

    @staticmethod
    def check_inventory():
        print(f'На складе находится: '
              f'{len(Storage.__INVENTORY["computer"])} - компьютеров, '
              f'{len(Storage.__INVENTORY["printer"])} - принтеров, '
              f'{len(Storage.__INVENTORY["cooler"])} - кулеров')

    @staticmethod
    def item_exist(tech_type, serial):
        return serial in Storage.__INVENTORY[tech_type]


class Office:                                      # офис является самостоятельным классом, не наследуется от склада
    __INVENTORY = {'computer': [], 'printer': [], 'cooler': []}

    @staticmethod
    def collect(tech_type, serial):
        Office.__INVENTORY[tech_type].append(serial)

    @staticmethod
    def send_to_storage(tech_type, serial):
        Storage.collect(tech_type, serial)
        idx = Office.__INVENTORY[tech_type].index(serial)
        del Office.__INVENTORY[tech_type][idx]

    @staticmethod
    def send_all_to_storage():
        [Storage.collect('computer', serial) for serial in Office.__INVENTORY['computer']]
        [Storage.collect('printer', serial) for serial in Office.__INVENTORY['printer']]
        [Storage.collect('cooler', serial) for serial in Office.__INVENTORY['cooler']]
        Office.__INVENTORY["computer"].clear()
        Office.__INVENTORY["printer"].clear()
        Office.__INVENTORY["cooler"].clear()
        print('Вся техника из офиса направлена на склад')

    @staticmethod
    def check_inventory():
        print(f'Офис укомплектован следующей техникой: '
              f'{len(Office.__INVENTORY["computer"])} - компьютеров, '
              f'{len(Office.__INVENTORY["printer"])} - принтеров, '
              f'{len(Office.__INVENTORY["cooler"])} - кулеров')

    @staticmethod
    def item_exist(tech_type, serial):
        return serial in Office.__INVENTORY[tech_type]


class Tech:
    @abstractmethod
    def __init__(self, serial):
        self.serial = serial
        self.tech_type = 'None'

    def __str__(self):
        return f'{self.serial}'

    def delivery(self):
        if Storage.item_exist(self.tech_type, self.serial):
            Storage.send_to_office(self.tech_type, self.serial)
            print('Статус: доставлен в филиал')
        elif Office.item_exist(self.tech_type, self.serial):
            Office.send_to_storage(self.tech_type, self.serial)
            print('Статус: доставлен на склад')
        else:
            print('Данный предмет не обнаружен ни в одной инстанции')


class Computer(Tech):
    def __init__(self, serial):
        super().__init__(serial)
        self.tech_type = 'computer'
        Storage.collect(self.tech_type, serial)

    @staticmethod
    def action():
        print('* sending emails... *')


class Printer(Tech):
    def __init__(self, serial):
        super().__init__(serial)
        self.tech_type = 'printer'
        Storage.collect(self.tech_type, serial)

    @staticmethod
    def action():
        print('* printing text file... *')


class WaterCooler(Tech):
    def __init__(self, serial):
        super().__init__(serial)
        self.tech_type = 'cooler'
        Storage.collect(self.tech_type, serial)

    @staticmethod
    def action():
        print('* brr brr water supply... *')


if __name__ == '__main__':
    pc1 = Computer('pc11111')
    pc2 = Computer('pc22222')
    pc3 = Computer('pc33333')
    printer1 = Printer('sc44444')
    printer2 = Printer('sc55555')
    printer3 = Printer('sc66666')
    cooler1 = WaterCooler('wc77777')
    cooler2 = WaterCooler('wc88888')
    cooler3 = WaterCooler('wc99999')

    pc1.delivery()
    cooler1.delivery()
    Storage.check_inventory()
    Office.check_inventory()
    Storage.send_all_to_office()
    Storage.check_inventory()
    Office.check_inventory()

    print(pc1, pc2, pc3, printer1, cooler1)               # __str__
    pc1.action()
    printer1.action()
    cooler1.action()
