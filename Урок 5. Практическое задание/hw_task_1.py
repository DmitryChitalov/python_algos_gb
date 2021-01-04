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


def profit_calc():
    count_buss = int(input('Введите количество предприятий для расчета прибыли: '))
    tmp_profit_base = []
    middle_profit_company = {}
    list_buss = namedtuple('firms', 'name_f quarter_1 quarter_2 quarter_3 quarter_4')
    while count_buss > 0:
        name_buss = input('Введите название предприятия: ')
        profit_buss = input('через пробел введите прибыль данного предприятия'
                            'за каждый квартал (Всего 4 квартала): ')
        for i in profit_buss.split():
            tmp_profit_base.append(i)
        company = list_buss(name_f=name_buss, quarter_1=int(tmp_profit_base[0]),
                            quarter_2=int(tmp_profit_base[1]), quarter_3=int(tmp_profit_base[2]),
                            quarter_4=int(tmp_profit_base[3]))
        middle_profit_company[company.name_f] = (company.quarter_1 + company.quarter_2 + \
                                                 company.quarter_3 + company.quarter_4) / 4
        tmp_profit_base.clear()
        count_buss -= 1

    count = 0
    for i in middle_profit_company.keys():
        count += 1
    middle_profit = sum(middle_profit_company.values()) / count

    minimum = []
    maximum = []
    for key in middle_profit_company:
        if middle_profit_company[key] < middle_profit:
            minimum.append(key)
        elif middle_profit_company[key] > middle_profit:
            maximum.append(key)
    print(f'Средняя годовая прибыль всех предприятий: {sum(middle_profit_company.values())}')
    print(f'Средняя прибыль за квартал обобщенная на каждое предприятие: {middle_profit / 4}')
    print(f'Предприятия, с прибылью выше среднего значения: {", ".join(maximum)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(minimum)}')


profit_calc()
