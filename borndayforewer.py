"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def year_of_birth (year):
    while not (year == '1799'):
        print("Не верно")
        year = input('Ввведите год рождения А.С.Пушкина:')



def day_of_birth (day):
    while not (day == '6'):
        print("Не верно")
        day = input('В какой день июня родился Пушкин?')



year_of_birth(input('Ввведите год рождения А.С.Пушкина:'))
print('Верно')
day_of_birth(input('Ввведите день рождения Пушкин:'))
print('Верно')

