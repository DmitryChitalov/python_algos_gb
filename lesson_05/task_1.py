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


def get_firms_data(number):
    """Формирует словарь с шаблоном namedtuple по умолчанию
       и заполняет его данными по предприятиям за 4 квартала"""
    FIRM_PROFIT = namedtuple('Profits', 'I II III IV sum_profit')
    firms_dict = defaultdict(FIRM_PROFIT)
    try:
        for _ in range(number):
            firm_name = input('\nВведите название предприятия: ')
            firm_profit = [float(elem)for elem in input(
                'Через пробел введите прибыль данного предприятия поквартально: ').split()]
            sum_profit = sum(firm_profit)
            firms_dict[firm_name] = FIRM_PROFIT(*firm_profit, sum_profit)
    except ValueError:
        print('\nНеобходимо ввести числа в качестве значений прибыли!')
        return get_firms_data(number)
    except TypeError:
        print('\nНеобходимо ввести прибыль за четыре квартала!')
        return get_firms_data(number)
    return firms_dict


def average_profit(firms_dct):
    """Считает среднюю прибыль по всем предприятиям"""
    profit = sum(value.sum_profit for value in firms_dct.values())
    return profit / len(firms_dct)


def below_profit(firms_dct, profit):
    """Возвращает генератор, содержащий наименования предприятий,
       прибыль которых ниже средней"""
    result = (key for key in firms_dct if firms_dct[key].sum_profit < profit)
    return result


def over_profit(firms_dct, profit):
    """Возвращает генератор, содержащий наименования предприятий,
       прибыль которых выше средней"""
    result = (key for key in firms_dct if firms_dct[key].sum_profit > profit)
    return result


def firms_count():
    """Возвращает количество предприятий"""
    try:
        count = int(input('\nВведите количество фирм: '))
    except ValueError:
        print('\nНеобходимо ввести целое число!')
        return firms_count()
    return count


firms_num = firms_count()
firms_data = get_firms_data(firms_num)
av_profit = average_profit(firms_data)
print(f'\nСредняя годовая прибыль всех предприятий: {av_profit}')
print('\nПредприятия с прыбылью выше средней:', *over_profit(firms_data, av_profit), sep='\n')
print('\nПредприятия с прыбылью ниже средней:', *below_profit(firms_data, av_profit), sep='\n')
