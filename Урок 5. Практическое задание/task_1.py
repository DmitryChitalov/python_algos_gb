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


def calc():
    my_var = 'Company'
    n = int(input('Количество ппредприятий: '))
    companies = namedtuple(
        my_var,
        'name period_1 period_2 period_3 period_4')
    profit_aver = {}
    for i in range(n):
        company = companies(
            name=input('Название предприятия '), period_1=int(
                input('Прибыль за 1 квартал ')), period_2=int(
                input('Прибыль за 2 квартал ')), period_3=int(
                input('Прибыль за 3 квартал ')), period_4=int(
                input('Прибыль за 4 квартал ')))

        profit_aver[company.name] = (company.period_1 + company.period_2 + company.period_3 + company.period_4) / 4
    total_aver = 0
    for value in profit_aver.values():
        total_aver += value
    total_aver = total_aver / n
    for key, value in profit_aver.items():
        if value > total_aver:
            print(f'{key} - прибыль выше среднего')
        elif value < total_aver:
            print(f'{key} - прибыль ниже среднего')
        elif value == total_aver:
            print(f'{key} - средняя прибыль')


calc()

# import collections
#
# def calc():
#     n=int(input('Количество ппредприятий: '))
#     d=dict()
#     a=1
#
#     for i in range(n):
#         name = input('Название: ')
#         pr = input('прибыль за каждый квартал\n'
#                    '(через пробел). всего 4 кв: ')
#         profit = pr.split()
#         d[name] = profit
#         a+=1
#
#     fab = collections.Counter(d)
#     b=0
#     t=0
#     for i in fab:
