"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
from collections import Counter

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
    cash = {}
    key, value = 0, 0
    for el in array:
        if cash.get(el):
            cash[el] += 1
            if cash[el] > value:
                key, value = el, cash[el]
        else:
            cash[el] = 1
    return f'Чаще всего встречается число {key}, ' \
           f'оно появилось в массиве {value} раз(а)'


def func_4():
    num, count = 0, 0
    dict_count = {key: array.count(key) for key in array}
    for key, value in dict_count.items():
        if value > count:
            num, count = key, value
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {count} раз(а)'


def func_5():
    dict_count = Counter(array)
    max_count = dict_count.most_common()
    return f'Чаще всего встречается число {max_count[0][0]}, ' \
           f'оно появилось в массиве {max_count[0][1]} раз(а)'


#print(func_1())
#print(func_2())
#print(func_3())
#print(func_4())
#print(func_5())


print('1) ', end='')
print(
    timeit(
        'func_1()',
        setup='from __main__ import func_1',
        number=10000))

print('2) ', end='')
print(
    timeit(
        'func_2()',
        setup='from __main__ import func_2',
        number=10000))

print('3) ', end='')
print(
    timeit(
        'func_3()',
        setup='from __main__ import func_3',
        number=10000))

print('4) ', end='')
print(
    timeit(
        'func_4()',
        setup='from __main__ import func_4',
        number=10000))

print('5) ', end='')
print(
    timeit(
        'func_5()',
        setup='from __main__ import func_5',
        number=10000))


"""Результаты:
   Были добавлены функции func_3, func_4, func_5
   
   func_3 выполняет операции примерно за то же время, что и func_1, используя цикл for in list и 
   пополнение словаря, но немного ей уступает.
   func_1 осталась самой быстрой, используя тот же цикл for in list и стандартную ф-ю count().
   
   func_4 использует Dict Comprehension, цикл for in dict.items(), и по скорости она близка 
   к func_2, которая использует цикл for in list и стандартную ф-ю max().
   
   А func_5 оказалась в 2 раза медленнее, чем func_1, но самой короткой по кол-ву строк кода.
   """