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


def min_element_from_list_1(user_list):
    """
    поиск минимального числа из списка путем сравнения каждого числа с каждым,
    Сложность: O(n**2)
    """
    for el in user_list:
        for idx in range(1, len(user_list)):
            if el < user_list[idx]:
                res = el
            else:
                res = user_list[idx]
            el = res
    return res


def min_element_from_list_2(user_list):
    """
    поиск минимального числа из списка путем сравнения парами,
    сложность: O(n)
    """
    min_element = user_list[0]
    for element in user_list:
        if element < min_element:
            min_element = element
    return min_element


def min_element_from_list_3(user_list):
    """
    поиск минимального числа из списка путем сортировки и выбора первого элемента у отсортированного списка,
    Сложность: O(n log n)
    """
    user_list.sort()
    return user_list[0]

# Тестируем на списке, список создаем через генератор

list_1 = [randint(1, 1000) for i in range(100)]
print(list_1)

print(f'Первый алгоритм: {min_element_from_list_1(list_1)}')
print(f'Второй алгоритм: {min_element_from_list_2(list_1)}')
print(f'Третий алгоритм: {min_element_from_list_3(list_1)}')
#print(min_element_from_list_2(list_1))
#print(min_element_from_list_3(list_1))
#print(min_element_from_list_4(list_1))