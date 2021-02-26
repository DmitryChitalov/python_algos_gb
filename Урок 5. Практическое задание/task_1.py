"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple

companies_count = int(input("Введите количество предприятий > "))
company = namedtuple('Company', 'company_name quarter_profit average_profit')
companies = list()
for company_index in range(companies_count):
    new_company_company_name = input("Введите название предприятия > ")
    quarters_profit = input("Через пробел введите прибыль данного предприятия за каждый "
                            "квартал(Всего 4 квартала) > ").split(' ')
    if len(quarters_profit) != 4:
        raise Exception('Quarters count must be 4.')
    new_company_quarter_profit = [int(el) for el in quarters_profit]
    new_company_average_profit = sum(new_company_quarter_profit) / len(new_company_quarter_profit)
    new_company = company(company_name=new_company_company_name, quarter_profit=new_company_quarter_profit,
                          average_profit=new_company_average_profit)
    companies.append(new_company)

average = sum(company.average_profit for company in companies) / companies_count
print(f'Средняя годовая прибыль всех предприятий: {average}')
print('Предприятия, с прибылью выше среднего значения: ',
      ' '.join([company.company_name for company in companies if company.average_profit > average]))
print('Предприятия, с прибылью ниже среднего значения: ',
      ' '.join([company.company_name for company in companies if company.average_profit < average]))
