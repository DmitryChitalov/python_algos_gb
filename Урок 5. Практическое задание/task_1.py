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
from collections import Counter

l_cnt_cmp = int(input("Введите количество предприятий для подсчета: "))
l_obj = Counter()
l_obj_f = Counter()

for i in range(l_cnt_cmp):
    l_cmp_name = str(input("Введите название Компании: "))
    l_cmp_fund = str()
    for ifunds in range(4):
        l_cmp_fund = l_cmp_fund + ' ' + str(input("Введите прибыль за " + str(ifunds+1) + "квартал для " + l_cmp_name + " = "))
    l_obj[l_cmp_name] += 1
    l_obj_f[l_cmp_name] += 1
    l_cmp_fund = l_cmp_fund[1:]
    l_obj[l_cmp_name] = l_cmp_fund

for i_cmp in l_obj:
    l_sum_cmp = l_obj[i_cmp].split(" ")
    l_sum_cmp_f = int(0)
    for i_sum_cmp in range(len(l_sum_cmp)):
        l_v = int(l_sum_cmp[i_sum_cmp])
        l_sum_cmp_f = l_v + l_sum_cmp_f
    l_obj_f[i_cmp] = l_sum_cmp_f

l_cmp_avg_f = int(0)
for i_cmp_avg_f in l_obj_f:
    l_cmp_avg_f = l_obj_f[i_cmp_avg_f] + l_cmp_avg_f

l_cmp_avg_f = l_cmp_avg_f / len(l_obj)

print("Средняя годовая прибыль компаний = " + str(l_cmp_avg_f))

l_cmp_name_max = str("Компании с годовой прибылью больше средней - ")
for i_max_f in l_obj_f:
    if l_obj_f[i_max_f] > l_cmp_avg_f:
        l_cmp_name_max = l_cmp_name_max + i_max_f

print(l_cmp_name_max)

l_cmp_name_min = str("Компании с годовой прибылью меньше средней - ")
for i_min_f in l_obj_f:
    if l_obj_f[i_min_f] < l_cmp_avg_f:
        l_cmp_name_min = l_cmp_name_min + " " + i_min_f

print(l_cmp_name_min)
"""
from collections import namedtuple


def calc():
    my_var - "company"
    n = int(input("Введите количество предприятий: "))
    companies = namedtuple(
        my_var,
        " name_period_1 period_2 period_3 period_4")
    profit_aver = {}
    
    for i in range(n):
        company = companies(
            name=input("Введите название предприятия: "), period_1=int(
                input("Введите прибыль за первый квартал: ")), period_2=int(
                input("Введите прибыль за второй квартал: ")), period_3=int(
                input("Введите прибыль за третий квартал: ")), period_4=int(
                    input("Введите прибыль за четвёртый квартал: ")))
                
        profit_aver[company.name] = (
            company.period_1 + company.period_2 +
            company.period_3 + company.period_4) / 4
        
    total_aver = 0
    for value in profit_aver.values():
        total_aver += value
    total_aver = total_aver / n
    
    for key, value in profit_aver.items():
        if value > total_aver:
            print(f"{key} - прибыль выше среднего")
        elif value < total_aver:
            print(f"{key} - прибыль ниже среднего")
        elif value == total_aver:
            print(f"{key} - прибыль средняя")
            
calc()
#  Выше пример кода от преподавателя.

"""