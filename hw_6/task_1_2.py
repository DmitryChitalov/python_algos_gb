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
import memory_profiler
from timeit import default_timer


def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        res_time = default_timer() - start_time
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff, res_time
    return wrapper


@decor
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        str_num = str(i)
        new_arr.append(str_num)
    return new_arr


@decor
def func_2(nums):
    new_arr2 = [str(el) for el in nums]
    return new_arr2


@decor
def func_3(nums):
    return map(str, nums)


if __name__ == '__main__':
    res, mem_diff, res_time = func_1(list(range(30000)))
    print(f"Выполнение заняло {mem_diff} Mib")
    print(f"Выполнение заняло {res_time} sec")
    res1, mem_diff1, res_time1 = func_2(list(range(30000)))
    print(f"Выполнение заняло {mem_diff1} Mib")
    print(f"Выполнение заняло {res_time1} sec")
    res2, mem_diff2, res_time2 = func_3(list(range(30000)))
    print(f"Выполнение заняло {mem_diff2} Mib")
    print(f"Выполнение заняло {res_time2} sec")

'''
Перевод в строковое представление переданной числовой последовательности
Для списка при использовании append:
Выполнение заняло 1.12109375 Mib
Выполнение заняло 0.10745679999999999 sec
Для списка при списковом включении:
Выполнение заняло 1.03125 Mib
Выполнение заняло 0.1055681 sec
При использовании функции map:
Выполнение заняло 0.0 Mib
Выполнение заняло 0.0995566 sec
Как здесь видно, использование функции map сократило использование памяти почти до 0, потому что идет применение 
функции к одному элементу последовательности за раз, далее идет списковое включение,
 которое потребляет тоже достаточно мало памяти. 
'''
