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


import collections


def input_profit(msg='', err_msg='', **kwargs):
    while True:
        try:
            res = int(input(msg))
        except ValueError:
            print(err_msg)
        else:
            break
    return res


while True:
    try:
        companies_count = int(input('Введите количество предприятий для расчета прибыли: '))
    except ValueError:
        companies_count = -1
    if companies_count >= 0:
        break
    print('Требуется ввести целое положительное число!')
company = collections.namedtuple('Companies', 'name quart_1 quart_2 quart_3 quart_4')
companies = {}
profit = 0
for i in range(companies_count):
    while True:
        company.name = input('Введите название предприятия: ')
        if company.name not in companies:
            break
        print('Предприятие с таким названием уже есть!')
    company.quart_1 = input_profit(f'Введите прибыль за 1-й квартал: ', 'Требуется ввести целое число!')
    company.quart_2 = input_profit(f'Введите прибыль за 2-й квартал: ', 'Требуется ввести целое число!')
    company.quart_3 = input_profit(f'Введите прибыль за 3-й квартал: ', 'Требуется ввести целое число!')
    company.quart_4 = input_profit(f'Введите прибыль за 4-й квартал: ', 'Требуется ввести целое число!')
    companies[company.name] = (company.quart_1 + company.quart_2 + company.quart_3 + company.quart_4) / 4
    profit += companies[company.name]
avg_profit = profit / companies_count
print(f'Средняя годовая прибыль по всем предприятиям {avg_profit}')
for comp in companies:
    if companies[comp] < avg_profit:
        str_profit = 'ниже'
    elif companies[comp] > avg_profit:
        str_profit = 'выше'
    else:
        str_profit = 'равна'
    print(f'Предприятие {comp}, прибыль: {str_profit} средней.')
