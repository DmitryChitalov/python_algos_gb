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



while True:
    try:
        num_of_comp = int(input('Введите количество предприятий для расчета прибыли: '))
    except ValueError:
        print('Вы ввели неверное значение. Попробуйте еще раз, используя цифровой ввод.')
        continue
    break


company_ies = namedtuple('company', 'name profit')
list_of_companies = []
common_profit = 0


for i in range(num_of_comp):
    comp_name = input(f'Введите название {i+1}-го предприятия: ')
    profit = list(map(int, input('Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): ').split()))
    list_of_companies.append(company_ies(name=comp_name, profit=profit))


for company in list_of_companies:
    common_profit += sum(company.profit)

profit_avg = common_profit / num_of_comp
print(f'Средняя годовая прибыль всех предприятий: {profit_avg}')

comp_above_avg = list(filter(lambda x: sum(x.profit) > profit_avg, list_of_companies))
comp_below_avg = list(filter(lambda x: sum(x.profit) < profit_avg, list_of_companies))

print(f"Предприятия, с прибылью выше среднего значения: {', '.join([x.name for x in comp_above_avg])}")
print(f"Предприятия, с прибылью ниже среднего значения: {', '.join([x.name for x in comp_below_avg])}")













