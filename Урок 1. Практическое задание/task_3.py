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


def best_company_1(company: dict, k: int) -> list:
    company_lst = [itm for itm in company.items()]
    for i in range(len(company_lst)):
        for j in range(len(company_lst)):
            if company_lst[i][1] > company_lst[j][1]:
                company_lst[i], company_lst[j] = company_lst[j], company_lst[i]
    return company_lst[0: k]  # O(N^2)


def best_company_2(company: dict, k: int) -> list:
    result = []
    comply_lst = [itm for itm in company.items()]
    for n in range(k):
        min_itm = comply_lst[0]
        for i in range(1, len(comply_lst)):
            if comply_lst[i][1] > min_itm[1]:
                min_itm = comply_lst[i]
        result.append(min_itm)
        comply_lst.remove(min_itm)
    return result  # O(k*N)


def best_company_3(company: dict, k: int) -> list:
    company_sorted = [(i, company[i]) for i in sorted(company, key=company.get, reverse=True)]
    return company_sorted[0: k]  # O(NlogN)


""" Эффективнее будет третья функция, использующая стандартные средства языка, она быстрее и требует меньше ресурсов """

comp_key = [chr(random.randint(97, 122)) for j in range(10)]
for j in range(10):
    comp_value = random.sample(range(-100000, 100000), j)
company = dict(zip(comp_key, comp_value))

print(best_company_1(company, 3))
print(best_company_2(company, 3))
print(best_company_3(company, 3))
