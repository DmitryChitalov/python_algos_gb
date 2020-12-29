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



# Самая быстрая функция. Она быстрее всех остальных потому что используется встроенная функция set
# и из-за того что это множество, убираются дубликаты и мы проходим циклом только по уникальным значениям


def func_3():
    my_dict = set(array)
    max_num = 0
    for i in my_dict:
        if array.count(i) > max_num:
            max_num = i
    return f'Чаще всего встречается число {max_num}, ' \
           f'оно появилось в массиве {array.count(max_num)} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit(stmt='func_1()', setup='from __main__ import func_1,array', number=100000))
print(timeit(stmt='func_2()', setup='from __main__ import func_2,array', number=100000))
print(timeit(stmt='func_3()', setup='from __main__ import func_3,array', number=100000))

