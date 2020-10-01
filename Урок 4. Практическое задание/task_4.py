"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 1, 3, 4, 5, 1, 6, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1]


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
    return f'Чаще всего встречается число {numb}, ' \
           f'оно появилось в массиве {array.count(numb)} раз(а)'


print(f'func_1 = {func_1()}')
print(f'func_2 = {func_2()}')
print(f'func_3 = {func_3()}')

print(f'*' * 75)

print(f'func_1 = '
      f'{timeit("func_1()", setup="from __main__ import func_1")}')

print(f'func_2 = '
      f'{timeit("func_2()", setup="from __main__ import func_2")}')

print(f'func_3 = '
      f'{timeit("func_3()", setup="from __main__ import func_3")}')

'''
func_2 Самая медленная, func_3 чуть быстрее чем func_1
'''
