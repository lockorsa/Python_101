"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(name, lastname, dob, city, email, phone):
    result = f'{name}, {lastname}, {dob}, {city}, {email}, {phone}'
    return result

print(user_data(name="Саня", lastname="Иванов", dob="01.01.1488", city="Мухосрань", email="mail@mail.com", phone=12345))