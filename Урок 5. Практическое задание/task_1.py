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
from statistics import mean

Company = namedtuple('Company', 'name q1 q2 q3 q4')

companies_quantity = input('Введите количество предприятий: ')

data = []
for i in range(int(companies_quantity)):
    name = input(f'Введите название компании {i + 1}: ')
    quarterly_revenue = input('Введите прибыль за каждый квартал через пробел (всего 4 квартала): ')
    q1 = int(quarterly_revenue.split()[0])
    q2 = int(quarterly_revenue.split()[1])
    q3 = int(quarterly_revenue.split()[2])
    q4 = int(quarterly_revenue.split()[3])
    new_comp = Company(name, q1, q2, q3, q4)
    data.append(new_comp)

revenues = []
for company in data:
    company_yearly = sum([company.q1, company.q2, company.q3, company.q4])
    revenues.append(company_yearly)

avg_revenue = mean(revenues)


def find_below_avg(avg_revenue, data):
    below_avg = []
    for company in data:
        if sum([company.q1, company.q2, company.q3, company.q4]) < avg_revenue:
            below_avg.append(company)
    return below_avg


def find_above_avg(avg_revenue, data):
    above_avg = []
    for company in data:
        if sum([company.q1, company.q2, company.q3, company.q4]) > avg_revenue:
            above_avg.append(company)
    return above_avg


list_above_average = []
for company in find_above_avg(avg_revenue, data):
    list_above_average.append(company.name)

list_below_average = []
for company in find_below_avg(avg_revenue, data):
    list_below_average.append(company.name)

print(f'Средняя прибыль компаний: {avg_revenue}')
print(f'Компании с прибылью выше среднего: {list_above_average}')
print(f'Компании с прибылью ниже среднего: {list_below_average}')
