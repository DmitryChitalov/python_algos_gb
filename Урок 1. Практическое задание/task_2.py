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


def user_min_square(in_lst):
    if not in_lst:
        raise ValueError('List is empty')
    min_val = tmp_min_val = in_lst[0]
    for i in in_lst:
        for j in in_lst:
            if i < j:
                tmp_min_val = i
        if tmp_min_val < min_val:
            min_val = tmp_min_val
    return min_val


def user_min_linear(in_lst):
    if not in_lst:
        raise ValueError('List is empty')
    min_val = in_lst[0]
    for i in in_lst:
        if i < min_val:
            min_val = i
    return min_val


if __name__ == '__main__':

    lst = [random.randint(0, 100) for _ in range(10)]
    print(f' min value is: {user_min_square(lst)}')
    print(f' min value is: {user_min_linear(lst)}')
    print(f' min value is: {user_min_linear([])}')
