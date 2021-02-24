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
from collections import Counter

from collections import namedtuple

numer_company = int(input('Введите количество предприятий: '))
company = namedtuple('Comp', 'Name first_quarter second_quarter third_quarter fourth_quarter average_income')
revenue_each = {}

while numer_company > 0:
    name = input("Введите название: ")
    revenue = list(input("Через пробел введите прибыль данного предприятия: ").split(" "))

    # print(revenue[0])
    res = company(Name=name, first_quarter=revenue[0], second_quarter=revenue[1], third_quarter=revenue[2],
                  fourth_quarter=revenue[3], average_income=0)
    revenue_each[res.Name] = (int(res.first_quarter) + int(res.second_quarter) + int(res.third_quarter) +
                              int(res.fourth_quarter)) / 4
    #print(revenue_each)
    numer_company = numer_company - 1

total = 0
for value in revenue_each.values():
    total += value
total = total / len(revenue_each)
print(f'Среднее значение: {total}')

for key, value in revenue_each.items():
    if value > total:
        print(f'Предприятие с прибылью выше среднего значения: {key} ')
    else:
        print(f'Предприятие с прибылью ниже среднего значения: {key} ')
