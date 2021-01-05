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

from collections import namedtuple
from typing import List


def company_analysis():
    company = namedtuple('Resume', 'id name profit_1 profit_2 profit_3 profit_4 all_profit')
    companies: List[namedtuple] = []
    count_companies = int(input('Введите количество компаний: '))
    all_sum = 0
    for i in range(1, count_companies + 1):
        sum_prof = 0
        n = input('Введите название компании: ')
        prof = input('Введите прибыль данного предприятия за каждый квартал через пробел: ').split(' ')
        for el in prof:
            sum_prof = sum_prof + int(el)
            all_sum = all_sum + int(el)
        companies.append(company(
            id=i,
            name=n,
            profit_1=prof[0],
            profit_2=prof[1],
            profit_3=prof[2],
            profit_4=prof[3],
            all_profit=sum_prof
        ))
    comp_up = []
    comp_down = []
    for i in range(len(companies)):
        if companies[i].all_profit > float(all_sum / count_companies):
            comp_up.append(companies[i].name)
        else:
            comp_down.append(companies[i].name)
    print('Средняя годовая прибыль всех предприятий: ', float(all_sum / count_companies))
    print('Предприятия с прибылью выше среднегодовой прибыли: ', ', '.join(comp_up))
    print('Предприятия с прибылью ниже среднегодовой прибыли: ', ', '.join(comp_down))


company_analysis()
