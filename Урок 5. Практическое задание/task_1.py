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
количество предприятий для расчета прибыли: Рога
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


def calc_firm():
    my_var = 'Company'
    firms = namedtuple(my_var, 'name period_1 period_2 period_3 period_4')
    n = int(input('Введите количество предприятий для расчета прибыли: '))
    profit_companies = {}
    for i in range(n):
        name_firm = input('Название предприятия для расчета прибыли: ')
        profit_firm = input('Через пробел введите прибыль данного предприятия\nза каждый квартал(Всего 4 квартала): ')
        profit_firm = profit_firm.split(' ')
        if len(profit_firm) == 4:
            firm = firms(name=name_firm,
                         period_1=int(profit_firm[0]), period_2=int(profit_firm[1]),
                         period_3=int(profit_firm[2]), period_4=int(profit_firm[3])
                         )
            profit_companies[firm.name] = (firm.period_1 + firm.period_2 + firm.period_3 + firm.period_4) / 4
        else:
            print('Данная фирма не будет внесена в отчет, так как не верно указан доход за кварталы')
    total_profit = 0
    for value in profit_companies.values():
        total_profit += value
    total_profit = total_profit / n
    print(f'Средняя годовая прибыль всех предприятий равна {total_profit}')
    for key, value in profit_companies.items():
        if value > total_profit:
            print(f'Предприятие {key} приносит прибыли больше среднего')
        elif value < total_profit:
            print(f'Предприятие {key} приносит прибыли меньше среднего')
        else:
            print(f'Предприятие {key} приносит среднию прибыль')


calc_firm()
'''
Решал ДЗ уже намного позже срока и поэтому много подсмотрел у вас в задании после решения самостоятельно.
'''
