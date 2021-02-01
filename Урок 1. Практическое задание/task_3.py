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
import random
from heapq import nlargest


# O(n)
def get_three_largest_1(companies_lst, profits_lst):
    return nlargest(3, zip(profits_lst, companies_lst))


# O(n*logn)
# самое неэффективное
def get_three_largest_2(companies_lst, profits_lst):
    return sorted(zip(profits_lst, companies_lst), reverse=True)[:3]


# companies names only
# O(n)
def get_three_largest_3(companies_lst, profits_lst):
    target = dict(zip(profits_lst, companies_lst))
    result = []
    for i in range(3):
        cur_max = max(target.keys())
        result.append(target.pop(cur_max))
    return result


companies = list('ABCDEFGH')
profits = random.sample(range(-100000, 100000), len(companies))
print(companies)
print(profits)
print(get_three_largest_1(companies, profits))
print(get_three_largest_2(companies, profits))
print(get_three_largest_3(companies, profits))

""" варианты 1 и 3 сравнимы по эффективности """
