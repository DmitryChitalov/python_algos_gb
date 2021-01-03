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
from collections import  deque, namedtuple

def enterprises():
    d = deque()
    count_enterprises = int(input("Введите количество предприятий для расчета прибыли: "))
    for i in range(count_enterprises):
        enterprise_name = input("Введите название предприятия: ")
        enterprise_profit = input("Через пробел введите прибыль данного предприятия\n"
            "за каждый квартал(Всего 4 квартала): ").split()
        pseudo_class = namedtuple('Enterprise', 'name first_quater second_quater third_quater fourth_quater total_profit')
        obj = pseudo_class(
            name=enterprise_name,
            first_quater = int(enterprise_profit[0]),
            second_quater = int(enterprise_profit[1]),
            third_quater = int(enterprise_profit[2]) ,
            fourth_quater = int(enterprise_profit[3]),
            total_profit = int(enterprise_profit[0]) + int(enterprise_profit[1])
                + int(enterprise_profit[2]) + int(enterprise_profit[3])
        )
        d.appendleft(obj)
    average_profit = 0
    for i in range(len(d)):
        average_profit += d[i].total_profit
    average_profit /= len(d)
    less_than_average = []
    more_than_average = []
    for i in range(len(d)):
        if d[i].total_profit > average_profit:
            more_than_average.append(d[i].name)
        else:
            less_than_average.append(d[i].name)
    print("Средняя годовая прибыль всех предприятий: ", average_profit)
    print("Предприятия, с прибылью выше среднего значения: ", more_than_average)
    print("Предприятия, с прибылью ниже среднего значения: ", less_than_average)

enterprises()



