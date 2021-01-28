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
import random

#array = [1, 3, 1, 3, 4, 5, 1]
array = [random.randrange(0,10) for i in range(100)]

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
    max_list = Counter(array).most_common(1)[0]
    return  f'Чаще всего встречается число {max_list[0]}, ' \
           f'оно появилось в массиве {max_list[1]} раз(а)'

print(func_1())
print(func_2())
print(func_3())
print('Замеры timeit:')
print('func_1(): ', timeit('func_1()', globals=globals(), number=1000))
print('func_2(): ', timeit('func_2()', globals=globals(), number=1000))
print('func_3(): ', timeit('func_3()', globals=globals(), number=1000))

"""
Количество элементов списка array зависит на скорость выполнения функций.
Так например, 
в списке длиной в 10 элементов замеры func_3 отрабатывает дольше всего:
func_1():  0.003749500000000003
func_2():  0.004088700000000001
func_3():  0.007133500000000001

в списке длиной в 100 элементов замеры timeit func_3 самая быстрая:
func_1():  0.1623489
func_2():  0.17178069999999998
func_3():  0.010588700000000006

Но в любом случае проигрывает func_2, так как в ней создается новый массив  
"""

