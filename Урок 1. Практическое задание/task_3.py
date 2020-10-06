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


company_list = [["google",500],["Apple",1000],["amazon",800],["yandex",100],["netflix",400]]




#Алгоритм 1
#O(n)

def keyFunc(item):
   return item[1]

def check_1(company_list):
	company_list_copy = company_list
	company_list_copy.sort(key = keyFunc, reverse = True)
	return(company_list_copy)

#new_company_list = check_1(company_list)

#print(new_company_list[0],new_company_list[1],new_company_list[2])


#Алгоритм 2
# O(n), так как тут вызвается цикл, где n - длина списка company_list
"""

top_3_list_v2 = []

top_3_list_v2.append(company_list[0])
"""
for n in company_list:
	if n[1] > top_3_list_v2[0][1]:
		top_3_list_v2.insert(0,n)
"""
for m in company_list:
	for idx, val in enumerate(top_3_list_v2):
		if m[1] > val[1]:
			top_3_list_v2.insert(idx,m)

print(top_3_list_v2)
"""

#Алгоритм 3
# O(n^3), так как тут трижды вызвается цикл, где n - длина списка company_list

company_list_copy = company_list

def check3(company_list):
	max_ = company_list[0]
	for n in company_list:
		for m in company_list:
			if max_[1]<m[1]:
				max_ = m
	return(max_)

top_3_list_v3 = []

while len(top_3_list_v3)<3:
	comp = check3(company_list_copy)
	top_3_list_v3.append(check3(company_list_copy))
	company_list_copy.remove(comp)

#print(top_3_list_v3)



#Вывод: алгоритм 1 эффективнее, потому что в нем доминирующую часть операций занимает нотация O(n), который производит меньше вычислений, чем O(n^3) или O(n^2)
