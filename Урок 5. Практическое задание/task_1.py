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


number_of_companies = int(input('Введите количество предприятий для расчета прибыли: '))
dict_companies = defaultdict(list)

for n in range(number_of_companies):
    name_of_company = input('Введите название предприятия: ')
    profit = input(f'Введите через пробел прибыль {name_of_company} за каждый квартал (всего 4 квартала): ')
    for el in str.split(profit):
        dict_companies[name_of_company].append(int(el))

total_sum = 0
for key in dict_companies:
    total_sum += sum(dict_companies[key])

average_total_sum = total_sum / number_of_companies
more_than_average = []
less_than_average = []

for key in dict_companies:
    if sum(dict_companies[key]) < average_total_sum:
        less_than_average.append(key)
    elif sum(dict_companies[key]) > average_total_sum:
        more_than_average.append(key)


print(f'Средняя годовая прибыль всех предприятий: {average_total_sum}')
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(more_than_average)}')
print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(less_than_average)}')

