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

try:
    comp_number = int(input("Введите количество предприятий для расчета прибыли: "))
    companies = namedtuple("Company", ("comp_name quarter_1 quarter_2 quarter_3 quarter_4"))
except ValueError:
    print("Некорректный ввод ")
    exit()
name_profit_dict = {}


for n in range(comp_number):
    name = input("Введите название предприятия: ")
    profit = input("Через пробел введите поквартальную прибыль данного предприятия: ")
    profit_list = profit.split()
    try:
        company = companies(comp_name=name, quarter_1=int(profit_list[0]), quarter_2=int(profit_list[1]),
                            quarter_3=int(profit_list[2]), quarter_4=int(profit_list[3]))
    except ValueError:
        print("Некорректный ввод ")

    average = (company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4) / 4
    print(company, average)
    name_profit_dict.setdefault(name, average)
    print(name_profit_dict)

common = 0

for avg_profit in name_profit_dict.values():
    common += avg_profit

common = common/comp_number
more_avg = ''
less_avg = ''
print(f"Средняя годовая прибыль всех предприятий: {common}")
for comp_name, avg_profit in name_profit_dict.items():
    if avg_profit > common:
        more_avg = f"{more_avg} {comp_name}"
    else:
        less_avg = f"{less_avg} {comp_name}"

print(f"Предприятия, с прибылью выше среднего значения: {more_avg}")
print(f"Предприятия, с прибылью ниже среднего значения: {less_avg}")

