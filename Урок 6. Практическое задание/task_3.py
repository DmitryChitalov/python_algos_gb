"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile

@profile
def recursion(number):
    def numbers(num):
        if len(str(num)) == 1:
            return str(num)
        return str(num % 10) + numbers(num // 10)
    print(f'Перевернутое число {number}, равно - {numbers(number)}')


@profile
def cycle(number):
    copy_num = number
    reverse_num = ''
    while len(str(number)) != 1:
        reverse_num += str(number % 10)
        number //= 10
    print(f'Перевернутое число {copy_num}, равно - {reverse_num}')



recursion(123456789**110)
cycle(123456789**110)

"""
Подводные камни в профилировании рекурсии есть, и это кол-во таблиц будет столько, сколько
и вызовов функции
Это решается помещением рекурсии во внутрь другой функции

1. Рекурсия
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    10     16.0 MiB     16.0 MiB           1   @profile
    11                                         def recursion(number):
    12     17.0 MiB      0.7 MiB         892       def numbers(num):
    13     17.0 MiB      0.4 MiB         891           if len(str(num)) == 1:
    14     17.0 MiB      0.0 MiB           1               return str(num)
    15     17.0 MiB      0.0 MiB         890           return str(num % 10) + numbers(num // 10)
    16     17.0 MiB      0.0 MiB           1       print(f'Перевернутое число {number}, равно - {numbers(number)}')
    
2. Цикл
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    19     17.0 MiB     17.0 MiB           1   @profile
    20                                         def cycle(number):
    21     17.0 MiB      0.0 MiB           1       copy_num = number
    22     17.0 MiB      0.0 MiB           1       reverse_num = ''
    23     17.0 MiB      0.0 MiB         891       while len(str(number)) != 1:
    24     17.0 MiB      0.0 MiB         890           reverse_num += str(number % 10)
    25     17.0 MiB      0.0 MiB         890           number //= 10
    26     17.0 MiB      0.0 MiB           1       print(f'Перевернутое число {copy_num}, равно - {reverse_num}')
    
Как мы видим в цикле память не выделяется, что нельзя сказать о рекурсии,
При работе рекурсии заполняется стек вызываемых функций.
Windows 10/x64 
Python 3.8.3

"""





