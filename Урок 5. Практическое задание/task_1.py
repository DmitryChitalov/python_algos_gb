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

company = namedtuple('Company', 'name period_1 period_2 period_3 period_4 sum_profit')
company_amount = int(input("Введите количество предприятий для расчета прибыли: "))
# company_amount = 2
companies = []
for i in range(0, company_amount):
    company_name = input("Введите название предприятия: ")
    company_profit = input("через пробел введите прибыль данного предприятия за каждый квартал (Всего 4 квартала): ")
    company_quarters = list(map(int, company_profit.split(' ')))
    companies.append(company(company_name, *company_quarters, sum(company_quarters)))

companies_avg_profit = sum(comp.sum_profit for comp in companies) / len(companies)
print(f'Средняя годовая прибыль всех предприятий: {companies_avg_profit}')

companies_above_avg = [comp.name for comp in companies if comp.sum_profit > companies_avg_profit]
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(companies_above_avg)}')

companies_below_avg = [comp.name for comp in companies if comp.sum_profit < companies_avg_profit]
print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(companies_below_avg)}')
