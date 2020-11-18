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

company = namedtuple('company', 'Name quarters total')
name = ''
quarters = []
total = 0
company_list = []
while True:
    try:
        quantity = int(input('Введите количество предприятий для расчета прибыли: '))
        if quantity <= 0:
            print('Введите положительное число')
            continue
        break
    except ValueError:
        print('Нужно вводить число')
for i in range(quantity):
    space = False
    while not space:
        name = input(f'Введите название предприятия {i + 1}: ')
        if len(name) < 1 or name == ' ' * len(name):
            print('Название не может быть пустым')
            continue
        space = True
    correct = False
    while not correct:
        while True:
            quarters = input(
                f'Через пробел введите прибыль предприятия "{name}" за каждый квартал(Всего 4 квартала): ').split()
            if len(quarters) != 4:
                print('Введите 4 числа')
            else:
                break
        try:
            total = sum([float(item) for item in quarters])
        except ValueError:
            print('Вводить можно только числа')
            continue
        correct = True
    data = company(Name=name, quarters=quarters, total=total)
    company_list.append(data)

total_annual_profit = 0
for i in company_list:
    total_annual_profit += i.total

avg = total_annual_profit / quantity
print('+' * 100)
print(f'Средняя годовая прибыль всех предприятий: {avg}')

high = {}
low = {}
middle = {}

for i in company_list:
    if i.total > avg:
        high[i.Name] = i.total
    elif i.total == avg:
        middle[i.Name] = i.total
    else:
        low[i.Name] = i.total

print(f'Предприятия, с прибылью выше среднего значения: {high}')
print(f'Предприятия, с прибылью ниже среднего значения: {low}')
print(f'Предприятия, с прибылью равной среднему значению: {middle}')
