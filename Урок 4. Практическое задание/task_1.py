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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


our_nums_1 = [el for el in range(1000)]

res_1_1 = timeit(
            stmt="func_1(our_nums_1)",
            setup="from __main__ import func_1, our_nums_1",
            number=1000)  # запуск 1000 раз

res_1_2 = timeit(
        stmt="func_2(our_nums_1)",
        setup="from __main__ import func_2, our_nums_1",
        number=1000)

print(f'Результат 1 (на 1000 элементов): \n'
      f'func_1 отрабатывает за {res_1_1} \n'
      f'func_2 отрабатывает за {res_1_2} \n'
      f'~ быстрее в {res_1_1/res_1_2:.10f} раз \n')

our_nums_2 = [el for el in range(10000)]

res_2_1 = timeit(
            stmt="func_1(our_nums_2)",
            setup="from __main__ import func_1, our_nums_2",
            number=1000)  # запуск 1000 раз

res_2_2 = timeit(
        stmt="func_2(our_nums_2)",
        setup="from __main__ import func_2, our_nums_2",
        number=1000)

print(f'Результат 2 (на 10000 элементов): \n'
      f'func_1 отрабатывает за {res_2_1} \n'
      f'func_2 отрабатывает за {res_2_2} \n'
      f'~ быстрее в {res_2_1/res_2_2:.10f} раз \n')

our_nums_3 = [el for el in range(1000000)]

res_3_1 = timeit(
            stmt="func_1(our_nums_3)",
            setup="from __main__ import func_1, our_nums_3",
            number=1000)  # запуск 1000 раз

res_3_2 = timeit(
        stmt="func_2(our_nums_3)",
        setup="from __main__ import func_2, our_nums_3",
        number=1000)

print(f'Результат 3 (на 1000000 элементов): \n'
      f'func_1 отрабатывает за {res_3_1} \n'
      f'func_2 отрабатывает за {res_3_2} \n'
      f'func_2 ~ быстрее в {res_3_1/res_3_2:.10f} раз')


"""
Аналитика

Результат 1 (на 1000 элементов): 
func_1 отрабатывает за 0.135286435 
func_2 отрабатывает за 0.09559910400000002 
~ быстрее в 1.4151433365 раз 

Результат 2 (на 10000 элементов): 
func_1 отрабатывает за 1.277174821 
func_2 отрабатывает за 0.9555555569999998 
~ быстрее в 1.3365782990 раз 

Результат 3 (на 1000000 элементов): 
func_1 отрабатывает за 151.71376642299998 
func_2 отрабатывает за 118.41819964499999 
func_2 ~ быстрее в 1.2811693378 раз

Выполнение функций решающих поставленную задачу
с использование генераторного выражения - быстрее, 
чем с использование циклов for

С ростом объема передаваемых в функции данных разница становится менее заметной в общем итоговом замере
"""