"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

"""

from collections import namedtuple

Enterprise = namedtuple('Enterprise', ['name', 'quarters', 'profit'])
all_companies = set()

ent_num = int(input("Введите количество предприятий для расчета прибыли: "))
total_profit = 0
for i in range(1, ent_num + 1):
    profit = 0
    quarters = []

    name = input(f'Название {i}-го предприятия: ')

    quarters = list(map(int, input(f'Через пробел введите прибыль предприятия {name} за каждый квартал '
                                   f'(всего 4 квартала): ').split()))
    for j in range(len(quarters)):
        profit += quarters[j]

    company = Enterprise(name=name, quarters=tuple(quarters), profit=profit)

    all_companies.add(company)
    total_profit += profit

average = total_profit / ent_num

print(f'\nСредняя годовая прибыль всех предприятий: {average}')

print(f'\nПредприятия с прибылью >= среднего:')
for company in all_companies:
    if company.profit >= average:
        print(f'Предприятие {company.name} заработало {company.profit}')

print(f'\nПредприятия с прибылью < среднего:')
for company in all_companies:
    if company.profit < average:
        print(f'Предприятие {company.name} заработало {company.profit}')