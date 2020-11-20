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

# стандартный подход

companies = {}
n = int(input("Количество фирм: "))
s = 0
for i in range(n):
    company_name = input(str(i + 1) + "ая компания: ")
    profit1 = int(input("Прибыль за 1 квартал: "))
    profit2 = int(input("Прибыль за 2 квартал: "))
    profit3 = int(input("Прибыль за 3 квартал: "))
    profit4 = int(input("Прибыль за 4 квартал: "))
    avg_profit = (profit1 + profit2 + profit3 + profit4)/4
    companies[company_name] = avg_profit
    s += avg_profit


avrg = s / n
print(f'Средний доход всех компаний {avrg}. Компании , у которых доход выше среднего: ')
for i in companies:
    if companies[i] > avrg:
        print(i)


#namedtuple

def profit_check():
    n = int(input("Введите количество предприятий: "))
    companies = namedtuple(
        'Company',
        " name period_1 period_2 period_3 period_4")
    profit_avr = {}

    for i in range(n):
        company = companies(
            name=input("Введите название предприятия: "), period_1=int(
                input("Введите прибыль за первый квартал: ")), period_2=int(
                input("Введите прибыль за второй квартал: ")), period_3=int(
                input("Введите прибыль за третий квартал: ")), period_4=int(
                    input("Введите прибыль за четвертый квартал: ")))

        profit_avr[company.name] = (
            company.period_1 + company.period_2 + company.period_3 + company.period_4) / 4

    total_avr = 0
    for value in profit_avr.values():
        total_avr += value
        total_avr = total_avr / n

    for key, value in profit_avr.items():
        if value > total_avr:
            print(f"{key} - прибыль выше среднего")
        elif value < total_avr:
            print(f"{key} - прибыль ниже среднего")
        elif value == total_avr:
            print(f"{key} - средняя прибыль")


profit_check()




