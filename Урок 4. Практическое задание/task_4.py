"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
"""Третий вариант написал через встроенную функцию max, но прироста в скорости не произошло,
хотя в первых двух есть циклы - O(n).
Все три функции выполняются за одно и тоже время (есть небольшая погрешность), при этом 
ни увеличение длины исходного листа, ни количество повторений выполнения функций на время значительно не влияют."""

from timeit import timeit
import random

array = [random.randrange(1, 50, 1) for i in range(750)]


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
    count_num = max(array, key=array.count)
    return f'Чаще всего встречается число {count_num}'


print(func_1())
print(func_2())
print(func_3())
print()

functions = ["func_1", "func_2", "func_3"]
setup_data = "from __main__ import func_1, func_2, func_3"

for fn in functions:
    print(f'Время выполнения функции {fn}',
          timeit(fn, setup=setup_data))
