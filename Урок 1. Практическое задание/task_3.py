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
import operator

companies = {"Company1": round(random.uniform(10000, 500000), 2),
             "Company2": round(random.uniform(10000, 500000), 2),
             "Company3": round(random.uniform(10000, 500000), 2),
             "Company4": round(random.uniform(10000, 500000), 2),
             "Company5": round(random.uniform(10000, 500000), 2),
             "Company6": round(random.uniform(10000, 500000), 2),
             "Company7": round(random.uniform(10000, 500000), 2)
             }


# Этот вариант самый эффективный
# только одна дорогостоящая операция поиска max в словаре.
# предполагаю, что сложность внутри функции max O(n). Не нашел в таблице
# Итовая сложность O (3N)
def profit1(company_profit_dict):
    pass
    my_profit_dict = dict(company_profit_dict)  # O(1)
    result_profit_list = []  # O(1)
    print(company_profit_dict)
    for _ in range(3):  # O (3)
        maxprofit_company = max(my_profit_dict.items(), key=operator.itemgetter(1))[0]  # O(N)
        result_profit_list.append(maxprofit_company)  # O(1)
        my_profit_dict.pop(maxprofit_company)  # O(1)
        return result_profit_list


# Итоговая сложность O(3N + N^2)
def profit_2(company_profit_dict):
    profit_storage = []
    for _ in range(3):
        max_profit = 0
        for val in company_profit_dict.values():
            if val > max_profit and val not in profit_storage:
                max_profit = val
        profit_storage.append(max_profit)

    for key in company_profit_dict.keys():
        for i in profit_storage:
            if company_profit_dict[key] == i:
                print(f'{key}, {company_profit_dict[key]}')


res1 = profit1(companies)
print(res1)
