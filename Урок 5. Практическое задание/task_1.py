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

COMPANY = namedtuple('Company', 'name q1 q2 q3 q4')
count_comp = int(input('Введите количество предприятий для расчета прибыли:  '))
company_list = []
income_y_dict = {}
for i in range(count_comp):
    name = input('Введите название предприятия:  ')
    income_str = input('через пробел введите прибыль данного предприятия \n ' +
                       'за каждый квартал (Всего 4 квартала):  ')
    income = list(map(float, income_str.split()))
    my_company = COMPANY(name=name, q1=income[0], q2=income[1], q3=income[2], q4=income[3])
    company_list.append(my_company)
for my_company in company_list:
    income_year = my_company.q1+my_company.q2+my_company.q3+my_company.q4
    income_y_dict[my_company.name] = income_year

avg_income = sum(income_y_dict.values()) / count_comp

print(f'Средняя годовая прибыль всех предприятий: {avg_income}')
print('Предприятия, с прибылью выше среднего значения: ',
      [name for name, inc in income_y_dict.items() if inc > avg_income])
print('Предприятия, с прибылью ниже среднего значения: ',
      [name for name, inc in income_y_dict.items() if inc <= avg_income])
