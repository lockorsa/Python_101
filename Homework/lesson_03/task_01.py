"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(a: int, b: int) -> float:
    result = a / b
    return result


while True:
    a = input("Введите первое число\n >>> ")
    b = input("Введите второе число\n >>> ")
    if a.isdigit() and b.isdigit():
        a, b = int(a), int(b)
        break
    print("Ошибка, введите положительное число")


print(division(a, b))
