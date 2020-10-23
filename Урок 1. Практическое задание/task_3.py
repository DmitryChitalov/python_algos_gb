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
storage = {'company1': 1000, 'company2': 200, 'company3': 500, 'company4': 12, 'company5': 10000}
""" 
Варианты 1 и 2 имеют одинаковую сложность, но второй вариант боле предпочтителен из-за лаконичности и отсутствия
необходимости создания промежуточного списка.
Вариант 3 имеет худшую сложность, и сложнее для восприятия
"""


# Решение 1. Сложность: O(n*log n)
def sort_by_profit1(some_dict):
    companies_lst = some_dict.items()  # O(n)
    companies_three_richest = sorted(companies_lst, key=lambda x: x[1], reverse=True)[:3]  # O(n*log n) + O(n)
    most_profitable = []  # O(1)
    for el in companies_three_richest:  # O(n)
        most_profitable.append(el[0])  # O(1)
    return most_profitable


print(f'Три самых прибыльных компании: {sort_by_profit1(storage)}')


# Решение 2. Сложность: O(n*log n)
def sort_by_profit2(some_dict):
    companies_lst = sorted(some_dict.items(), key=lambda x: x[1], reverse=True)  # O(n*log n)
    companies_three_richest = [(name, profit) for (name, profit) in companies_lst][:3]  # O(n) + O(n)
    return [el[0] for el in companies_three_richest]  # O(1) + O(n)


print(f'Три самых прибыльных компании: {sort_by_profit2(storage)}')


# Решение 3. Сложность: O(n^2)
def sort_by_profit3(some_dict):
    profits = []
    for name, profit in some_dict.items():
        profits.append(some_dict[name])  # O(n)
    profits.sort(reverse=True)  # O(n*log(n)) - sorting
    profits = profits[:3]  # O(n) - slice
    most_profitable = []  # O(n)
    for el in profits:  # O(n^2)
        for name, profit in some_dict.items():
            if profit == el:
                most_profitable.append(name)  # O(n)
    return most_profitable


print(f'Три самых прибыльных компании: {sort_by_profit3(storage)}')
