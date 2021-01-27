"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from timeit import timeit
array = [1, 3, 1, 3, 4, 5, 1, 4, 1, 5, 6, 1]


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
    set_3 = set(array)
    m = 0
    num = 0
    for i in set_3:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(timeit("func_1()", globals=globals(), number=1000))
print(timeit("func_2()", globals=globals(), number=1000))
print(timeit("func_3()", globals=globals(), number=1000))

'''
Решение под номером один быстрее из-за того, что там меньше операций
со списком. Постарался улучшить данную реализацию, заметив, что при больших
списках со многими повторениями нерационально каждый раз делать цикл по
одним и тем же числам, после преобразования в set время выполнения функции уменьшилось
Для array = [1, 3, 1, 3, 4, 5, 1, 4, 1, 5, 6, 1] и number=1000
    func_1 = 0.0030685999999999977
    func_2 = 0.004092600000000002
    func_3 = 0.001972499999999995
'''