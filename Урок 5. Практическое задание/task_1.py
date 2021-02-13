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
import functools

le_list = collections.defaultdict(list)
tot_inc_list = collections.defaultdict(list)

print('Input quantity of legal entities:')
qty = input()

for i in range(int(qty)):
    print('Input legal entity name:')
    name = input()
    inc_list = []
    for j in range(4):
        print(f'Input income for <{j + 1}> quarter')
        inc_list.append(int(input()))

    le_list[name] = inc_list
    tot_inc_list[name] = functools.reduce(lambda a, b: a + b, le_list[name])
    print(f'Total income is {tot_inc_list[name]}')

median = functools.reduce(lambda a, b: a + b, list(tot_inc_list.values())) / len(le_list)
print(f'Median income is {median}')

gt_tot_list = dict(filter(lambda a: (a[1] > median), tot_inc_list.items()))
lt_tot_list = dict(filter(lambda a: (a[1] < median), tot_inc_list.items()))

print(f'Income greater than {median}')
print(gt_tot_list)
print(f'Income less than {median}')
print(lt_tot_list)
