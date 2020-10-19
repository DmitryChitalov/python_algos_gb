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


# Realization from lesson2 O(n^2)

def search_min_value(lst: list) -> int:
    for el1 in lst:
        is_min = True
        for el2 in lst:
            if el1 < el2:
                is_min = False
        if is_min:
            return el1


'''
My realization O(n^2) 
Не смог заврешить реализацию квадратичнной сложности.
Похоже что что-то перемудрил)
'''


def search_min_value_version2(lst: list) -> int:
    min_value = True

    while min_value:
        for i in lst:
            for j in lst:
                if i < j:
                    i, j = j, i
                    min_value = False
            if min_value:
                return i

# Realization O(n) такой варинат делал на основах питона или на check.io точно не скажу.
def search_min_value_version3(lst: list) -> int:
    min_value = lst[0]
    for i in lst:
        if min_value > i:
            min_value = i
    return min_value

