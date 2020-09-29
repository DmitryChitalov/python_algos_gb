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
from collections import defaultdict, namedtuple


def average_profit_defaultdict():
    data = defaultdict(int)
    quantity = int(input('Введите количество предприятий для расчета прибыли: '))
    for i in range(quantity):
        title = input('Введите название предприятия: ')
        profit = input('через пробел введите прибыль данного предприятия '
                       'за каждый квартал(Всего 4 квартала): ').split(' ')
        profit_sum = sum([int(el) for el in profit])
        data[title] += profit_sum

    data_average = defaultdict(str)
    average = sum(data.values()) / quantity
    data_average[f'average'] = average
    for key, val in data.items():
        if val >= average:
            data_average['above_average'] += key + ' '
        else:
            data_average['below_average'] += key + ' '
    return f'Средняя годовая прибыль всех предприятий: {average:.2f} \n' \
           f'Предприятия, с прибылью выше среднего значения: {data_average["above_average"]} \n' \
           f'Предприятия, с прибылью ниже среднего значения: {data_average["below_average"]}'


def average_profit_namedtuple():
    Data = namedtuple('Data_company', 'title profit_average')
    quantity = int(input('Введите количество предприятий для расчета прибыли: '))
    all_company_list = []
    average = 0
    for i in range(quantity):
        title = input('Введите название предприятия: ')
        profit = input('через пробел введите прибыль данного предприятия '
                       'за каждый квартал(Всего 4 квартала): ')
        profit = sum([int(el) for el in profit.split(' ')])
        average += profit
        all_company_list.append(Data._make([title, profit]))
    average /= quantity
    above_average, below_average = '', ''
    for el in all_company_list:
        if el.profit_average > average:
            above_average += el.title + ' '
        else:
            below_average += el.title + ' '

    return f'Средняя годовая прибыль всех предприятий: {average:.2f} \n' \
           f'Предприятия, с прибылью выше среднего значения: {above_average} \n' \
           f'Предприятия, с прибылью ниже среднего значения: {below_average}'



print(average_profit_defaultdict())
print(average_profit_namedtuple())
