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

import collections
import random

Comp_data = collections.namedtuple('Company_Data', ['comp_name', 'profit_1q', 'profit_2q', 'profit_3q', 'profit_4q',
                                                    'annual_profit'])

print('Введите количество предприятий для расчета прибыли:')
comp_qty = 10
print(comp_qty)

comp_list = []
total_profits = 0

for element in range(comp_qty):
    print('Введите название предприятия:')  # user input imitation
    comp_name = 'Компания_' + str(element + 1)
    print(comp_name)
    print('Через пробел введите прибыль данного предприятия за каждый квартал:')
    comp_profits = str(random.randint(1000, 10000)) + ' ' + str(random.randint(1000, 10000)) + ' ' + \
                   str(random.randint(1000, 10000)) + ' ' + str(random.randint(1000, 10000))
    comp_profits_list = [int(n) for n in comp_profits.split(sep=" ")]

    print(comp_profits)
    company_data_tuple = Comp_data(comp_name, *comp_profits_list, sum(comp_profits_list))
    comp_list.append(company_data_tuple)
    total_profits += comp_list[element].profit_1q + comp_list[element].profit_2q + \
                     comp_list[element].profit_3q + comp_list[element].profit_4q

#  print(comp_list)

average_profits = int(total_profits/comp_qty)

print()
print(f'средняя годовая приыль всех предприятий:{average_profits}')

more_profitable_comps = []
less_profitable_comps = []

for element in range(comp_qty):
    if comp_list[element].annual_profit > average_profits:
        more_profitable_comps.append(comp_list[element].comp_name)
    else:
        less_profitable_comps.append(comp_list[element].comp_name)

print(f'Предприятия с прибылью выше среднего:{more_profitable_comps}')
print(f'Предприятия с прибылью ниже среднего: {less_profitable_comps}')
