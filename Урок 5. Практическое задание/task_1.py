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
########################################################################################################################

from collections import defaultdict

info = defaultdict(int)


def information(n):
    if n == 0:
        return
    firm_name = input('Введите название предприятия: ')
    profit = sum([int(i) for i in input('Введите прибыль данного предприятия за каждый квартал: ').split()]) / 4
    info[firm_name] = profit
    return information(n-1)


firms = int(input('Введите количество предприятий для расчета прибыли: '))
information(firms)
average_profit = (sum(info.values()) / firms)
print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
high = [a[0] for a in info.items() if a[1] > average_profit]
print(f"Предприятия, с прибылью выше среднего значения: {', '.join(high)}")
low = [b[0] for b in info.items() if b[1] < average_profit]
print(f"Предприятия, с прибылью ниже среднего значения: {', '.join(low)}")


