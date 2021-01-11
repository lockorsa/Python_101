"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""


def my_sum(*args: int) -> int:
    """ Моя собственная функция сложения

    :param args: числа
    :return: сумма всех аргументов
    """
    result = 0
    for el in args:
        result += el
    return result


def my_func(a: int, b: int, c: int) -> int:
    """Функция для вычисления суммы двух самых больших аргументов
    Элегантное-релевантное решение в одну строку
    :return: int
    """
    return my_sum(a, b, c) - min(a, b, c)


print(my_func(1, 2, 3))
print(my_func(2, 3, 1))
print(my_func(3, 1, 2))
print(my_func(3, 2, 1))
print(my_func(8, 6, 6))
print(my_func(8, 8, 6))
