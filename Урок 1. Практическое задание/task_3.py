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
from random import randint


# 1: O(n^2)
def top3_v1(companies_dict):
    companies_list = list(companies_dict.items())
    for i in range(len(companies_list)):
        min_value_index = i
        for j in range(i + 1, len(companies_list)):
            if companies_list[j][1] > companies_list[min_value_index][1]:
                min_value_index = j
        companies_list[i], companies_list[min_value_index] = \
            companies_list[min_value_index], companies_list[i]
    return dict(companies_list[0:3])


# 2: O(n log n)
def top3_v2(companies_dict):
    companies_list = list(companies_dict.items())
    companies_list.sort(key=lambda i: i[1], reverse=True)
    return dict(companies_list[0:3])


# 3: O(n)
def top3_v3(companies_dict):
    top3_dict = {}
    list_d = dict(companies_dict)
    for i in range(3):
        max_value = max(list_d.items(), key=lambda j: j[1])
        del list_d[max_value[0]]
        top3_dict[max_value[0]] = max_value[1]
    return top3_dict


# check:
companies_dict_example = {f'Company_{i}': i * randint(0, 1000) for i in range(10)}
print(f'Словарь команий: {companies_dict_example}\n'
      f'ТОП-3, вариант 1: {top3_v1(companies_dict_example)}\n'
      f'ТОП-3, вариант 2:{top3_v2(companies_dict_example)}\n'
      f'ТОП-3, вариант 2:{top3_v3(companies_dict_example)}')
