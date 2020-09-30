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


def data_from_user():
    count = int(input('Введите количество фирм: '))
    data_firm = namedtuple('data_firm', 'name I II III IV')
    list_firms_all = []
    while count > 0:
        list_firm = data_firm(
            name=input('Введите название фирмы: '),
            I=input('Введите прибыль за I квартал: '),
            II=input('Введите прибыль за II квартал: '),
            III=input('Введите прибыль за III квартал: '),
            IV=input('Введите прибыль за IV квартал: ')
        )
        list_firms_all.append(list_firm)
        count -= 1
    return list_firms_all


def middle_profit_firm(list_firms_in: list):
    dict_middle_profit_firm = {}
    for firm in list_firms_in:
        dict_middle_profit_firm[firm.name] = sum(map(int, firm[1:]))
    return dict_middle_profit_firm


def count_middle_profit_all(middle_profit_firm_in: dict):
    return sum(middle_profit_firm_in.values()) / len(middle_profit_firm_in)


def print_firms(middle_profit_firms_in: list, profit_year_firm_in: dict):
    list_up = []
    list_down = []
    for firm in profit_year_firm_in.keys():
        if profit_year_firm_in.get(firm) > middle_profit_firms_in:
            list_up.append(firm)
        else:
            list_down.append(firm)
    print(f'фирмы с прибылью больше средней {list_up}\n'
          f'фирмы с прибылью меньше средней {list_down}'
          )


profit_year_firm = middle_profit_firm(data_from_user())
middle_profit_firms = count_middle_profit_all(profit_year_firm)
print_firms(middle_profit_firms, profit_year_firm)
