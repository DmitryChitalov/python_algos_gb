"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
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


print(func_1())
print(func_2())


print(timeit('func_1()', setup='from __main__ import func_1', number=10000))
print(timeit('func_2()', setup='from __main__ import func_2', number=10000))

# my solution:

'''
func_1 выполняется быстрее всего, func_2 на втором месте по скорости. Мое решение сработало, но, к сожалению, медленее
данных изначально - списки и правда быстрее словарей, с одной стороны, а с другой - нет решения из коробки для поиска 
ключа по значению, потому пришлось идти через ген. выражение, что замедлило выполнение.
'''

from collections import Counter

def func_3(array):
    count3 = Counter(array)
    val_res = max(count3.values())
    key_res = [key for key, val in count3.items() if val == val_res]
    return f'Чаще всего встречается число {key_res}' \
           f'Оно появилось {val_res} раз(а).'

print(func_3(array))


print(timeit('func_3(array)', setup='from __main__ import func_3, array', number=10000))