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


def determine_average_profit():
    base_companies = 'company'
    average_profit = {}
    num_enterprises = int(input('Введите количество предприятий: '))
    company_data = namedtuple(base_companies, 'name period_1 period_2 period_3 period_4')

    for i in range(num_enterprises):
        company = company_data(name=input('\nВведите название предприятия: '),
                               period_1=int(input('Введите прибыль за первый квартал:  ')),
                               period_2=int(input('Введите прибыль за второй квартал: ')),
                               period_3=int(input('Введите прибыль за третий квартал: ')),
                               period_4=int(input(f'Введите прибыль за четвертый квартал: '))
                               )

        average_profit[company.name] = \
            (company.period_1 + company.period_2 + company.period_3 + company.period_4) / 4

    sum_mean_values = 0
    for val in average_profit.values():
        sum_mean_values += val
    sum_mean_values = sum_mean_values / num_enterprises

    print(f'\nСредняя годовая прибыль всех предприятий = {sum_mean_values}\n')

    for key, val in average_profit.items():
        if val == sum_mean_values:
            print(f'У компании "{key}" средняя прибыль')
        elif val > sum_mean_values:
            print(f'У компании "{key}" прибыль выше среднего')
        elif val < sum_mean_values:
            print(f'У компании "{key}" прибыль ниже среднего')


determine_average_profit()
