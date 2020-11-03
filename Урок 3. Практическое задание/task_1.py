"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time


def check_time(func):
	"""decorator"""

	def wraper(*args):
		start_check = time.time()
		return_func = func(*args)
		end_check = time.time()

		print(f"Процесс обработки операции занял: {round(end_check - start_check, 6)} сек.")
		return return_func

	return wraper


###########################
print("\nСоздание списка и словаря:")
print('_'*25)


@check_time
def fill_list(num):
	list_elem = []
	for elem in range(num):
		list_elem.append(elem * 30)
	return list_elem


@check_time
def fill_dict(num):
	dict_elem = {}
	for key in range(num):
		dict_elem[key] = key * 30
	return dict_elem


list_el = fill_list(10000)
dict_el = fill_dict(10000)
##########################
print("\nУдаление елементов:")
print('_'*20)


@check_time
def del_num_from_list(some_list):
	some_list.clear()


del_num_from_list(list_el)


@check_time
def del_from_dict(some_dict):
	some_dict.clear()


del_from_dict(dict_el)

print('\nВзятие елементов')
print('_'*20)

@check_time
def take_el_list(some_list):
	for i in range(len(some_list)):
		return some_list.index(some_list[i])


take_el_list(list_el)

@check_time
def take_el_dict(some_dict):
	for el in some_dict.keys():
		some_dict.get(el)


take_el_dict(dict_el)
