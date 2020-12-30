"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from collections import Counter
from timeit import timeit

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
    most_common_el = Counter(array).most_common(1)
    return f'Чаще всего встречается число {most_common_el[0][0]}, '\
           f'оно появилось в массиве {most_common_el[0][1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit("func_1()", setup="from __main__ import func_1, array", number=1000))
print(timeit("func_2()", setup="from __main__ import func_2, array", number=1000))
print(timeit("func_3()", setup="from __main__ import func_3, array", number=1000))

"""
Временной анализ трёх функций показал, что уменьшить время решения задачи использованием модуля collections
не удалось. Это связано с тем, что класс Counter использует словарь для создания списка кортежей, а значит хеширование,
которое увеличивает время. Из разбора домашнего задания стало понятно, что лучшим вариантом решения данной задачи 
стало бы использование метода списка count, в качестве ключа для функции max(). Однако в данной реализации 
наиболее эффективным по времени является первый алгоритм, не использующий методы списка, увеличивающие время поиска.
"""

