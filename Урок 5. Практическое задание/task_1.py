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

horns = namedtuple('Horns', 'first_quarter second_quarter third_quarter fourth_quarter')

hoofs = namedtuple('hoofs', 'first_quarter second_quarter third_quarter fourth_quarter')

horns_company = horns(
    first_quarter=235,
    second_quarter=345634,
    third_quarter=55,
    fourth_quarter=235
)

hoofs_company = hoofs(
    first_quarter=345,
    second_quarter=34,
    third_quarter=543,
    fourth_quarter=34
)

res_horns = (horns_company.first_quarter + horns_company.second_quarter + horns_company.third_quarter
             + horns_company.fourth_quarter) / 4

res_hoofs = (hoofs_company.first_quarter + hoofs_company.second_quarter + hoofs_company.third_quarter
             + hoofs_company.fourth_quarter) / 4

if res_horns > 43389.38:
    print('Предприятия, с прибылью выше среднего значения: Рога \n'
          'Предприятия, с прибылью ниже среднего значения: Копыта')

