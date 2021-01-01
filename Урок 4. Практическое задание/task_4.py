"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Ответ: нет смылса перебирать весь массив, где для одного числа проверять
количество вхождений по несколько раз, поэтому оставляем только
по одному элементу используя set.

Кстати, у всех функций есть один недостаток, поэтому задание необхлдимо
переформулировать, а функции исправить.
"""

from timeit import timeit
from random import randint

# Возьмем список размером побольше
array = [randint(1, 11) for _ in range(100)]


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


def func_3(obj: list) -> str:
    max_count = 0
    num = 0
    for i in set(obj):
        if (cnt := obj.count(i)) > max_count:
            num = i
            max_count = cnt
    return f'Чаще всего встречается число {num}, 'f'оно появилось в массиве {max_count} раз(а)'


if __name__ == '__main__':
    print(func_1())
    print(func_2())
    print(func_3(array))
    print(timeit('func_1()', number=10000, globals=globals()))
    print(timeit('func_2()', number=10000, globals=globals()))
    print(timeit('func_3(array)', number=10000, globals=globals()))
