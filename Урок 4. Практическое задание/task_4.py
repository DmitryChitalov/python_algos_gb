"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

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


print(func_1())
print(func_2())


def func_3():
    from collections import Counter
    count = Counter(array).most_common()
    return f'Самое часто втречающееся число в массиве - {count[0][0]}, оно появилось в массиве {count[0][1]} раз'


print(func_3())


def func_4():
    res = max(array, key=array.count)
    return f'Самое часто втречающееся число в массиве - {res}, оно появилось в массиве {array.count(res)} раз'


print(func_4())

from timeit import timeit

print(timeit('func_1()', setup='from __main__ import func_1', number = 100000))
print(timeit('func_2()', setup='from __main__ import func_2', number = 100000))
print(timeit('func_3()', setup='from __main__ import func_3', number = 100000))
print(timeit('func_4()', setup='from __main__ import func_4', number = 100000))

'''
0.24944091599999998
0.279151134
0.532375144
0.22307405199999986

Функция func_4 самая быстрая
функция func_3 катастрофически медленная
'''