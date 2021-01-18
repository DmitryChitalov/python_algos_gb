"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

from random import randint

#O(n^2)
def smallestElement(list):
    for i in list:
        smallest = True
        for j in list:
            if i > j:
                smallest = False
        if smallest:
            return i      


list = [randint(1, 50) for x in range(10)]
print(list)
print(smallestElement(list))

#O(n)
def smallestElement1(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest


list1 = [randint(1, 50) for x in range(10)]

print(list1)
print(smallestElement1(list1))
