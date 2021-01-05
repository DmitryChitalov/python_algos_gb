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

n = None
while not n:
    try:
        n = int(input('Введите количество предприятий для расчета прибыли: '))
    except ValueError:
        print('Ошибка! Введите целое положительное число')
        continue
firm_data = namedtuple('Фирма', 'name profit_1 profit_2 profit_3 profit_4')
companies = []
profit_all_companies = 0
for i in range(n):
    name = input('Введите название предприятия: ')
    profits = input('через пробел введите прибыль данного предприятия '
                    'за каждый квартал(Всего 4 квартала): ').split()
    firm = firm_data(
        name=name,
        profit_1=int(profits[0]),
        profit_2=int(profits[1]),
        profit_3=int(profits[2]),
        profit_4=int(profits[3]),
    )
    companies.append(firm)
    profit_all_companies += firm.profit_1 + firm.profit_2 + firm.profit_3 + \
                            firm.profit_4
average_profit = profit_all_companies / len(companies)
more_then_average = []
less_then_average = []
for i in companies:
    if i.profit_1 + i.profit_2 + i.profit_3 + i.profit_4 > average_profit:
        more_then_average.append(i.name)
    else:
        less_then_average.append(i.name)
print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {more_then_average}')
print(f'Предприятия, с прибылью ниже среднего значения: {less_then_average}')