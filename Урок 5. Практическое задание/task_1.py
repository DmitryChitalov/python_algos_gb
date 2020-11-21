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

from collections import namedtuple, defaultdict


def is_it_int(data):
    while not data.isdigit():
        print('Ошибка ввода. Пожалуйста, введите одно целое натуральное число.')
        data = input('Введите число: ')
    return int(data)


def check_input(data):
    while len(data) != 4:
        print('Ошибка ввода.')
        data = input('Пожалуйста, введите 4 числа, разделённых пробелом: ').split()
    return data


def progam_1():
    company_nt = namedtuple('company', 'name profit')
    company_list = []
    for i in range(is_it_int(input('Введите количество предприятий для расчета прибыли: '))):
        company = company_nt(
            name=input('Введите название предприятия: '),
            profit=sum(map(int, check_input(input('Через пробел введите прибыль данного предприятия'
                                      ' за каждый квартал(Всего 4 квартала): ').split())))
        )
        company_list.append(company)

    print(company_list)

    overall_profit = 0
    for company in company_list:
        overall_profit += company.profit
    overall_profit /= len(company_list)
    print(overall_profit)

    more, less = [], []
    for i in range(len(company_list)):
        if company_list[i].profit > overall_profit:
            more.append(company_list[i].name)
        if company_list[i].profit < overall_profit:
            less.append(company_list[i].name)

    if len(more) > 0:
        print('Наименования предприятий, чья прибыль выше среднего:')
        [print(i) for i in more]
    if len(less) > 0:
        print(f'\nНаименования предприятий, чья прибыль ниже среднего:')
        [print(i) for i in less]
    if len(more) == 0 and len(less) == 0:
        print(f'Прибыль всех предприятий является равной среднему показателю ({overall_profit}).')

# progam_1()


def progam_2():
    company_dd = defaultdict(list)

    for i in range(is_it_int(input('Введите количество предприятий для расчета прибыли: '))):
        company_temp_list = []
        company_temp_list.append(input('Введите название предприятия: '))
        company_temp_list.extend(check_input(input('Через пробел введите прибыль данного предприятия'
                                        ' за каждый квартал(Всего 4 квартала): ').split()))
        company_dd[company_temp_list[0]] = company_temp_list[1:]

    overall_profit = 0
    for profit in company_dd.values():
        overall_profit += sum(map(int, profit))
    overall_profit /= len(company_dd)
    print(f'\nСредняя прибыль всех предприятий равна: {overall_profit}.\n')

    more, less = [], []
    for company in company_dd.keys():
        if sum(map(int, company_dd[company])) > overall_profit:
            more.append(company)
        if sum(map(int, company_dd[company])) < overall_profit:
            less.append(company)

    if len(more) > 0:
        print('Наименования предприятий, чья прибыль выше среднего:')
        [print(i) for i in more]
    if len(less) > 0:
        print(f'\nНаименования предприятий, чья прибыль ниже среднего:')
        [print(i) for i in less]
    if len(more) == 0 and len(less) == 0:
        print(f'Прибыль всех предприятий является равной среднему показателю ({overall_profit}).')


progam_2()
