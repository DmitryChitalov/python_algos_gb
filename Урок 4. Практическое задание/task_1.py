"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

1 Сделайте замеры времени выполнения кода с помощью модуля timeit

2 Попробуйте оптимизировать код, чтобы снизить время выполнения
  Проведите повторные замеры

3 Добавьте аналитику: что вы сделали и почему
"""
import timeit


def func_1(nums):  # O(n)
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


"""
1 делаем замеры. Два варианта первый через timeit.Timer, второй через timeit.timeit
"""
my_list = [i for i in range(10)]
t1 = timeit.Timer("func_1(my_list)", "from __main__ import func_1, my_list")
print("func_1 v_1", t1.timeit(number=100000), "seconds")

"""
100 тыс запусков:
        для 10 элементов - 0.10232450000000001 seconds
        для 100 - 0.6512728 seconds
        для 1000 - 7.161947199999999 seconds
        для 10000 - 74.73720349999999 seconds    
"""
print('-' * 79)
print('func_1 v_2', timeit.timeit('func_1(my_list)', setup='from __main__ import func_1, my_list', number=100000),
      'seconds')

"""
Второй вариант дает примероно такойже результат, но код короче.
"""

"""
2 Оптимизируем код. Сделаем формирование массива через генераторное выражение.
"""

print('--*--' * 16)
def func_2(nums):
    new_arr = [i for i, j in enumerate(nums) if i % 2 == 0]
    return new_arr


t1 = timeit.Timer("func_2(my_list)", "from __main__ import func_2, my_list")
print("func_2 v_1", t1.timeit(number=100000), "seconds")
print('-' * 79)
print('func_1 v_2', timeit.timeit('func_2(my_list)', setup='from __main__ import func_2, my_list', number=100000),
      'seconds')
"""
100 тыс запусков:
        для 10 элементов - 0.10029249999999999 seconds
        для 100 - 0.5681884 seconds
        для 1000 - 6.9027997 seconds
        для 10000 - 71.295923 seconds    
"""

"""
3 Аналитика. func_1 также как и func_2 имеет линейную сложность O(n). При этом func_2 имеет более короткую 
запись, легче читается и работает немного быстрее, при большом количестве элементов массива разница может стать
ощутимой, поэтом отдаем приемущество генераторному выражению.
"""