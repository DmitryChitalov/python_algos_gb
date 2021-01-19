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

# number = int(input('Введите количество компаний для расчета:  '))
# companies = []
#
# for i in range(number):
#     company = input('Введите название:  ')
#     prof = input('Введите прибыль за 4 квартала через пробел:  ')
#     prof = prof.split()
#     template = namedtuple('companies', 'name prof_1q prof_2q prof_3q prof_4q')
#     data = template(
#         name=company,
#         prof_1q=prof[0],
#         prof_2q=prof[1],
#         prof_3q=prof[2],
#         prof_4q=prof[3],
#     )
#     companies.append(data)
# print(companies)


number = int(input('Введите количество компаний для расчета:  '))
companies = {}

for i in range(number):
    company = input('Введите название:  ')
    prof = input('Введите прибыль за 4 квартала через пробел:  ')
    prof = prof.split()
    template = namedtuple('companies', 'name prof_1q prof_2q prof_3q prof_4q')
    data = template(
        name=company,
        prof_1q=prof[0],
        prof_2q=prof[1],
        prof_3q=prof[2],
        prof_4q=prof[3],
    )
    companies[data.name] = int(data.prof_1q) + int(data.prof_2q) + int(data.prof_3q) + int(data.prof_4q)

total_av = 0
for i in companies.values():
    total_av += i
    total_av = total_av / number

print(f'Средняя годовая прибыль компаний {total_av}')
for i, y in companies.items():
    if y > total_av:
        print(f'Прибыль у компании "{i}" выше среднего, годовая прибыль равна {y}')
    elif y < total_av:
        print(f'Прибыль у компании "{i}" ниже среднего, годовая прибыль равна {y}')
    else:
        print(f'У компании "{i}" средняя прибыль')





