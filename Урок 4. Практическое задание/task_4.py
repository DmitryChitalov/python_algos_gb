"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1]
count = {}


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


# мои варианты
non_Counter = """Counter()"""
setup = "from collections import Counter"

count = Counter(array)

print(func_1())
print(func_2())
print(count)

print(timeit.timeit("func_1()", setup="from __main__ import func_1", number=100000))
print(timeit.timeit("func_2()", setup="from __main__ import func_2", number=100000))
print(sum(timeit.repeat(non_Counter, setup=setup, number=100000)))

# Пока что мой вариант самый долгий, хотя сам год короткий
