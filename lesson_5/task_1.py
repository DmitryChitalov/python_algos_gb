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

# import random

REP = namedtuple('Report', 'company_name income_1 income_2 income_3 income_4')
company_quantity = 0
reports = []

# reports = [REP(f'company_{i}', int(random.randint(1, 100)), int(random.randint(1, 100)), int(random.randint(1, 100)),
#                int(random.randint(1, 100))) for i in range(company_quantity)]

a = None
while type(a) is not int:
    try:
        a = int(input('Введите количество предприятий для расчета прибыли : '))
        company_quantity = a
    except ValueError:
        print('ошибка ввода')

for i in range(company_quantity):
    b = input('Введите Введите название предприятия: ')
    print(b)
    c = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()
    print(c)

    reports.append(REP(company_name=b, income_1=int(c[0]), income_2=int(c[1]), income_3=int(c[2]), income_4=int(c[3])))

sum_avg_income = 0
sum_income = 0
lst = []

for i in range(company_quantity):
    avg_income = (reports[i].income_1 + reports[i].income_2 + reports[i].income_3 + reports[i].income_4) / 4

    print(f'Средняя прибыль {reports[i].company_name} = {avg_income}')

    lst.append(avg_income)

    sum_income += avg_income

sum_avg_income = sum_income / company_quantity
print(f'Средняя прибыль всех предприятий  = {sum_avg_income}')

for i in range(company_quantity):
    if lst[i] < sum_avg_income:
        print(f'Средняя прибыль {reports[i].company_name} ({lst[i]}) меньше {sum_avg_income}')
    else:
        print(f'Средняя прибыль {reports[i].company_name} ({lst[i]}) больше или равна {sum_avg_income}')

# def get_avg_sum(nt: reports):
#     return sum(nt.)

# print(reports[0])

# REP_INCOMES = [REP(f"Report{i} company_name='company_1',
#                    income_1=10,
#                    income_2=20,
#                    income_3=30,
#                    income_4=40") for i in range(3)]
# for i in range(5):
#     print(f"Объект_{i}: ", REP_INCOMES[i])


# REP_INCOMES1 = REP.__class__  (company_name='company_1', income_1=10, income_2=20, income_3=30, income_4=40)


# for i in range(company_quantity):

# REP_INCOMES1 = REP(company_name='company_1', income_1=10, income_2=20, income_3=30, income_4=40)
# REP_INCOMES2 = REP(company_name='company_2', income_1=10, income_2=20, income_3=30, income_4=40)


# REP_INCOMES = REP(
#     company_name='company_1',
#     income_1=10,
#     income_2=20,
#     income_3=30,
#     income_4=40
# )

#    print(b)
#    c = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')

# print(REP_INCOMES1)
# print(REP_INCOMES2)
