"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

'''
3-е задание 
Замеры рекурсии
Создадим рекурсивную функцию 
Обернем ее в другую функцию
Таким образом мы избежим множественного вызова профилировщика
'''


from memory_profiler import profile


@profile
def func2(n):
    res = sum_rec(n)
    return res


def sum_rec(n):
    if n == 1:
        return 1
    return n + sum_rec(n-1)


print(func2(100))

"""
Результат:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     13.9 MiB     13.9 MiB           1   @profile
    19                                         def func2(n):
    20     13.9 MiB      0.0 MiB           1       res = sum_rec(n)
    21     13.9 MiB      0.0 MiB           1       return res


5050
"""
