"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
from collections import Counter
from random import randint

# array = [1, 3, 1, 3, 4, 5, 1]
array = [randint(1, 10) for i in range(100)]


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
    number, count = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {number}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(timeit('func_1()', globals=globals(), number=10000))
print(timeit('func_2()', globals=globals(), number=10000))
print(timeit('func_3()', globals=globals(), number=10000))


'''
Для представленного в примере массива третий вариант решения не эффективен,
так как на него уходит больше времени. Однако на больших массивах он работает 
намного быстрее первых 

2.3738970999999998
2.3524344000000004
0.12673640000000042

'''
