"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
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


def func_3(arr, count=0, count_i=0, m=0, num=0):
    if len(arr) == count_i:
        # print(f'Чаще всего встречается число {num}, ' \
        #    f'оно появилось в массиве {m} раз(а)')
        return
    count = array.count(arr[count_i])
    if count > m:
        m = count
        num = arr[count_i]
    func_3(arr, count, count_i + 1, m, num)


print(func_1())
print(func_2())
func_3(array)
print(timeit.timeit("func_1()", setup="from __main__ import func_1", number=1000))
print(timeit.timeit("func_2()", setup="from __main__ import func_2", number=1000))
print(timeit.timeit("func_3(array)", setup="from __main__ import func_3, array", number=1000))

"""
в первом и втором случае применен цикл for, в первом случае взятие элемента по индексу дает больше скорость, чем
дополнительно создание нового списка во втором случае методом append. В третьем случае попытка заменить цикл for на 
рекурсию, модифицировав первый вариант. в итоге вариант с рекурсией самый медленный
"""