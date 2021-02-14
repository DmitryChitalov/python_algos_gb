"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit
import collections

array = [1, 3, 1, 3, 4, 5, 1, 2, 3, 4, 5]


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
    counter = collections.Counter(array)
    key_max = counter.most_common()
    return f'Чаще всего встречается число {key_max[0][0]}, ' \
           f'оно появилось в массиве {key_max[0][1]} раз(а)'

def func_4():
    numb = max(array, key=array.count)
    return f'Чаще всего встречается число {numb}, ' \
           f'оно появилось в массиве {array.count(numb)} раз(а)'

print(func_1())
print(timeit.timeit("func_1()", setup="from __main__ import func_1, array", number=10000))

print(func_2())
print(timeit.timeit("func_2()", setup="from __main__ import func_2, array", number=10000))

print(func_3())
print(timeit.timeit("func_3()", setup="from __main__ import func_3, array", number=10000))

print(func_4())
print(timeit.timeit("func_4()", setup="from __main__ import func_4, array", number=10000))
#func_2 Самая медленная, func_4 самая быстрая