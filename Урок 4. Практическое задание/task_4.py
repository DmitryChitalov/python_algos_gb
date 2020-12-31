"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import cProfile
from collections import Counter
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
    result = max(set(array), key=array.count)
    count = array.count(result)
    return f'Чаще всего встречается число {result}, ' \
           f'оно появилось в массиве {count} раз(а)'


def func_4():
    data = Counter(array)
    result = data.most_common(1)
    return f'Чаще всего встречается число {result[0][0]}, ' \
           f'оно появилось в массиве {result[0][1]} раз(а)'


def main():
    func_1()
    func_2()
    func_3()
    func_4()


cProfile.run('main()')

print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(
    timeit(
        "func_1()",
        setup='from __main__ import func_1',
        number=10000))

print(
    timeit(
        "func_2()",
        setup='from __main__ import func_2',
        number=10000))

print(
    timeit(
        "func_3()",
        setup='from __main__ import func_3',
        number=10000))

print(
    timeit(
        "func_4()",
        setup='from __main__ import func_4',
        number=10000))

"""
Результаты:
func_1 = 0.01807752800000001
func_2 = 0.024876923999999967
func_3 = 0.017178291000000012
func_4 = 0.04351234599999998

func_3 получилась чуть быстрее func_1 за счет:
- использования set для уникализации массива
- использования функции max с передаваемой внутрь функцией array.count(), по которой будет отбираться максимальное значение
- метод можно сделать быстрее, если не считать второй аргумент - кол-во повторений
"""
