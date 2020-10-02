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

template_for_companies = namedtuple('company', 'name profit')
number_of_companies = int(input('Введите количество предприятий для расчета прибыли: '))
list_of_companies = []
summary_profit = 0
companies_above_average_profit = []
companies_below_average_profit = []

for elem in range(number_of_companies):
    company = template_for_companies(
        name=input(f'Введите название предприятия {elem + 1}: '),
        profit=sum([int(elem) for elem in input('Через пробел введите прибыль данного предприятия за '
                                                '4 квартала (4 числа подряд): ').split()])
    )
    list_of_companies.append(company)

average_profit = sum([x.profit for x in list_of_companies]) / number_of_companies

for el in list_of_companies:
    if el.profit > average_profit:
        companies_above_average_profit.append(el.name)
    else:
        companies_below_average_profit.append(el.name)

print(f'Средняя годовая прибыль всех предприятий: {average_profit}\n'
      f'Предприятия, с прибылью выше среднего значения: {companies_above_average_profit}\n'
      f'Предприятия, с прибылью ниже среднего значения: {companies_below_average_profit}')
