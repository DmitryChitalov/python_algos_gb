"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

"""
Через функцию max() выходит быстрее, но иногда первая функция показывает результаты лучше чем max()
"""


import timeit as t

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
	m = 0
	num = 0
	for i in array:
		count = array.count(i)
		if count > m:
			m = count
			num = i
	return f'Чаще всего встречается число {num}, ' \
	       f'оно появилось в массиве {m} раз(а)'


def func_2():
	new_array = []
	for el in array:
		count2 = array.count(el)
		new_array.append(count2)

	max_2 = max(new_array)
	elem = array[new_array.index(max_2)]
	return f'Чаще всего встречается число {elem}, ' \
	       f'оно появилось в массиве {max_2} раз(а)'


def func_3():
	numb = max(array, key=array.count)
	return f"Чаще всего встречается число {numb}, " \
	       f"оно появилось в массиве {array.count(numb)} раз(а)"


print(func_1())
print(func_2())
print(func_3())
# #########################################################

print("Проверка первой функции: ", t.repeat(stmt="func_1()",
                                            setup="from __main__ import func_1",
                                            timer=t.default_timer,
                                            repeat=4,
                                            number=10000))

result1 = t.repeat("func_1()",
                   "from __main__ import func_1",
                   t.default_timer,
                   4,
                   10000)

print(f"Среднее значение для {len(result1)} запусков: ", sum(result1) / len(result1))
# #########################################################

print("Проверка второй функции: ", t.repeat("func_2()",
                                            "from __main__ import func_2",
                                            t.default_timer,
                                            4,
                                            10000))

result2 = t.repeat("func_2()",
                   "from __main__ import func_2",
                   t.default_timer,
                   4,
                   10000)

print(f"Среднее значение для {len(result2)} запусков: ", sum(result2) / len(result2))
# ########################################################################

print("Проверка второй функции: ", t.repeat("func_3()",
                                            "from __main__ import func_3",
                                            t.default_timer,
                                            4,
                                            10000))


result3 = t.repeat("func_3()",
                   "from __main__ import func_3",
                   t.default_timer,
                   4,
                   10000)

print(f"Среднее значение для {len(result3)} запусков: ", sum(result3) / len(result3))
# #########################################################################


# def func_3():
# 	arr = [3, 5, 7, 29, 3, 12, 7, 3, 12, 9, 3]
# 	repeat_num = {}
# 	for i in arr:
# 		if arr.count(i) > 1:
# 			repeat_num[i] = arr.count(i)
# 	max_elem = [(k, v) for k, v in repeat_num.items() if v == max(arr.count(v))]
# print(func_3())

# конченный мозг не может сообразить как сделать еще один варриант поиска
# #######################################################################


