"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
from random import random


def dict_init(dict_size):
    start = 100
    dictionary = {f"Company_{a}": int((a + start) ** 2.2) for a in range(dict_size)}
    return dictionary


## Сложность кода O(n^2)
def get_rich_company(dictionary) -> int:
    dict_value = 0  # O(1)
    for dict_key in dictionary.keys():  # O(n)
        if dictionary.get(dict_key) > dict_value:  # O(n)
            dict_value = dictionary.get(dict_key)  # O(1)

    return dict_value


## Добились линейной сложности
def get_rich_company2(dictionary) -> int:
    return max(dictionary.values())  # O(n)


v_dictionary = dict_init(5)
print(f"Dictionary: {v_dictionary}")

## Первый вариант
rich_company = get_rich_company(v_dictionary)
print(f"The richest company has ${rich_company} budget!")

## Второй вариант
rich_company2 = get_rich_company2(v_dictionary)
print(f"The richest company has ${rich_company2} budget!")
