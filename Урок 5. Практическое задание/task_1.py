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
from statistics import mean
import collections


def input_data():
    data = collections.OrderedDict([])
    while True:
        try:
            count = int(input('Введите количество предприятий для расчета прибыли: '))
        except ValueError:
            print('Введите число!!!')
        else:
            break
    data['count'] = count
    for i in range(count):
        company = collections.namedtuple('company', 'company_name profit')
        result = company(
            company_name=input('Введите название предприятия: '),
            profit=input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        )
        data[i] = result
    return data


data = input_data()
all_profit = []
for i in range(data['count']):
    profit = mean(list(map(int, data[i].profit.split())))
    all_profit.append(profit)
    company = collections.namedtuple('company', 'company_name profit')
    data[i] = company(
        company_name=data[i].company_name,
        profit=profit
    )
all_profit = mean(all_profit)
print(f'Средняя годовая прибыль всех предприятий: {all_profit}')
more = []
less = []
for i in range(data['count']):
    if data[i].profit > all_profit:
        more.append(data[i].company_name)
    elif data[i].profit < all_profit:
        less.append(data[i].company_name)
print(f'''Предприятия, с прибылью выше среднего значения: {str(more)[1:-1].replace("'", '')}''')
print(f'''Предприятия, с прибылью ниже среднего значения: {str(less)[1:-1].replace("'", '')}''')