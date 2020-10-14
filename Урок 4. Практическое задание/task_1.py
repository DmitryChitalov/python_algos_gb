"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from random import randint
from timeit import timeit

# Сначала сгенерируем исходный список
nums = [randint(0, 100) for i in range(10)]
print(f'Исходный список: {nums}')


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Попробуем извлечь индексы четных элементов nums с помощью генератор списка
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


# Попробуем применить рекурсию. Но здесь все попытки вывести именно индексы успехом не увенчались, вывел сами элементы,
# думаю, что на замеры это никак не повлияет, но в будущем буду очень благодарен за разбор.

def func_3(nums, new_arr):
    if len(nums) == 0:
        return new_arr
    if nums[0] % 2 == 0:
        new_arr.append(nums[0])
    return func_3(nums[1:], new_arr)


print()
print(f'Вывод через цикл: {func_1(nums)}')
print(f"number = 1: {timeit('func_1(nums)', setup='from __main__ import func_1, nums', number=1)}")
print(f"number = 1000: {timeit('func_1(nums)', setup='from __main__ import func_1, nums', number=1000)}")
print(f"number = 1000000: {timeit('func_1(nums)', setup='from __main__ import func_1, nums', number=1000000)}")
print()
print(f'Вывод через генератор списка: {func_2(nums)}')
print(f"number = 1: {timeit('func_2(nums)', setup='from __main__ import func_2, nums', number=1)}")
print(f"number = 1000: {timeit('func_2(nums)', setup='from __main__ import func_2, nums', number=1000)}")
print(f"number = 1000000: {timeit('func_2(nums)', setup='from __main__ import func_2, nums', number=1000000)}")
print()
# Проведя замеры с разным количеством вызовов, мы видим,
# что генератор списка при любых обстоятельствах работает быстрее обычного цикла.
# На мой взгляд генераторы более удобны в использовании и как бы намекают на стиль=)


# Рекурсивный метод, как и ожидалось, оказался самым медленным.
# С другой стороны, если бы я смог оформить корректный вывод, то возможно, получилось бы вас удивить=)
new_arr = []
func_3(nums, new_arr)
print(f'Вывод через рекурсию: {new_arr}')
print(f"number = 1: "
      f"{timeit('func_3(nums, new_arr)', setup='from __main__ import func_3, nums, new_arr', number=1)}")
print(f"number = 1000: "
      f"{timeit('func_3(nums, new_arr)', setup='from __main__ import func_3, nums, new_arr', number=1000)}")
print(f"number = 1000000: "
      f"{timeit('func_3(nums, new_arr)', setup='from __main__ import func_3, nums, new_arr', number=1000000)}")

# Вывод: генераторы списков - удобство и стиль вашего кода!=).