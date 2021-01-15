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

import operator

"""
Задача, к сожалению не доделана в силу дефецита времени, 
но так мне понравилось элеганное первое решение, что не смог не запостить.
"""

company_dict = {'Kopor': 1033,
                'Kirish': 800,
                'SZt': 870,
                'PskG': 0,
                'Kal_TES': 900,
                'Kilingi-Nim': 640}

"""
Хороший вариант, чёткий, по питоновски.
Сложность, за счёт sorted, O(n log n)
"""


def top_comp_1(company_dict):  # O(n log n)
    return sorted(company_dict.items(), key=operator.itemgetter(1), reverse=True)[:3]


print(top_comp_1(company_dict))

"""
Вариант — O(N^2) — квадратичная сложность
"""

def top_comp_2(comp_dict):
    for i in range(len(comp_dict)):
        lowest_value_index = i
        for j in range(i + 1, len(comp_dict)):
            if comp_dict[j][1] > comp_dict[lowest_value_index][1]:
                lowest_value_index = j
        comp_dict[i], comp_dict[lowest_value_index] = comp_dict[lowest_value_index], comp_dict[i]
    return comp_dict[0:3]


list_from_comp_dict = list(company_dict.items())
highest_value = {}
for i in top_comp_2(list_from_comp_dict):
    print(i[0], ':', i[1], end='; ')

print()


"""
Вариант — O(N) — линейная сложность
The winner is — top_comp_3 func!
"""

def top_comp_3(comp_dict):
    highest_value = {}
    list_comp = dict(comp_dict)
    for i in range (3):
        find_highest = max(list_comp.items(), key=lambda value: value[1])
        del list_comp[find_highest[0]]
        highest_value[find_highest[0]] = find_highest[1]
    return highest_value


print(top_comp_3(company_dict))