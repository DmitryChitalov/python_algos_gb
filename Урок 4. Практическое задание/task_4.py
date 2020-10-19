"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1]
def func_my(array):
    print (f'Чаще всего встречается число {list(Counter(array))[:1]}' \
            f'оно появилось в массиве {max((value) for key, value in c.items())} раз(а)')

def func_ex():
    numb = max(array, key=array.count)
    return f'Чаще всего встречается число {numb}, ' \
           f'оно появилось в массиве {array.count(numb)} раз(а)'

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

import timeit

print(timeit.timeit("func_1()", setup="from __main__ import func_1")); #2.1097367
print(timeit.timeit("func_2()", setup="from __main__ import func_2")); #2.662277800000005
print(timeit.timeit("func_ex()", setup="from __main__ import func_ex")); #1.9497334999998
print(timeit.timeit("func_my(array)", setup="from __main__ import func_my, array")) #4.8393487

#Разница в реализации - наглядна, мною написаннный вариант в 2 раза медленнее... вариант с ключами словаря учту.