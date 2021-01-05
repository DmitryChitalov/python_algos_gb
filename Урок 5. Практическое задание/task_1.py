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

amount_company = int(input('Введите количество предприятий для расчета прибыли: '))
list_company = []
company = namedtuple('company', 'name profit')
while amount_company:
    name = input('Введите название предприятия: ')
    profit = input('через пробел введите прибыль данного предприятия\n'
                   'за каждый квартал(Всего 4 квартала): ').split(' ')
    list_company.append(company(name, sum(int(v) for v in profit)))
    amount_company -= 1
print(list_company)

avg_profit = 0
for c in list_company:
    avg_profit += c.profit
avg_profit = avg_profit / len(list_company)

print(f'Средняя годовая прибыль всех предприятий: {avg_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {[val.name for val in list_company if val.profit > avg_profit]}')
print(f'Предприятия, с прибылью ниже среднего значения: {[val.name for val in list_company if val.profit < avg_profit]}')