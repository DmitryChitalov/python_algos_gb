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

list_fabrics = []
fabrics_low_profit = []
fabrics_high_profit = []
fabric_info = namedtuple('fabric_info', ['fabric', 'profit'])

num_fabrics = int(input("Введите количество предприятий для расчета прибыли: "))

while num_fabrics:
    fabric_name = input("Введите название предприятия: ")
    profit = list(map(
        int,
        input("через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ").split(" ")
    ))
    info = fabric_info(fabric=fabric_name, profit=profit)
    list_fabrics.append(info)
    num_fabrics -= 1

avg_profit = sum([sum(fabric.profit) for fabric in list_fabrics]) / len(list_fabrics)

for fabric in list_fabrics:
    if sum(fabric.profit) >= avg_profit:
        fabrics_high_profit.append(fabric.fabric)
    else:
        fabrics_low_profit.append(fabric.fabric)

print(f"Средняя годовая прибыль всех предприятий: {avg_profit}")
print(f"Предприятия с прибылью выше средней: {', '.join(fabrics_high_profit)}")
print(f"Предприятия с прибылью ниже средней: {', '.join(fabrics_low_profit)}")
