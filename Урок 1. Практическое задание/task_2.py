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

list_of_numbers = [7, 3, 8, 1, 11, 2, 37, 23]


def find_min_number_first(input_list):
    for item in input_list:
        flag = True
        for i in input_list:
            if i < item:
                flag = False
        if flag:
            return item


def find_min_number_second(input_list):
    minimum = input_list[0]
    for item in input_list[1:]:
        if item < minimum:
            minimum = item
    return minimum


print(find_min_number_first(list_of_numbers))
print(find_min_number_second(list_of_numbers))
