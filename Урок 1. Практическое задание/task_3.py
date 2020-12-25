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

company = {
	'Mail': 2500,
	'Yandex': 3200,
	'Sber': 5400,
	'Rosneft': 3500,
	'Gazprom': 2700,
	'Cisco': 3250
}


def func1(dictionary):  # Сложность O(n*log n)
	profit = dictionary.values()
	profit = sorted(profit)
	profit = profit[-1:-4:-1]
	name = {key: value for key, value in dictionary.items() if value in profit}
	print(name)


def func2(dictionary):  # Сложность O(n)
	profit = [value for key, value in dictionary.items()]
	max1 = 0
	max2 = 0
	max3 = 0
	for i in range(len(profit)):
		if profit[i] > max1:
			max3 = max2
			max2 = max1
			max1 = profit[i]
		elif profit[i] > max2:
			max3 = max2
			max2 = profit[i]
		elif profit[i] > max3:
			max3 = profit[i]
	name = { key: value for key, value in dictionary.items() if value in [max1, max2, max3] }
	print(name)


func1(company)
func2(company)

# Использование функции func2 эфффективнее имет сложность O(n) т.к. не используется встроенная функция сортировки как в функции func1

