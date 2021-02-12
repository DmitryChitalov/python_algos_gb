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

num_firms = int(input("Введите количество предприятий для расчета прибыли:"))

firms_data = namedtuple('Firms', 'name quarter1 quarter2 quarter3 quarter4')
firms = []

for i in range(num_firms):
    firm_name = input("Введите название предприятия: ")
    firm_profit = input("через пробел введите прибыль данного предприятия \n"
                        "за каждый квартал(Всего 4 квартала): ").split(" ")
    firms.append(
        firms_data(
            name=firm_name,
            quarter1=int(firm_profit[0]),
            quarter2=int(firm_profit[1]),
            quarter3=int(firm_profit[2]),
            quarter4=int(firm_profit[3])
        )
    )

sum_profit = 0

for i in firms:
    sum_profit = sum_profit + i.quarter1 + i.quarter2 + i.quarter3 + i.quarter4

avr_profit = sum_profit / len(firms)

print("Средняя годовая прибыль всех предприятий: ", avr_profit)

high_firm = []
less_firm = []

for i in firms:
    tmp_sum = i.quarter1 + i.quarter2 + i.quarter3 + i.quarter4
    if tmp_sum >= avr_profit:
        high_firm.append(i.name)
    else:
        less_firm.append(i.name)

print("Предприятия, с прибылью выше среднего значения: ", high_firm)
print("Предприятия, с прибылью ниже среднего значения: ", less_firm)
