"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user = input("Введите слова через пробел\n>>> ").split()

for idx, word in enumerate(user):
    print(idx + 1, word)
