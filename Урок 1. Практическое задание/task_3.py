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


# O(n log n)
def top3(cmpn):
    sort_cmpn = sorted(cmpn.items(), key=lambda item: item[1], reverse=True)
    return sort_cmpn[:3]


# O(n)
def top3_2(cmpn):
    input_top3 = {}
    for i in range(3):
        val = max(cmpn.items(), key=lambda item: item[1])
        input_top3[val[0]] = val[1]
        del cmpn[val[0]]
    return input_top3


company = {'sber': 10010, 'vtb': 1200, 'tinkoff': 3000, 'alfa': 10400, 'bcs': 500}
print(top3(company))
print(top3_2(company))

# Второй вариант легче по сложности и без необходимости сортировки исходного словаря
