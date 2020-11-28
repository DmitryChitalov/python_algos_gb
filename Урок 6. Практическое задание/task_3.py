"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from mymodules import measurer
from memory_profiler import profile


@measurer
@profile
def wrapped(n):
    def sum_numb(start, stop):
        """
        Функция возвращает сумму от 1+2+...+n

        start: Начало отчета == 1
        stop: Конец ряда чисел == n
        """
        if start == stop:
            return start
        else:
            return start + sum_numb(start + 1, stop)

    if sum_numb(1, n) == n * (n + 1) / 2:
        print(f'1+2+...+n = n(n+1)/2 - равенство выполняется!')
    else:
        print(f'1+2+...+n = n(n+1)/2 - равенство НЕ выполняется!')
    return sum_numb


n = int(input('Введите n: '))
wrapped(n)

"""
-- PROFILER --

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    13     13.6 MiB     13.6 MiB           1   @measurer
    14                                         @profile
    15                                         def wrapped(n):
    16     15.0 MiB      1.2 MiB         901       def sum_numb(start, stop):
    17                                                 
    23     15.0 MiB      0.1 MiB         900           if start == stop:
    24     15.0 MiB      0.0 MiB           1               return start
    25                                                 else:
    26     15.0 MiB      0.0 MiB         899               return start + sum_numb(start + 1, stop)
    27                                         
    28     15.0 MiB      0.0 MiB           1       if sum_numb(1, n) == n * (n + 1) / 2:
    29     15.0 MiB      0.0 MiB           1           print(f'1+2+...+n = n(n+1)/2 - равенство выполняется!')
    30                                             else:
    31                                                 print(f'1+2+...+n = n(n+1)/2 - равенство НЕ выполняется!')
    32     15.0 MiB      0.0 MiB           1       return sum_numb

-- ДЕКОРАТОР --
Выполнение заняло 0.29432 сек и 1.531 Miб


Произвел замеры своим декоратором и memory_profiler, предварительно сделал обертку, не увидел проблем 
в замерах. Через обертку вобщем-то рекурсия тоже замеряется не плохо.
"""