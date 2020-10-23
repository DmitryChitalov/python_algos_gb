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

firm_num = int(input('Введите количество предприятий для расчета прибыли:'))
firms = namedtuple('Firm', 'name quarter1 quarter2 quarter3 quarter4')
firm_average = {}
for i in range(firm_num):
    firm=firms(
        name = input('Введите название предприятия:'),
        quarter1 = int(input('1 kv')),
        quarter2=int(input('2 kv')),
        quarter3=int(input('3 kv')),
        quarter4=int(input('4 kv'))
    )
    firm_average[firm.name] = (firm.quarter1 + firm.quarter2 + firm.quarter3 + firm.quarter4) / 4

total_aver = 0
for value in firm_average.values():
    total_aver += value
total_aver = total_aver / firm_num

for key, value in firm_average.items():
    if value > total_aver:
        print(f'{key} - прибыль выше среднего')
    elif value < total_aver:
        print(f'{key} - прибыль ниже среднего')
    elif value == total_aver:
        print(f'{key} - прибыль cредняя')

