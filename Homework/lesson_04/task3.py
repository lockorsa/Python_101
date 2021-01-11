"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

result = []                                        #решение через цикл
for number in range(20, 241, 20):
    result.append(number)
print(result)


result2 = [num for num in range(20, 241, 20)]      #решение в одну строку через list comprehension
print(result2)