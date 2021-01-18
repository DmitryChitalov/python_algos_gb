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
    number = max(array, key=array.count)
    return number


print(timeit("func_1()", "from __main__ import func_1"))
print(timeit("func_2()", "from __main__ import func_2"))
print(timeit("func_3()", "from __main__ import func_3"))

"""
Результаты:

1.3176097
1.6486165999999998
0.8826595999999998

Вариант 2 самый долгий, так как помимо цикла for (операции перебора), в нем мы еще и создаем новый список
В Варианте 1 мы используем "счетсчик", но также перебираем элементы списка
В предложенном варианте 3 мы сразу что ищем, используя метод простой сортировки по ключу.
"""

