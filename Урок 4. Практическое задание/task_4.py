"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.


Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым

"""

from timeit import timeit
import collections

array = [1, 3, 1, 3, 4, 5, 1]

@@ -36,6 +40,35 @@ def func_2():
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

for i in range(1, 1000): # увеличим размер массива
    array.append(7)

print(func_1())
print(func_2())


###########################################################################################3
def max_coll():
    counter = collections.Counter(array)
    key_max = counter.most_common()
    return key_max[0][0], key_max[0][1]


print("решение через Collections")
max_coll_el, max_coll_cnt_el = max_coll()
print(f'Чаще всего встречается число {max_coll_el}, оно появилось в массиве {max_coll_cnt_el} раз(а)')

print("-------------- замеры --------------------------")
print("func_1", timeit('func_1()', setup='from __main__ import func_1, array', number=10000))
print("func_2", timeit('func_2()', setup='from __main__ import func_2, array', number=10000))
print("max_coll", timeit('max_coll()', setup='from __main__ import max_coll, array', number=10000))

"""
-------------- замеры --------------------------
func_1 14.0197108
func_2 17.010997
max_coll 0.5865653000000002
самый быстрый способ поиска элемента в массиве - через модуль Collections
