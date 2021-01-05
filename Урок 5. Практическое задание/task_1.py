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
from collections import namedtuple, Counter
from statistics import mean
from random import randint

com_lst = []


def add_company():
    com = namedtuple('company', 'name, profit_list')
    while True:
        com.name = input('Введите название компании:')
        try:
            cmp = list(map(float, input('Введите через пробел прибыли за 4 квартала: ').strip().split(' ')))
            if len(cmp) == 4:
                com.profit_list = cmp
                break
        except ValueError:
            print('Ошибка ввода! Попробуйте ещё раз!')
    com_lst.append(com)


def get_averages():
    profits = [sum(el.profit_list) for el in com_lst]
    avg = mean(profits)
    result = namedtuple('result', 'avg, below_avg_list above_avg_list')
    result.avg = avg
    result.above_avg_list = [el for el in com_lst if sum(el.profit_list) >= avg]
    result.below_avg_list = [el for el in com_lst if sum(el.profit_list) < avg]
    return result


for i in range(10):
    com = namedtuple('company', 'name, profit_list')
    com.name = 'company' + str(i)
    com.profit_list = [randint(0, 1000) for i in range(4)]
    com_lst.append(com)

while True:
    user_ans = input('Введите: 1 - Добавить компанию, 2 - Вычислить результат, 3 - Вывести компании, 0 - Выход:')
    if user_ans == '0':
        break
    if user_ans == '1':
        add_company()
    elif user_ans == '2':
        res = get_averages()
        print(f'Средняя годовая прибыль: {res.avg}')
        print('Прибыль выше среднего:')
        for el in res.above_avg_list:
            print(f'{el.name}: {el.profit_list}')
        print('Прибыль ниже среднего:')
        for el in res.below_avg_list:
            print(f'{el.name}: {el.profit_list}')
    elif user_ans == '3':
        for el in com_lst:
            print(f'{el.name}: {el.profit_list}')
    else:
        print('Ошибка. Попробуйте ещё раз')
