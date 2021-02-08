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


from collections import namedtuple, deque, defaultdict

company_cnt = int(input('Введите количество предприятий для расчета прибыли: '))
company = namedtuple('companies', 'name quarter_1 quarter_2 quarter_3 quarter_4')
company_total_profit_dict = {}
sum_profit = 0

for i in range(company_cnt):
    company_name = input('Введите название компании: ')
    company_profit = input('Через пробел введите прибыль данного предприятия за каждый квартал: ').split()
    companies = company(
        name=company_name,
        quarter_1=int(company_profit[0]),
        quarter_2=int(company_profit[1]),
        quarter_3=int(company_profit[2]),
        quarter_4=int(company_profit[3])
    )
    company_total_profit_dict[companies.name] = (companies.quarter_1 +
                                                 companies.quarter_2 +
                                                 companies.quarter_3 +
                                                 companies.quarter_4)
for values in company_total_profit_dict.values():
    sum_profit += values
average_profit = sum_profit / company_cnt
print(f'Компания и годовая прибыль: {company_total_profit_dict}\n'
      f'Средняя годовая прибыль компаний: {round(average_profit, 2)}')
lower_list = []
upper_list = []
for key, val in company_total_profit_dict.items():
    if val >= average_profit:
        upper_list.append(key)
    else:
        lower_list.append(key)
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(upper_list)}\n'
      f'Предприятия, с прибылью ниже среднего значения: {", ".join(lower_list)}')

# # # # # another way (с небольшим отклонением от ТЗ) # # # # #
n = int(input('Введите количество компаний: '))

corp = defaultdict()
prof_c = deque()
unprof_c = deque()
all_profit = 0
quarter = 4

for i in range(n):
    name = input(f'\nВведите название {i + 1}й компании: ')
    profit = 0
    q = 1

    while q <= quarter:
        profit += float(input(f'Введите прибыль за {q}й квартал: '))
        q += 1
    corp[name] = profit
    all_profit += profit

mid_profit = all_profit / n

for i, item in corp.items():
    if item > mid_profit:
        prof_c.append(i)
    elif item < mid_profit:
        unprof_c.append(i)

print(f'\nСредняя прибыль для всех компаний составила: {mid_profit}')
print(f'Прибыль выше среднего у {len(prof_c)} компаний:  ')
for name in prof_c:
    print(name)
print(f'Прибыль ниже среднего у {len(unprof_c)} компаний:')
for name in unprof_c:
    print(name)
