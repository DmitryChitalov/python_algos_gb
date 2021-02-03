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

company = {"test0": 5657, "tes1": 100, "test2": 556, "test3": 123, "test4": 3949, "test5": 63534543}
max_companys = 3


def method1(comp_dict, m):
    company_list = []
    price_list = []
    result_company = []
    for i in comp_dict.values():
        price_list.append(i)
    for i in comp_dict.keys():
        company_list.append(i)
    for i in range(m):
        a = max(price_list)
        index = price_list.index(a)
        result_company.append(company_list[index])
        price_list.remove(a)
        company_list.remove(company_list[index])

    print(result_company)


def method2(comp_dict, m):
    h = sorted(comp_dict, key=comp_dict.get, reverse=True)[:m]
    print(h)


method1(company, max_companys)  # O(n^2)
method2(company, max_companys)  # O(n log n ) - самый дешевый вариант т.к. меньше чем O(n^2)
