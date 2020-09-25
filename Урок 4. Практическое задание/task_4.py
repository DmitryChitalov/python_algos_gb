"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import hashlib
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 5, 5, 5]


def my_func():
    new_dict, max_count, num = {}, 0, 0
    for el in array:
        if new_dict.get(el):
            new_dict[el] = new_dict.get(el) + 1
            if new_dict.get(el) > max_count:
                max_count = new_dict.get(el)
                num = el
        else:
            new_dict[el] = 1
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {max_count} раз(а)'


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


print(f'Массив: {array}')
print(func_1())
print(func_2())
print(my_func())
print(f'func_1: {timeit("func_1()", setup="from __main__ import func_1", number=100000)}')
print(f'func_2: {timeit("func_2()", setup="from __main__ import func_2", number=100000)}')
print(f'my_func: {timeit("my_func()", setup="from __main__ import my_func", number=100000)}')

"""
Попытался написать свою фун-ию, но быстрее чем func_1 она не получилась и ничего другого к сожалению придумать
не успеваю :(
"""
