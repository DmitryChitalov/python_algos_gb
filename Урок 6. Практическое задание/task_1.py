"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import memory_usage, profile
from timeit import default_timer
from random import randint
from sys import version


def my_profile(func):
    def wrapper(*args, **kwargs):
        t = default_timer()
        res = func(*args, **kwargs)
        print(f'время выполнения: {default_timer() - t}сек, использованная память {memory_usage()}')
        return res
    return wrapper


@my_profile
@profile
def t1():
    my_list = [randint(0, 1000) for i in range(randint(30, 100))]
    print(len(my_list), my_list)
    r_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
    print(len(r_list), r_list)


@my_profile
@profile
def t2(n):
    i = 0
    j = 0
    for el in str(n):
        if int(el) % 2 == 0:
            i += 1
        else:
            j += 1
    print(f'Количество четных и нечетных цифр в числе равно: {i} и {j}.')


"""
3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)]
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     18.4 MiB     18.4 MiB           1   @my_profile
    39                                         @profile
    40                                         def t1():
    41     18.4 MiB      0.0 MiB          68       my_list = [randint(0, 1000) for i in range(randint(30, 100))]
    42     18.4 MiB      0.0 MiB           1       print(len(my_list), my_list)
    43     18.4 MiB      0.0 MiB          67       r_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
    44     18.4 MiB      0.0 MiB           1       print(len(r_list), r_list)
строка 41 - создание списка из чисел. нет увеличения памяти, поскольку ссылки на числа уже имеются.
строка 43 - аналогично


время выполнения: 0.03713069999999999сек, использованная память [18.43359375]

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    47     18.4 MiB     18.4 MiB           1   @my_profile
    48                                         @profile
    49                                         def t2(n):
    50     18.4 MiB      0.0 MiB           1       i = 0
    51     18.4 MiB      0.0 MiB           1       j = 0
    52     18.4 MiB      0.0 MiB           9       for el in str(n):
    53     18.4 MiB      0.0 MiB           8           if int(el) % 2 == 0:
    54     18.4 MiB      0.0 MiB           4               i += 1
    55                                                 else:
    56     18.4 MiB      0.0 MiB           4               j += 1
    57     18.4 MiB      0.0 MiB           1       print(f'Количество четных и нечетных цифр в числе равно: {i} и {j}.')
Алгоритм работает с числами, поскольку они уже имеются в памяти, 
увеличения использования памяти внутри алгоритма не происходит. 

время выполнения: 0.002033900000000033сек, использованная память [18.4375]
"""
if __name__ == '__main__':
    print(version)
    t1()
    t2(49329212)
