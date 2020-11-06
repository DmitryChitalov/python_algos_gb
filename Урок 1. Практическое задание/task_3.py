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


#Решение 1:
"""
Сложность O(2N^2)
"""

def company_searcher(any_dict):
    company_name = []
    maximum = []
    bigest_companies = []
    for i in any_dict.values():
        company_name.append(i)
    for j in [1, 2, 3]:
        maximum.append(max(company_name))
        company_name.remove(max(company_name))
    for i in maximum:
        for k, v in any_dict.items():
            if v == i:
                bigest_companies.append(k)
    return bigest_companies



company_vault = {
    'Ikea': 20000,
    'VK': 100000,
    'Games Workshop': 5000,
    'National Geographic': 3000,
    'Завод консервных банок': 1000
}


printer = company_searcher(company_vault)
print(printer)

#решение 2:
"""
Сложность: 0(N^2)
"""

def company_maximum(any_dict):
    company = []
    bigest_companies_values = []
    top_companies = []
    for i in any_dict.values():
        company.append(i)
    d = 0
    while d != 3:
        bigest_companies_values.append(max(company))
        company.remove(max(company))
        d = d+1
    print(bigest_companies_values)
    for k, v in any_dict.items():
            if v in bigest_companies_values:
                top_companies.append(k)
    return top_companies



printer = company_maximum(company_vault)
print(printer)

"""
Эффективнее второе решение, так как оно менее сложное. Однако, и оно не очень хорошее 
из-за большого количества переменных.
"""