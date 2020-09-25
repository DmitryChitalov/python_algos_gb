"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
"""
Результаты профилировки через timeit: 
0.1570783
0.2227505
функция func_1() работает быстрее

Свое решение искал долго, пробывал решить через словарь, но добился только второго места по скорости,
удалось решить с помощью google(я делал попытки использовать функцию max, но они оказались не на столько удачными).
С таким return func_3  по скорости равна func_3:
0.1598761 - func_1()
0.22291060000000001
0.15885319999999997 - func_3 
 но если не выводить количество вхождений элемента в массив то func_3 выиграет:
0.1423886 - func_1()
0.22452369999999996
0.12970320000000007 - func_3 
"""
import timeit

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
    el = max(array, key=array.count)
    return f'Чаще всего встречается число {el}, ' \
           f'оно появилось в массиве {array.count(el)} раз(а)'


# print(func_1())
# print(func_2())
# print(func_3())
print(timeit.timeit("func_1()", setup="from __main__ import func_1", number=100000))
print(timeit.timeit("func_2()", setup="from __main__ import func_2", number=100000))
print(timeit.timeit("func_3()", setup="from __main__ import func_3", number=100000))
