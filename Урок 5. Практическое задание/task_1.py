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

def aver_profit_company():
    name_company = 'Company'
    numbers_company = int(input('Please enter number of firm: '))
    company = namedtuple(
        name_company,
        "company_name first_quarter second_quarter third_quarter fourth_quarter")
    profit_aver = {}

    for el in range(numbers_company):
        all_company = company(
            company_name = input('Please enter a name of company: '),
            first_quarter  = int(input('Please enter first quarter profit ')),
            second_quarter = int(input('Please enter second quarter profit ')),
            third_quarter = int(input('Please enter third quarter profit ')),
            fourth_quarter= int(input('Please enter fourth quarter profit ')))

        profit_aver[all_company.company_name] = (all_company.first_quarter + all_company.second_quarter + all_company.third_quarter + all_company.fourth_quarter) / 4

    total_aver = 0
    for value in profit_aver.values():
        total_aver += value
    total_aver = total_aver / numbers_company

    for key, value in profit_aver.items():
        if value < total_aver:
            print(f'Company "{key}" below average profit ')
        elif value < total_aver:
            print(f'Company "{key}"above average profit')
        elif value == total_aver:
            print(f'Company "{key}" average profit')

print('Program "Count average profit of all companies"')
aver_profit_company()