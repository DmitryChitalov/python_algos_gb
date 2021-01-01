"""
Задание 4.
Приведены два алгоритма. В них определяется число, которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit
array = [1, 3, 1, 3, 4, 5, 1, 3, 6, 1, 10, 1, 6, 1, 5, 6, 1, 1, 4, 6, 1]


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
    max_v = max(set(array), key=array.count)
    return f'Чаще всего встречается число {max_v}, ' \
           f'оно появилось в массиве {array.count(max_v)} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print("func_1", timeit.timeit("func_1()", setup="from __main__ import func_1", number=1000), "millisecond")
print("func_2", timeit.timeit("func_2()", setup="from __main__ import func_2", number=1000), "millisecond")
print("func_3", timeit.timeit("func_3()", setup="from __main__ import func_3", number=1000), "millisecond")

"""
Результат:
func_1 0.008251770999999998 millisecond
func_2 0.012748807000000001 millisecond
func_3 0.004376456000000001 millisecond

Третий вариант поиска часто встречающегося элемента в массиве самый быстрый по времени, 
т.к. в нем сразу ищется максимальное значение из кол-в вхождений элементов в исходном списке.
"""