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
from collections import defaultdict

'''
Это задание показалось сложней чем второее как по мне)
Так и не смог до конца решить заговстку в конце.
'''
company_count = int(input('Введите колчиство предприятий для рассчёта прибыли: '))

company_data = defaultdict(int)

i = 0
while i < company_count:
    company_name = input('Введите название компании: ')
    company_for_season_income = input(
        'Введите через пробел приль даннго предприятия за каждый квартал всего 4 квартала:')
    lst = company_for_season_income.split()
    company_data[company_name] = lst
    for k in company_data.values():
        for j in k:
            print(sum(j))
    i += 1


print(company_data)

