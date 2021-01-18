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
import random


def search_min_number(list_search):
    """
    Поиск минимального значения в списке при помощи сравнения
    каждого числа списка со всеми другими.

    :param list_search:
    :return:
    """
    min_number = list_search[0]
    for i in list_search:
        for j in list_search:
            if i <= min_number and i <= j:
                min_number = i
    return min_number



def search_min_number2 (list_search):
    """
    Поиск минимального значения для списка
    :param list_search:
    :return:
    """
    return min(list_search)

list_number = [random.randint(0, 100) for i in range(random.randint(0, 100))]
min_numbers = search_min_number(list_number)
min_numbers2 = search_min_number2(list_number)
print(list_number)
print(min_numbers)
print(min_numbers2)
