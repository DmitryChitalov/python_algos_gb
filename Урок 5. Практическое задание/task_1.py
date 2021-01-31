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


def get_sum_mer(obj):
    sum_mer = 0
    for elem in obj:
        sum_mer += int(elem)
    return sum_mer


num_companies = int(
    input(
        "Введите количество предприятий (для рассчет прибыльности): "))
list_companies = []
total_profit = 0
for num in range(num_companies):
    name_company = input("Пожалуйста введите название предприятия: ")
    company_profits = input(
        "Введите через пробел прибыль этого предприятия за соотв. квартал: ").split(' ')
    sum_profit = get_sum_mer(company_profits)
    total_profit += sum_profit
    company_tuple = namedtuple(
        name_company,
        'name first_quarter second_quarter third_quarter fourth_quarter annual_profit'
    )
    company_tuple_parts = company_tuple(
        name=name_company,
        first_quarter=int(company_profits[0]),
        second_quarter=int(company_profits[1]),
        third_quarter=int(company_profits[2]),
        fourth_quarter=int(company_profits[3]),
        annual_profit=sum_profit
    )
    list_companies.append(company_tuple_parts)
average_profit = total_profit / num_companies
print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
companies_below_average = ''
companies_above_average = ''
for company in list_companies:
    if company.annual_profit > average_profit:
        companies_above_average += company.name
    else:
        companies_below_average += company.name
print(f'Предприятия с прибылью выше среднего: {companies_above_average}')
print(f'Предприятия с прибылью ниже среднего: {companies_below_average}')
