"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple


def tax_report():
    v_title = "Company"
    n = int(input("Введите количество предприятий: "))
    companies = namedtuple(
        v_title,
        " name period_1 period_2 period_3 period_4")
    aver_revenue = {}

    for i in range(n):
        company = companies(
            name=input("Введите название компании: "),
            period_1=int(input("Введите прибыль за первый квартал: ")),
            period_2=int(input("Введите прибыль за второй квартал: ")),
            period_3=int(input("Введите прибыль за третий квартал: ")),
            period_4=int(input("Введите прибыль за четвертый квартал: "))
        )

        aver_revenue[company.name] = (
                                             company.period_1 + company.period_2 + company.period_3 + company.period_4) / 4

    total_revenue = 0
    for c_value in aver_revenue.values():
        total_revenue += c_value
    total_revenue = total_revenue / n

    print("Средняя общая прибыль:", total_revenue)

    for c_key, c_value in aver_revenue.items():
        if c_value > total_revenue:
            print(f"{c_key} - прибыль выше среднего")
        elif c_value < total_revenue:
            print(f"{c_key} - прибыль ниже среднего")
        elif c_value == total_revenue:
            print(f"{key} - средняя прибыль")


tax_report()

"""
Введите количество предприятий: 3
Введите название компании: Amdocs
Введите прибыль за первый квартал: 110
Введите прибыль за второй квартал: 130
Введите прибыль за третий квартал: 125
Введите прибыль за четвертый квартал: 140
Введите название компании: JNetix
Введите прибыль за первый квартал: 90
Введите прибыль за второй квартал: 150
Введите прибыль за третий квартал: 110
Введите прибыль за четвертый квартал: 99
Введите название компании: Comverce
Введите прибыль за первый квартал: 120
Введите прибыль за второй квартал: 90
Введите прибыль за третий квартал: 85
Введите прибыль за четвертый квартал: 100
Средняя общая прибыль: 112.41666666666667
Amdocs - прибыль выше среднего
JNetix - прибыль ниже среднего
Comverce - прибыль ниже среднего
"""
