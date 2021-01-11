"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк
"""

seconds = int(input('Введите значение в секундах\n >>> '))

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print('Часы, Минуты, Секунды - {0}:{1}:{2}'.format(hours, minutes, seconds))





