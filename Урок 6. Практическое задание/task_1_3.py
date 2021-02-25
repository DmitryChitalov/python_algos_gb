"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
@profile
def function_1(max_value):
    """Функция возвращает сумму квадатов четных чисел от 0 до max_value"""
    gen = [x ** 2 for x in range(1, max_value) if x % 2 == 0]
    value = reduce(lambda x, y: x + y, gen)
    return value


print(function_1(9999999))

"""
Результаты:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     17.8 MiB     17.8 MiB           1   @profile
     6                                         def function_1(max_value):
     7                                             """Функция возвращает сумму квадатов четных чисел от 0 до max_value"""
     8    212.1 MiB -15021.7 MiB    10000001       gen = [x ** 2 for x in range(1, max_value) if x % 2 == 0]
     9    212.1 MiB -282884.9 MiB     9999997       value = reduce(lambda x, y: x + y, gen)
    10    212.1 MiB     -0.0 MiB           1       return value

    
Результаты рыботы профилировщика выглядят странно. 
На маленьких значениях работа с памятью в статистике не видна. На любых скриптах объем памяти примерно одинаковый.
Похоже, что это память под работу собственно профилировщика.

По крайней мере, в выводе заметно, что было увеличение используемой памяти в нужном месте.
По другим вариантам вызова результаты аналогичные - видно, что количество памяти изменялось, 
но выводимые значения некорректны
"""

@profile
def function_2(max_value):
    """Функция возвращает сумму квадатов четных чисел от 1 до max_value"""
    gen = (x**2 for x in range(1, max_value) if x % 2 == 0)
    print(type(gen))
    value = reduce(lambda x, y: x + y, gen)
    return value


print(function_2(9999999))

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     6     17.6 MiB     17.6 MiB           1   @profile
     7                                         def function_2(max_value):
     8                                             """Функция возвращает сумму квадатов четных чисел от 1 до max_value"""
     9     17.7 MiB -346580.6 MiB    15000000       gen = (x**2 for x in range(1, max_value) if x % 2 == 0)
    10     17.6 MiB      0.0 MiB           1       print(type(gen))
    11     17.7 MiB -231053.7 MiB     9999997       value = reduce(lambda x, y: x + y, gen)
    12     17.7 MiB     -0.0 MiB           1       return value

"""

@profile
def function_3(max_value):
    """Функция возвращает сумму квадатов четных чисел от 0 до max_value"""
    gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    value = reduce(lambda x, y: x + y, gen)
    del gen
    return value


print(function_3(9999999))

"""
Сделано принудительное удаление пременной. Память освобождается.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     6     17.6 MiB     17.6 MiB           1   @profile
     7                                         def function_3(max_value):
     8                                             """Функция возвращает сумму квадатов четных чисел от 0 до max_value"""
     9    212.0 MiB -28951.5 MiB    10000001       gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    10    212.1 MiB -7228413.7 MiB     9999997       value = reduce(lambda x, y: x + y, gen)
    11     17.9 MiB   -194.2 MiB           1       del gen
    12     17.9 MiB      0.0 MiB           1       return value
"""
