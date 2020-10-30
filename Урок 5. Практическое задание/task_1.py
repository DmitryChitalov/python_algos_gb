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


def calc():

    companies_count = int(input("Введите количество предприятий: "))
    companies = collections.defaultdict()
    for i in range(companies_count):
        name = input(f"Введите название предприятия {i+1}: ")
        profit = [int(input(f"Введите прибыль за {j+1}-й квартал: ")) for j in range(4)]
        companies[name] = sum(profit)
        print(companies)

    avg = sum(companies.values())/companies_count
    print(f"Средняя прибыль всех компаний за год: {avg}")

    for company in companies:
        print(company)
        if companies[company] >= avg:
            print(f"Компания: {company} имееет прибыль выше средней: {companies[company]}")
    for company in companies:
        if companies[company] < avg:
            print(f"Компания: {company} имеет прибыль ниже среднего: {companies[company]}")

calc()