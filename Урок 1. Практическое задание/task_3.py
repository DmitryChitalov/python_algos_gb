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

from typing import Dict

companies = {'fashion': 40000000, 'donCARLEON': 3090000, 'Lewon': 40300002,
             'Pasew': 302000900, 'GeoJ': 20030000, 'KeyCan': 400300200, 'JohnN': 6000400003,
             'LastProject': 300090000, 'Dollar': 9000030008, 'PopColt': 500000000000}

# Общая сложность О(n log n), т.к присутствует функция sort
def top_companies1(dct: Dict[str, int]):
    lst_comp = []
    lst_comp_values = []
    for j in dct.values():
        lst_comp_values.append(j)

    lst_comp_values.sort(reverse=True)                                      # O(n log n)

    for i in lst_comp_values[:3]:                                           # O(1)
        for k, v in dct.items():                                            # O(n)
            if v == i:
                lst_comp.append((k, v))

    print(lst_comp)

# Сложность также О(n log n), т.к используется функция sort
def top_companies2(dct: Dict[str, int]):
    a = sorted(dct.items(), key=lambda x: x[1], reverse=True)               # O(n log n)
    print(a[:3])

# Наиболее эффективное решение, общая сложность О(n)
def top_companies3(dct: Dict[str, int]):
    lst_comp = list(dct.items())
    tops = sorted(list(lst_comp[:3]), key=lambda x: x[1], reverse=True)     # O(3), т.к всегда 3 значения
    for el in lst_comp:                                                     # O(n)
        if el[1] < tops[2][1]:                                              # O(1)
            continue                                                        # O(1)
        elif tops[2][1] < el[1] < tops[1][1]:                               # O(1)
            tops[2] = el                                                    # O(1)
        elif tops[1][1] < el[1] < tops[0][1]:                               # O(1)
            tops[1], tops[2] = tops[2], tops[1]                             # O(1)
            tops[1] = el                                                    # O(1)
        elif el[1] > tops[0][1]:                                            # O(1)
            tops[1], tops[2] = tops[2], tops[1]                             # O(1)
            tops[0], tops[1] = tops[1], tops[0]                             # O(1)
            tops[0] = el                                                    # O(1)

    print(tops)


top_companies1(companies)
top_companies2(companies)
top_companies3(companies)
