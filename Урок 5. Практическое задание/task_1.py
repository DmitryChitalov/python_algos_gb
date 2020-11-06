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

FP = namedtuple('firm_profit', 'quarter_1 quarter_2 quarter_3 quarter_4 total')
enterprise_base = {}

enterprises_number = int(input("Введите количество предприятий для расчета прибыли: "))
for enterprise in range(enterprises_number):
    brand = input("Введите название предприятия: ")
    profit_string = input("через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ")
    profit = profit_string.split()
    enterprise_base[brand] = FP(quarter_1=int(profit[0]), quarter_2=int(profit[1]), quarter_3=int(profit[2]),
                                quarter_4=int(profit[3]),
                                total=int(profit[0]) + int(profit[1]) + int(profit[2]) + int(profit[3]))
for el in enterprise_base:
    print(enterprise_base[el])

general_average_annual_profit = sum(enterprise_base[el].total for el in enterprise_base) / len(enterprise_base)
print(f'Средняя годовая прибыль всех предприятий: {general_average_annual_profit}')

winner, loser = '', ''
for el in enterprise_base:
    if enterprise_base[el].total > general_average_annual_profit:
        winner += el + ' '
    elif enterprise_base[el].total < general_average_annual_profit:
        loser += el + ' '

print(f'Предприятия, с прибылью выше среднего значения: {winner}')
print(f'Предприятия, с прибылью ниже среднего значения: {loser}')
