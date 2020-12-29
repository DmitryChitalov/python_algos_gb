"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для
списка. В основе алгоритма должно быть сравнение каждого числа со всеми
другими элементами списка. Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для
списка. Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
from random import randint

my_list = [randint(1, 5000) for i in range(1000)]


def search_min_number_v1(list):  # O(n)
    min = list[0]
    for source_number in range(1, len(list)):
        if list[source_number] < min:
            min = list[source_number]

    return min


def search_min_number_v2(list):  # O(1)
    return min(list)


def search_min_number_v3(list):  # O(n**2)
    for source_number in range(len(list)):
        for target_number in range(source_number + 1,
                                   len(list)):
            if list[source_number] < list[target_number]:
                list[source_number], list[target_number] = \
                    list[target_number], list[source_number]
    return list[-1]


def test():
    print('v1 OK' if search_min_number_v1([1, 2, 3, 4, 5]) == 1 else 'v1 FAIL')
    print('v1 OK' if search_min_number_v1(
        [100, 200, 300, 400]) == 100 else 'v1 FAIL')
    print('v1 OK' if search_min_number_v1(
        [2.5, 3.6, 50.8, 1.65, 1.64]) == 1.64 else 'v1 FAIL')
    print('v2 OK' if search_min_number_v2([1, 2, 3, 4, 5]) == 1 else 'v2 FAIL')
    print('v2 OK' if search_min_number_v2(
        [100, 200, 300, 400]) == 100 else 'v2 FAIL')
    print('v2 OK' if search_min_number_v2(
        [2.5, 3.6, 50.8, 1.65, 1.64]) == 1.64 else 'v2 FAIL')
    print('v3 OK' if search_min_number_v3([1, 2, 3, 4, 5]) == 1 else 'v3 FAIL')
    print('v3 OK' if search_min_number_v3(
        [100, 200, 300, 400]) == 100 else 'v3 FAIL')
    print('v3 OK' if search_min_number_v3(
        [2.5, 3.6, 50.8, 1.65, 1.64]) == 1.64 else 'v3 FAIL')


# test()

print(search_min_number_v1(my_list))
print(search_min_number_v2(my_list))
print(search_min_number_v3(my_list))
