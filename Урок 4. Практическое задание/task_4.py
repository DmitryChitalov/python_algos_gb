"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import random
from timeit import timeit


# array = [1, 3, 1, 3, 4, 5, 1]
array = [random.randint(1, 10) for i in range(100)]

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
    dict_count = array
    dict_count.sort()
    el1 = dict_count[0]
    count = 0
    el_max = 0
    count_max = 0
    for el in dict_count:
        if el == el1:
            count += 1
            if count > count_max:
                count_max = count
                el_max = el
        else:
            count = 1
            el1 = el
            
    return f'Чаще всего встречается число {el_max}, ' \
           f'оно появилось в массиве {count_max} раз(а)'
            

print(array)
print(func_1())
print(
    timeit(
        'func_1()',
        setup='from __main__ import func_1',
        number=10000))
print(func_2())
print(
    timeit(
        'func_2()',
        setup='from __main__ import func_2',
        number=10000))
print(func_3())
print(
    timeit(
        'func_3()',
        setup='from __main__ import func_3',
        number=10000))

"""
Использовал сортировку и последовательно перебрал элементы, получилось значительно ускорить поиск числа

[6, 1, 1, 5, 1, 4, 7, 3, 2, 5, 9, 1, 2, 2, 3, 9, 10, 8, 6, 7, 9, 8, 4, 3, 3, 1, 5, 4, 8, 1, 1, 8, 3, 6, 6, 8, 8, 7, 2,
8, 4, 9, 6, 4, 2, 2, 2, 6, 1, 2, 1, 9, 5, 4, 4, 1, 10, 3, 9, 3, 2, 10, 3, 1, 4, 10, 4, 5, 8, 9, 10, 7, 4, 1, 6, 8, 8, 8,
9, 3, 2, 6, 3, 9, 10, 1, 3, 5, 3, 3, 4, 3, 5, 4, 5, 6, 3, 4, 10, 1]
Чаще всего встречается число 3, оно появилось в массиве 15 раз(а)
1.670672             <--- func_1()
Чаще всего встречается число 3, оно появилось в массиве 15 раз(а)
1.8559451000000002   <--- func_2()
Чаще всего встречается число 3, оно появилось в массиве 15 раз(а)
0.11723309999999998  <--- func_3()
"""