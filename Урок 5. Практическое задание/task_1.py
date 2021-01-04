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

from collections import namedtuple, defaultdict, ChainMap


# Первый вариант решения, через namedtuple и defaultdict
def company_income_avg1(obj: list):
    companies_profit_max = defaultdict(int)
    companies_profit_min = defaultdict(int)

    profit_avg = sum([eval(f'i.quarter{j+1}') for i in obj for j in range(4)]) / len(obj)

    for i in obj:
        company_name = type(i).__name__
        company_profit = sum(i)
        if company_profit > profit_avg:
            companies_profit_max[company_name] = company_profit
        if company_profit < profit_avg:
            companies_profit_min[company_name] = company_profit

    print('Средняя годовая прибыль всех предприятий:', profit_avg)
    if companies_profit_max:
        print('Предприятия, с прибылью выше среднего значения:', *companies_profit_max.keys())
    if companies_profit_min:
        print('Предприятия, с прибылью ниже среднего значения:', *companies_profit_min.keys())


def company_formation1():
    companies = []

    for i in range(int(input('Введите количество предприятий для расчета прибыли: '))):
        name = input('Введите название предприятия: ')
        profit = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        company = namedtuple(name, 'quarter1 quarter2 quarter3 quarter4')
        companies.append(company._make(map(int, profit.split())))

    return company_income_avg1(companies)


# Второй вариант решения через ChainMap
def company_income_avg2(obj: list):
    companies_profit_max = []
    companies_profit_min = []

    profit_avg = sum([sum(i.values()) for i in ChainMap(*obj).values()]) / len(obj)

    for i, j in ChainMap(*obj).items():
        company_name = i
        company_profit = sum(j.values())
        if company_profit > profit_avg:
            companies_profit_max.append(company_name)
        if company_profit < profit_avg:
            companies_profit_min.append(company_name)

    print('Средняя годовая прибыль всех предприятий:', profit_avg)
    if companies_profit_max:
        print('Предприятия, с прибылью выше среднего значения:', *companies_profit_max)
    if companies_profit_min:
        print('Предприятия, с прибылью ниже среднего значения:', *companies_profit_min)


def company_formation2():
    companies = []

    for i in range(int(input('Введите количество предприятий для расчета прибыли: '))):
        name = input('Введите название предприятия: ')
        profit = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        companies.append({name: dict(zip(['quarter1', 'quarter2', 'quarter3', 'quarter4'], map(int, profit.split())))})

    return company_income_avg2(companies)


if __name__ == '__main__':
    company_formation1()
    company_formation2()
