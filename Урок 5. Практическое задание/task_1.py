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


def get_average_profit(count_enterprises):
    dict_enterprises = {}
    Enterprises = namedtuple("Enterprises", "profit profit_total")
    profit_all = 0
    for i in range(1, count_enterprises + 1):
        name = input("Введите название компании: ")
        str_profit = input("через пробел введите прибыль данного предприятия "
                           "за каждый квартал(Всего 4 квартала):")
        profit = [int(i) for i in str_profit.split()]
        enterprise = Enterprises(profit, sum(profit))
        profit_all = profit_all + enterprise.profit_total
        dict_enterprises[name] = enterprise

    return dict_enterprises, profit_all / count_enterprises


if __name__ == "__main__":
    count_enterprises = int(input("Введите количество предприятий для расчета прибыли: "))
    dict_enterprises, average_all = get_average_profit(count_enterprises)
    print(f'Средняя прибыль для всех компаний: {average_all}')
    print(
        f'Компании, у которых значение больше среднего: {[k for k, v in dict_enterprises.items() if v.profit_total >= average_all]}')
    print(
        f'Компании, у которых значение меньше среднего: {[k for k, v in dict_enterprises.items() if v.profit_total < average_all]}')
