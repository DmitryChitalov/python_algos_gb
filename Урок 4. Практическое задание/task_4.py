"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
	m = 0
	num = 0
	for i in array:
		count = array.count(i)
		if count > m:
			m = count
			num = i
	return f'Чаще всего встречается число {num}, ' f'оно появилось в массиве {m} раз(а)'


def func_2():
	new_array = []
	for el in array:
		count2 = array.count(el)
		new_array.append(count2)

	max_2 = max(new_array)
	elem = array[new_array.index(max_2)]
	return f'Чаще всего встречается число {elem}, ' f'оно появилось в массиве {max_2} раз(а)'


def func_3():
	m = 0
	num = 0
	b = set(array)
	for i in b:
		count = array.count(i)
		if count > m:
			m = count
			num = i
	return f'Чаще всего встречается число {num}, ' f'оно появилось в массиве {m} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(
	f"func_1: {timeit.timeit('func_1()', 'from __main__ import func_1', number=1000)}"
)
print(
	f"func_2: {timeit.timeit('func_2()', 'from __main__ import func_2', number=1000)}"
)
print(
	f"func_3: {timeit.timeit('func_3()', 'from __main__ import func_3', number=1000)}"
)
'''
func_1: 0.0031077080057002604
func_2: 0.004189083992969245
func_3: 0.002420874952804297
За счет прохода только по уникалным элементам массива func_3 удалось незначительно ускорить программу (с применением множества)
'''

