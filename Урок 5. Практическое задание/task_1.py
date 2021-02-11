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

res = namedtuple('Company', 'comp_name q1 q2 q3 q4 q_avg')

try:
    count_comp = int(
        input('Введите количество предприятий для расчета прибыли: '))
except ValueError:
    print('Введено не число')

all_profit_avg = 0
comp_list = []

for item in range(count_comp):
    var_str = input('Введите название предприятия: ')
    var_str_profit = input(
        'Через пробел введите прибыль данного предприятия за каждый '
        'квартал(Всего 4 квартала): ')
    var_profit = var_str_profit.split()
    profit_avg = (int(var_profit[0]) + int(var_profit[1]) +
                  int(var_profit[2]) + int(var_profit[3])) / 4
    var_company = res(var_str, int(var_profit[0]), int(var_profit[1]),
                      int(var_profit[2]), int(var_profit[3]), profit_avg)

    all_profit_avg = all_profit_avg + profit_avg
    comp_list.append(var_company)

all_profit_avg = all_profit_avg / count_comp

var_list = [i.comp_name for i in comp_list if i.q_avg > all_profit_avg]
if var_list:
    print('Предприятия, с прибылью выше среднего значения:')
    for item in var_list:
        print(item)

var_list = [i.comp_name for i in comp_list if i.q_avg < all_profit_avg]
if var_list:
    print('Предприятия, с прибылью ниже среднего значения:')
    for item in var_list:
        print(item)

var_list = [i.comp_name for i in comp_list if i.q_avg == all_profit_avg]
if var_list:
    print('Предприятия, с прибылью равной среднему значению:')
    for item in var_list:
        print(item)

#
# Введите количество предприятий для расчета прибыли: 2
# Введите название предприятия: Фирма_1
# Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 235 345634 55 235
# Введите название предприятия: Фирма_2
# Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 345 34 543 34
# Предприятия, с прибылью выше среднего значения:
# Фирма_1
# Предприятия, с прибылью ниже среднего значения:
# Фирма_2
