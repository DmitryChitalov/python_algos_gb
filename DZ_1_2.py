"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная."""

from random import randint


def Kvadratichnaya(lst1):  # Квадратичная сложность так как каждый
    # элемент списка проверяется с каждым другим элементом списка
    for el in lst1:
        min = True
        for i in lst1:
            if i < el:
                min = False
        if min:
            return el


def Lineynaya(lst2):  # Линейная так как цикл поочередно находит минимальное число.
    low = lst2[0]
    for el in lst2:
        if el < low:
            low = el
    return low


lst = []
while True:
    lst.append(randint(1, 100))
    if len(lst) > 10:
        break

print("Случайный набор чисел: " + " ".join(map(str, lst)))
print(Kvadratichnaya(lst))
print(Lineynaya(lst))
