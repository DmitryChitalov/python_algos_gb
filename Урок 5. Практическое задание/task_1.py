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
from collections import deque

company_amount = int(input("Введите кол-во компаний: "))
company_info_deque = deque()
average_deque = deque()

while company_amount:
    company_name = input("Введите название предприятия: ")
    income = input("Через пробел введите прибыль данного предприятия "
                   "за каждый квартал(Всего 4 квартала): ")
    income = list(map(lambda x: int(x), income.split(" ")))
    income.insert(0, company_name)
    company_info_deque.append(income)
    company_amount -= 1

[average_deque.append([x[0], sum(x[1:])]) for x in company_info_deque]

average_income = 0
for x in average_deque:
    average_income += x[1]

average_income = average_income / len(average_deque)

print(f"Средняя годовая прибыль всех предприятий: {average_income}")

print("Предприятия, с прибылью выше среднего значения: ", end='')
for x in average_deque:
    if x[1] > average_income:
        print(x[0], end=' ')

print("\nПредприятия, с прибылью ниже среднего значения: ", end=' ')
for x in average_deque:
    if x[1] < average_income:
        print(x[0], end='')
