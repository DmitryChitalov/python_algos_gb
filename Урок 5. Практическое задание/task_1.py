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

from collections import defaultdict, namedtuple

def company_average_profit():
    my_var = 'Company'
    n = int(input('Введите количество предприятий: '))
    company = namedtuple(my_var, 'name profit_period1 profit_period2 profit_period3 profit_period4')
    profit_average_dict = {}

    for i in range(n):
        companies = company(
            name=(input("Введите название компании: ")),
            profit_period1=int(input("Введите прибыль за первый квартал: ")),
            profit_period2=int(input("Введите прибыль за второй квартал: ")),
            profit_period3=int(input("Введите прибыль за третий квартал: ")),
            profit_period4=int(input("Введите прибыль за четверый квартал: ")),
        )

        profit_average_dict[companies.name] = (
         companies.profit_period1 + companies.profit_period2 + companies.profit_period3 + companies.profit_period4) / 4

    total_average = 0
    for value in profit_average_dict.values():
        total_average += value
    total_average = total_average / n
    print('Средняя прибыль = ', total_average)

    for name, value in profit_average_dict.items():
        if value > total_average:
            print(f"{name} - значение прибыли выше среднего")
        elif value < total_average:
            print(f"{name} - значение прибыли ниже среднего")
        elif value == total_average:
            print(f"{name} - средняя прибыль")


company_average_profit()


# Иное решение, не законченное, через defaultdict и namedtuple
# # создаем словарь на базе defaultdict с default = str
# dct = defaultdict(str)
#
#
# # ф-я заполняет словарь
# def create_dct(company_name, profit):
#     dct[company_name] = profit
#     return dct
#
#
# # Заполняем словарь Фирмами и Прибылью
# count_company = int(input('count company'))
# i = 0
# while i < count_company:
#     company_name = input('company name')
#     profit = input('profit')
#     # company_name = 'firma'
#     # profit = '235 345634 55 235'
#     i += 1
#     # create_dct(company_name=company_name, profit=profit)
#     print(create_dct(company_name=company_name, profit=profit))
#
# # Достаем в кортеж из (фирма,прибыль)
# # res = namedtuple('resume', 'name profit')
# # firms = res(dct.keys(), dct.values())
# # print(firms)
# ls = []
# for i in dct.items():
#     ls.append(i)
#
# print(ls)
#
# maxim = max(ls, key=lambda x: x[1])
# minim = min(ls,key=lambda x: x[1])
# print('max', maxim)
# print('min', minim)
