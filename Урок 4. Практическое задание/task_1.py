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

nums = [1,2,3,4,5,6,7,8,9]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = [i for i in nums[:-1] if i % 2 != 0]
    return new_arr



# one begin
print(f'#1 -- {func_1(nums)}')
time_one = timeit("func_1(nums)", setup = "from __main__ import func_1, nums", number=1)
print(f'#1 -- {time_one * 1000}')
# one end

#two begin
print(f'#2 -- {func_2(nums)}')
time_two = timeit("func_2(nums)",setup = "from __main__ import func_2, nums", number=1)
print(f'#2 -- {time_two * 1000}')
#two end

# генераторное выражение явно лучше.
# думаю, что первом случае больше действий:
    # 1. создаём список
    # 2. считаем кол-во элементов
    # 3. идём в цикл
    # 4. поиск и-того эл-та
    # 5. проверка
    # 6. добавление
    # 7. возврат

# во втором варианте не считается кол-во элементов и нет поиска элемента в списке.
# + каждое новое знаечение присваивается сразу, без append()



