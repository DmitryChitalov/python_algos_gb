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


def func_with_defaultdict():            # функция с использованием коллекции defaultdict
    company_dict = defaultdict(int)     # дефолтное значение - целые числа
    n = int(input('Введите количество предприятий для расчета прибыли: '))
    for i in range(n):
        name = input('Введите название предприятия: ')
        income_per_quarter = [int(i) for i in input('Через пробел введите прибыль данного предприятия \n'
                                                    'за каждый квартал(Всего 4 квартала): ').split()]
        income = sum(income_per_quarter)            # суммарная годовая рибыль компании
        company_dict[name] = income                 # добавление значения прибыли в словарь

    # общая годовая и средняя прибыль всех компаний
    full_sum_income = sum(company_dict.values())
    avg_income = full_sum_income / n

    # Предприятия, с прибылью ниже и выше среднего значения:
    small = [key for key, value in company_dict.items() if company_dict[key] < avg_income]
    high = [key for key, value in company_dict.items() if company_dict[key] > avg_income]

    print(f'\nСредняя годовая прибыль всех предприятий: {avg_income}')
    print('Предприятия, с прибылью выше среднего значения: ', end='')
    for i in high:
        print(i, end='')

    print('\nПредприятия, с прибылью ниже среднего значения: ', end='')
    for i in small:
        print(i, end='')


def func_with_namedtuple():                 # функция с использованием коллекции namedtuple
    n = int(input('\nВведите количество предприятий для расчета прибыли: '))
    company_lst = []
    for i in range(n):
        name = input('Введите название предприятия: ')
        income_per_quarter = [int(j) for j in input('Через пробел введите прибыль данного предприятия \n'
                                                    'за каждый квартал (Всего 4 квартала): ').split()]
        income = sum(income_per_quarter)                # суммарная годовая рибыль компании
        subject_set = ('income_per_quarter', 'Income')  # названия полей
        Marks = namedtuple(name, subject_set)           # кортеж с параметрами: имя типа, названия полей

        # добавление в список именованных кортежей
        company_lst.append( Marks(income_per_quarter, income) )
        print()

    # общая годовая и средняя прибыль всех компаний
    full_sum_income = sum(company.Income for company in company_lst)    # суммируем все значения по полю 'Income'
    avg_income = full_sum_income / n

    # Предприятия, с прибылью ниже и выше среднего значения:
    # запись названий компаний (получение имён именованных кортежей)
    small = [type(company).__name__ for company in company_lst if company.Income < avg_income]
    high = [type(company).__name__ for company in company_lst if company.Income > avg_income]

    print(f'Средняя годовая прибыль всех предприятий: {avg_income}')
    print('Предприятия, с прибылью выше среднего значения: ', end='')
    for i in high:
        print(i, end='')

    print('\nПредприятия, с прибылью ниже среднего значения: ', end='')
    for i in small:
        print(i, end='')


# func_with_defaultdict()
func_with_namedtuple()

