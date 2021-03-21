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

company = collections.namedtuple('Comp', "name period_1 period_2 period_3 period_4")

companies_set = dict()

num_of_companies = int(input("Введите количество предприятий для расчета прибыли: "))

# collecting all the companies
for i in range(num_of_companies):
    c_name = input("Введите название предприятия: ")
    p1, p2, p3, p4 = input(
        "Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ").split()
    companies_set[c_name] = company(name='ddd', period_1=int(p1), period_2=int(p2), period_3=int(p3), period_4=int(p4))

# calculating total profit
total_income = 0
for comp in companies_set:
    total_income += companies_set[comp].period_1 + companies_set[comp].period_2 + companies_set[comp].period_3 + \
                    companies_set[comp].period_4
print(f"Средняя годовая прибыль всех предприятий: {total_income}")

# calculating avg profit
avg_income = total_income / len(companies_set)

# final activity
for comp in companies_set:
    total = companies_set[comp].period_1 + companies_set[comp].period_2 + companies_set[comp].period_3 + companies_set[
        comp].period_4
    if total > avg_income:
        print(f"{comp} - прибыль выше среднего")
    elif total < avg_income:
        print(f"{comp} - прибыль ниже среднего")
    elif total == avg_income:
        print(f"{comp} - средняя прибыль")

# print(companies_set)
