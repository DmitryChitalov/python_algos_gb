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


def func_3():
    l_ss = sorted(array)
    l_cur_elm = l_ss[0]
    l_cur_ind = 0
    l_cur_max = 0
    l_max_elm = l_ss[0]
    l_max_ind = 0
    l_max_max = 0
    i = 0
    for el in l_ss:
        if el == l_cur_elm:
            l_cur_max += 1
            if l_cur_max > l_max_max:
                l_max_elm = el
                l_max_ind = i
                l_max_max = l_cur_max
        else:
            l_cur_elm = el
            l_cur_ind = i
            l_cur_max = 1
        i += 1
    return f'Чаще всего встречается число {l_max_elm}, ' \
           f'оно появилось в массиве {l_max_max} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(timeit('func_1()', setup='from __main__ import func_1', number=10000))
print(timeit('func_2()', setup='from __main__ import func_2', number=10000))
print(timeit('func_3()', setup='from __main__ import func_3', number=10000))
# У меня получилось реализовать более быстрый вариант(функция func_3()).
# Сложность первых двух функций - это O(n**2), плюс O(n) для func_2().
# У меня же идет сортировка, у которой сложность
# от O(n) до O(n**2)(зависит от данных), плюс O(n).
# Оценка по timeit показывает самое быстрое время
# у третьей функции.
# В общем случае (или в большинстве случаев для разных данных),
# третий вариант будет быстрее.

