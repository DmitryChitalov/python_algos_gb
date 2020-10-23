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

from collections import defaultdict

number_of_enterprises = int(input('Введите количество предприятий для расчета прибыли: '))
company = defaultdict(int)
for el in range(number_of_enterprises):
    company_name = input(f'Введите название предприятия: ')
    year_profit = sum(list(map(int, (input('Через пробел введите прибыль данного предприятия '
                                           'за каждый квартал(Всего 4 квартала):').split()))))
    company[company_name] = year_profit
# print(company)
average_profit = 0
for val in company.values():
    average_profit += val / number_of_enterprises
company_with_profit_above_average = [key for key, val in company.items() if val > average_profit]
company_with_profit_below_average = [key for key, val in company.items() if val < average_profit]
print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {company_with_profit_above_average}')
print(f'редприятия, с прибылью ниже среднего значения: {company_with_profit_below_average}')
