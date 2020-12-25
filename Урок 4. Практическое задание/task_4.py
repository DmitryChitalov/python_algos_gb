"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from timeit import timeit
from random import randint

# array = [1, 3, 1, 3, 4, 5, 1]
array = [randint(1,15) for el in range(100)]



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
    new_ar = [array.count(el) for el in array]
    max_f = max(new_ar)
    return f'Чаще всего встречается число {array[new_ar.index(max_f)]}, ' \
           f'оно появилось в массиве {max_f} раз(а)'


def func_4():
    array.sort()
    counts = 0
    for el in array:
        if array.count(el)>counts:
            max = el
            counts = array.count(el)
    return f'Чаще всего встречается число {max}, ' \
           f'оно появилось в массиве {counts} раз(а)'



print (timeit('func_1()','from __main__ import func_1',number=10000))
print (timeit('func_2()','from __main__ import func_2',number=10000))
print (timeit('func_3()','from __main__ import func_3',number=10000))
print (timeit('func_4()','from __main__ import func_4',number=10000))


"""
Выводы:
Сделал 2 попытки ускорить функцию
1 вариант - func_3 представляет собой по сути func_2 переписанный с помощью 
    генераторного выражения
    
2 вариант - func_4 по сути func_1 но с отсортированным списком

И то и другое дало небольшое увеличение скорости выполнения

    Результаты измерений:
        1.128126187 -- 1я функция
        1.179355681 -- 2я функция
        1.1153665819999996 -- 3я функция
        1.078509694 -- 4я функция
"""