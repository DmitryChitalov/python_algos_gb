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


def aver_and_sum():
    com_name = "Company"
    a = int(input("Введите количество предприятий: "))
    companies = namedtuple(
        com_name,
        " name quarter1 quarter2 quarter3 quarter4")
    com_profit = {}
    aver_profit = {}

    for i in range(a):
        company = companies(
            name=input("Введите название предприятия: "),
            quarter1=int(input("Введите прибыль за первый квартал: ")),
            quarter2=int(input("Введите прибыль за второй квартал: ")),
            quarter3=int(input("Введите прибыль за третий квартал: ")),
            quarter4=int(input("Введите прибыль за четвертый квартал: ")))
        com_profit[company.name] = (company.quarter1 + company.quarter2 + company.quarter3 + company.quarter4)
        aver_profit[company.name] = (
            company.quarter1 + company.quarter2 + company.quarter3 + company.quarter4) / 4

    aver_total = 0
    for value in aver_profit.values():
        aver_total += value
    aver_total = aver_total / a
    print(com_profit)
    print(aver_total)

    for key, value in aver_profit.items():
        if value > aver_total:
            print(f"{key} - прибыль выше среднего")
        elif value < aver_total:
            print(f"{key} - прибыль ниже среднего")
        elif value == aver_total:
            print(f"{key} - прибыль равна")

aver_and_sum()
