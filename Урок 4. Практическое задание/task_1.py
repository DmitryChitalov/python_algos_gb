"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return [index for index, i in enumerate(nums) if i % 2 == 0]

# Самый тормозной вариант - почти на порядок медленее остального
#def func_4(nums):
#    return list(nums.index(i) for i in nums if i % 2 == 0)


test_arr = [randint(0, 100) for i in range(100000)]
print(test_arr)
print(func_1(test_arr))
print(func_2(test_arr))
print(func_3(test_arr))
#print(func_4(test_arr))

print(timeit('func_1(test_arr)', setup='from __main__ import func_1, test_arr', number=10000))
print(timeit('func_2(test_arr)', setup='from __main__ import func_2, test_arr', number=10000))
print(timeit('func_3(test_arr)', setup='from __main__ import func_3, test_arr', number=10000))
#print(timeit('func_4(test_arr)', setup='from __main__ import func_4, test_arr'))

"""
100 элементов:
0.1671983359992737
0.10287084899937327
0.09326979799880064

1000 элементов:
1.2272903170014615
1.0594693109997024
0.9901098260015715

10000 элементов:
11.831746955998824
10.248948598000425
10.083051663001243

100000 элементов:
133.86116691799907
117.64352869100185
111.75325181200242

Замена цикла for на генераторное выражение дает небольшой выигрыш в скорости, т.е. преимущество встроенных 
инструментов заметно.
Причем, через функцию enumerate результат лучше, чем при проверке элементов по индексу.
Но всё равно выигрыш скорости довольно мал.
"""