"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import defaultdict


def four_quarters_profit():
    profit = input('Введите прибыль данного предприятия поквартально через пробел (4 значения): ').split(' ')
    if len(profit) != 4:
        raise Exception('Ошибка ввода, должно быть четыре значения')
    profit = [int(el) for el in profit]
    return profit


def filling_dict(dictionary):
    n = int(input('Введите число предприятий для расчета прибыли: '))
    for i in range(1, n + 1):
        dictionary[input(f'Введите название {i}-го предприятия: ')]
    return dictionary


def get_sum_profit(companies):
    profits = []
    for el in companies.values():
        profits.extend(el)
    full_profit = round(sum(profits) / len(companies.keys()), 2)
    return full_profit


def get_lower_profit(companies, full_profit=get_sum_profit):
    lower = []
    for k, v in companies.items():
        if sum(v) < full_profit(companies):
            lower.append(k)
    return lower


def get_higher_profit(companies, full_profit=get_sum_profit):
    higher = []
    for k, v in companies.items():
        if sum(v) > full_profit(companies):
            higher.append(k)
    return higher


companies_data = defaultdict(four_quarters_profit)
filling_dict(companies_data)

print(f'Средняя годовая прибыль всех предприятий: {get_sum_profit(companies_data)}')
print(f'Список предприятий с прибылью ниже среднего значения: {get_lower_profit(companies_data)}')
print(f'Список предприятий с прибылью выше среднего значения: {get_higher_profit(companies_data)}')
