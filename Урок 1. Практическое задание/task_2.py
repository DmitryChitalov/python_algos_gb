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
from random import randrange

def get_min_value_with_quadratic_complexity(list_obj):
    for elem_1 in list_obj:
        is_min = True
        for elem_2 in list_obj:
            if elem_1 > elem_2:
                is_min = False
        if is_min:
            return elem_1


def get_min_value_with_linear_complexity(list_obj):
    min_value = list_obj[0]
    for num_elem in range(len(list_obj)):
        if list_obj[num_elem] < min_value:
            min_value = list_obj[num_elem]
    return min_value


if __name__ == '__main__':
    test_list = [randrange(100) for i in range(10)]
    print(test_list)
    min_test_list_1 = get_min_value_with_quadratic_complexity(test_list)
    print(min_test_list_1)
    min_test_list_2 = get_min_value_with_linear_complexity(test_list)
    print(min_test_list_2)
