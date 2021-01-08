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


def search_for_min1(target_list):
    min_number = target_list[0]
    for number in target_list:
        if number < min_number:
            min_number = number
    return min_number


x = [2, 465, 9, 4, 1, 3]

y = search_for_min1(x)
print(y)


def search_for_min2(target_list):
    min_number = target_list[-1]
    for number in target_list:
        for again_number in target_list:
            if again_number < number and again_number < min_number:
                min_number = again_number
    return min_number


x = [2, 465, 9, 4, 1, 3]

y = search_for_min2(x)
print(y)
