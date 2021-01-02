"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

import timeit

array = [1, 3, 1, 3, 3, 3, 3, 3, 4, 1, 4, 4, 4, 4, 4, 4, 5, 1, 6, 6, 6, 6]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'func_1. Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'func_2. Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    new_array_dict = {}
    #  Получаем уникальные значения в списке array.
    unic_el = set(array)
    #  Считаем сколько рах каждое уникальное значение встречается в списке array.
    for el in unic_el:
        count_unic_el = array.count(el)
        #  Заполняем словарь парами: количество вхождений - элемент.
        new_array_dict[count_unic_el] = el
    # Сортируеи словарь по ключам, по количеству вхождений уникального элемента в список данный на входе.
    count_list = list(new_array_dict.keys())
    count_list_sort = sorted(count_list)
    #  В отсортированном списке берем максимальное количество вхождений уникального элемента.
    max_el = max(count_list_sort)
    #  В словаре с парами уник.значение - количество вхождений
    #  берем элемент с максимальным количеством вхлждений в заданный список.
    elem = new_array_dict[max_el]
    return f'func_3. Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_el} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print('Время работы функции func_1')
t1 = timeit.timeit(f"func_1()", setup="from __main__ import func_1", number=1000)
print(t1)
print('Время работы функции func_2')
t2 = timeit.timeit(f"func_2()", setup="from __main__ import func_2", number=1000)
print(t2)

print('Время работы функции func_3')
t3 = timeit.timeit(f"func_3()", setup="from __main__ import func_3", number=1000)
print(t3)

'''
Время работы функции func_3 значительно меньше чем у остальных функции , значит она быстрее.
Быстрее за счет использования словарей и использования встроенных функций.
Таких как сортировка, нахождение максимального значения и подсчет элементов в словарях.
'''
