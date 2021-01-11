"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""


#user = input("Введите символы через пробел \n >>> ").split()
user = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def swap(array: list) -> list:

    result = []
    for i, el in enumerate(array):
        try:
            if i == len(array) + 1:
                result.append(el)
            elif i % 2 == 0:
                result.append(array[i + 1])
            elif i % 2 == 1:
                result.append(array[i - 1])
        except IndexError:
            result.append(el)
    return result

print(swap(user))


idx = 0
break_point = len(user) - 1
while idx < break_point:
    user[idx], user[idx + 1] = user[idx + 1], user[idx]
    idx += 2

print(user)
