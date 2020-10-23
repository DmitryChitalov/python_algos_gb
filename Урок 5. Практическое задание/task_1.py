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

res = namedtuple('Company', 'id name_company product_type staff_size')

# ################################
# ##### обьект -> компания 1 #####
ARKO = res(id=1,
           name_company='Arko',
           product_type='Mobili',
           staff_size=1000)

# ################################
# ##### обьект -> компания 2 #####
DOC = res(id=2,
          name_company="DOC",
          product_type="pezzi di mobili",
          staff_size=500)
# ################################
print('_' * 20, ARKO, '_' * 20)
for data in ARKO:
	print(data, end=' ')
print()
print('_' * 20, DOC, '_' * 20)
for data in DOC:
	print(data, end=' ')


def calc():
	my_var = "Company"
	n = int(input("Введите кол-во предприятий: "))
	companies = namedtuple(
		my_var,
		"name period_1 period_2 period_3 period_4")
	profit_medium = {}

	for comp in range(n):
		company = companies(
			name=input("Введите название компании: "),
			period_1=int(input("period 1: ")),
			period_2=int(input("period 2: ")),
			period_3=int(input("period 3: ")),
			period_4=int(input("period 4: "))
		)

		profit_medium[company.name] = (company.period_1 + company.period_2
		                               + company.period_3 + company.period_4) / 4

	total_aver = 0
	for val in profit_medium.values():
		total_aver += val

	total_aver = total_aver / n

	for k, v in profit_medium.items():
		if v > total_aver:
			print(f"{k} прибыль выше среднего")
		elif v < total_aver:
			print(f"{k} прибыль ниже среднего")
		elif v == total_aver:
			print(f"{k} средняя прибыль")


calc()
