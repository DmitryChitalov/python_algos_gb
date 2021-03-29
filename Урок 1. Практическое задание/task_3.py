"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
# companies_info = {'name': , ammount}
companies_info = {'Ford': 900, 'Tesla': 800, 'Mercedes': 900, 'Nokia': 800, \
			'Yandex': 520, 'Mil.ru Group': 800}

# оба решения учитывают, что годовая прибыль может быть равная - тогда в топ 3 попадает компания,
	 # которая идет первая в хранилище (хранилище не отсортированное - поэтому мб выведена разная 
	 # последовтальность названий компани у решений)


def find_top_profit_1(comp_info_dict):	# сложность алгоритма - O(n) - линейная
	max1 = 0
	max2 = 0
	max3 = 0
	comp_max_amount = [i for i in range(3)]	 # O(1)
	for name, amount in comp_info_dict.items():	 # O(n) 
		#  comp_info_dict.items() -  O(1)
		if amount > max1:
			max1 = amount
			comp_max_amount[0] = name
		elif amount > max2:
			max2 = amount
			comp_max_amount[1] = name
		elif amount > max3:
			max3 = amount
			comp_max_amount[2] = name
	return comp_max_amount


def find_top_profit_2(comp_info_dict):	# сложность алгоритма - # O(n) 
	comp_max_amount = []  # O(1)

	list_amount = list(comp_info_dict.values())  # O(n) 

	max1 = max(list_amount)  # O(n) 
	list_amount.remove(max1)  # O(n) 
	max2 = max(list_amount)  # O(n) 
	list_amount.remove(max2)  # O(n) 	
	max3 = max(list_amount)	 # O(n) 
	list_amount.remove(max3)  # O(n)

	for name, amount in comp_info_dict.items():  # O(n) # comp_info_dict.items() - сложность O(1)
		# print(name, amount)
		if len(comp_max_amount) == 3:  # O(1)
			break
		elif amount == max1 or amount == max2 or amount ==max3:
			comp_max_amount.append(name)  # O(1)
		# else:
		# 	print('smth wrong')
	return comp_max_amount


# решение похоже на 2ое, но чуть инетересней
def find_top_profit_3(comp_info_dict):	# сложность алгоритма - O(n)
	list_max_amount = []
	comp_name_max_amount = []	
	list_amount = list(comp_info_dict.values())  # O(n), n - длина словаря

	for i in range(3):  # O(n=3) = O(1) - константа
		list_max_amount.append(max(list_amount))  # O(n) 
		val_remove = list_max_amount[i]
		list_amount.remove(val_remove)  # O(n) 
	for name, amount in comp_info_dict.items():  # O(n) 
		if len(comp_name_max_amount) == 3:
			break
		elif amount in list_max_amount:  # O(n)= O(1) - тк n=3, по задани нужно найти топ 3 
			comp_name_max_amount.append(name)  # O(1)
		# else:
		# 	print('smth wrong')
	return comp_name_max_amount

# если считала правильно, то все мои решения имееют сложностью O(n)
# считаю, что первое решение эффективне из-за отсутствия большого применения встроенных ф-ций, 
	# имеющих сложность O(n) и наглядности кода

print('1 решение - Список компаний с наибольшей годовой прибылью:', find_top_profit_1(companies_info), '\n')
print('2 решение - Список компаний с наибольшей годовой прибылью:', find_top_profit_2(companies_info), '\n')
print('3 решение - Список компаний с наибольшей годовой прибылью:', find_top_profit_3(companies_info), '\n')

