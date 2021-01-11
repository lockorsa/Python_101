"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
while и арифметические операции
"""

user_int = int(input('Введите целое положительное чсло\n >>> '))

result = 0
while user_int and result != 9:
    tmp = user_int % 10
    if tmp > result:
        result = tmp
    user_int //= 10

print(result)



