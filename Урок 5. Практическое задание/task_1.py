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

deq_obj = deque()  # -> deque(['b', 'c', 'd'])
number_of_businesses = int(input('Введите количество предприятий для расчета прибыли: '))

for number in range(number_of_businesses):
    new_dict = {}
    company_name = input('Введите название предприятия: ')
    quarter_1, quarter_2, quarter_3, quarter_4, = [
        int(n) for n in input('через пробел введите прибыль данного предприятия\n'
                              'за каждый квартал(Всего 4 квартала): ').split()]
    new_dict['company'] = company_name
    new_dict['profit_by_year'] = quarter_1 + quarter_2 + quarter_3 + quarter_4
    deq_obj.append(new_dict)

all_average = 0
num_of_comp = len(deq_obj)
for company in deq_obj:
    all_average += company['profit_by_year']
average_all_comp = all_average / num_of_comp

companies_with_profit_hire_average = []
for company in deq_obj:
    if company['profit_by_year'] > average_all_comp:
        companies_with_profit_hire_average.append(company['company'])

print('Средняя годовая прибыль всех предприятий:', average_all_comp)
print('Предприятия, с прибылью выше среднего значения: ', list(companies_with_profit_hire_average))
