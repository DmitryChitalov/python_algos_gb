"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
"""
Профилировать саму рекурсивную функцию можно при помощи cProfile, который умеет
работать с рекурсивными вызовами, либо обернув ее в функцию-"обертку", насколько я понял.
Хотя, в случае Python, использование рекурсии достаточно ограничено из-за ограничений
по вложенности. 

Input index:
15
Before func: [19.08203125]
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     19.3 MiB     19.3 MiB           1   @profile
    39                                         def main_fib(in_num):
    40     19.3 MiB      0.0 MiB           1       return fib(in_num)


After func: [19.33203125]
377
Before func: [19.33203125]
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     19.3 MiB     19.3 MiB           1   @profile
    43                                         def main_fac(in_num):
    44     19.3 MiB      0.0 MiB           1       return fac(in_num)


After func: [19.33203125]
1307674368000
Before func: [19.33203125]
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     19.3 MiB     19.3 MiB           1   @profile
    30                                         def fac_iter(in_num):
    31     19.3 MiB      0.0 MiB           1       res = 1
    32     19.3 MiB      0.0 MiB           1       counter = in_num
    33     19.3 MiB      0.0 MiB          15       while counter > 1:
    34     19.3 MiB      0.0 MiB          14           res = res * counter
    35     19.3 MiB      0.0 MiB          14           counter = counter - 1
    36     19.3 MiB      0.0 MiB           1       return res


After func: [19.33203125]
1307674368000
         263 function calls (256 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 enum.py:289(__call__)
        2    0.000    0.000    0.000    0.000 enum.py:580(__new__)
        1    0.000    0.000    0.000    0.000 enum.py:852(__and__)
        1    0.000    0.000    0.000    0.000 re.py:250(compile)
        1    0.000    0.000    0.000    0.000 re.py:289(_compile)
        1    0.000    0.000    0.000    0.000 sre_compile.py:249(_compile_charset)
        1    0.000    0.000    0.000    0.000 sre_compile.py:276(_optimize_charset)
        2    0.000    0.000    0.000    0.000 sre_compile.py:453(_get_iscased)
        1    0.000    0.000    0.000    0.000 sre_compile.py:461(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:492(_get_charset_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:536(_compile_info)
        2    0.000    0.000    0.000    0.000 sre_compile.py:595(isstring)
        1    0.000    0.000    0.000    0.000 sre_compile.py:598(_code)
      3/1    0.000    0.000    0.000    0.000 sre_compile.py:71(_compile)
        1    0.000    0.000    0.000    0.000 sre_compile.py:759(compile)
        3    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
        7    0.000    0.000    0.000    0.000 sre_parse.py:160(__len__)
       28    0.000    0.000    0.000    0.000 sre_parse.py:164(__getitem__)
       12    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
      3/1    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
        1    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
       13    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
        2    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
       11    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
        1    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
        1    0.000    0.000    0.000    0.000 sre_parse.py:435(_parse_sub)
        2    0.000    0.000    0.000    0.000 sre_parse.py:493(_parse)
        1    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:81(groups)
        1    0.000    0.000    0.000    0.000 sre_parse.py:921(fix_flags)
        1    0.000    0.000    0.000    0.000 sre_parse.py:937(parse)
        1    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       35    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    28/25    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        9    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
       60    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}


         263 function calls (256 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 enum.py:289(__call__)
        2    0.000    0.000    0.000    0.000 enum.py:580(__new__)
        1    0.000    0.000    0.000    0.000 enum.py:852(__and__)
        1    0.000    0.000    0.000    0.000 re.py:250(compile)
        1    0.000    0.000    0.000    0.000 re.py:289(_compile)
        1    0.000    0.000    0.000    0.000 sre_compile.py:249(_compile_charset)
        1    0.000    0.000    0.000    0.000 sre_compile.py:276(_optimize_charset)
        2    0.000    0.000    0.000    0.000 sre_compile.py:453(_get_iscased)
        1    0.000    0.000    0.000    0.000 sre_compile.py:461(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:492(_get_charset_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:536(_compile_info)
        2    0.000    0.000    0.000    0.000 sre_compile.py:595(isstring)
        1    0.000    0.000    0.000    0.000 sre_compile.py:598(_code)
      3/1    0.000    0.000    0.000    0.000 sre_compile.py:71(_compile)
        1    0.000    0.000    0.000    0.000 sre_compile.py:759(compile)
        3    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
        7    0.000    0.000    0.000    0.000 sre_parse.py:160(__len__)
       28    0.000    0.000    0.000    0.000 sre_parse.py:164(__getitem__)
       12    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
      3/1    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
        1    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
       13    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
        2    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
       11    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
        1    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
        1    0.000    0.000    0.000    0.000 sre_parse.py:435(_parse_sub)
        2    0.000    0.000    0.000    0.000 sre_parse.py:493(_parse)
        1    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:81(groups)
        1    0.000    0.000    0.000    0.000 sre_parse.py:921(fix_flags)
        1    0.000    0.000    0.000    0.000 sre_parse.py:937(parse)
        1    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       35    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    28/25    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        9    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
       60    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}


         269 function calls (262 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 enum.py:289(__call__)
        2    0.000    0.000    0.000    0.000 enum.py:580(__new__)
        1    0.000    0.000    0.000    0.000 enum.py:852(__and__)
        1    0.000    0.000    0.000    0.000 re.py:250(compile)
        1    0.000    0.000    0.000    0.000 re.py:289(_compile)
        1    0.000    0.000    0.000    0.000 sre_compile.py:249(_compile_charset)
        1    0.000    0.000    0.000    0.000 sre_compile.py:276(_optimize_charset)
        2    0.000    0.000    0.000    0.000 sre_compile.py:453(_get_iscased)
        1    0.000    0.000    0.000    0.000 sre_compile.py:461(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:492(_get_charset_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:536(_compile_info)
        2    0.000    0.000    0.000    0.000 sre_compile.py:595(isstring)
        1    0.000    0.000    0.000    0.000 sre_compile.py:598(_code)
      3/1    0.000    0.000    0.000    0.000 sre_compile.py:71(_compile)
        1    0.000    0.000    0.000    0.000 sre_compile.py:759(compile)
        3    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
        7    0.000    0.000    0.000    0.000 sre_parse.py:160(__len__)
       28    0.000    0.000    0.000    0.000 sre_parse.py:164(__getitem__)
       12    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
      3/1    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
        1    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
       13    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
        2    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
       11    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
        1    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
        1    0.000    0.000    0.000    0.000 sre_parse.py:435(_parse_sub)
        2    0.000    0.000    0.000    0.000 sre_parse.py:493(_parse)
        1    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:81(groups)
        1    0.000    0.000    0.000    0.000 sre_parse.py:921(fix_flags)
        1    0.000    0.000    0.000    0.000 sre_parse.py:937(parse)
        1    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       35    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    29/26    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        9    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
       63    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        5    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}


Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     19.6 MiB     19.6 MiB           1   @profile
    39                                         def main_fib(in_num):
    40     19.6 MiB      0.0 MiB           1       return fib(in_num)


0.0036981000000002595
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     19.6 MiB     19.6 MiB           1   @profile
    43                                         def main_fac(in_num):
    44     19.6 MiB      0.0 MiB           1       return fac(in_num)


0.000615200000000371
Filename: C:\Users\hukut\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     19.6 MiB     19.6 MiB           1   @profile
    30                                         def fac_iter(in_num):
    31     19.6 MiB      0.0 MiB           1       res = 1
    32     19.6 MiB      0.0 MiB           1       counter = in_num
    33     19.6 MiB      0.0 MiB          15       while counter > 1:
    34     19.6 MiB      0.0 MiB          14           res = res * counter
    35     19.6 MiB      0.0 MiB          14           counter = counter - 1
    36     19.6 MiB      0.0 MiB           1       return res


0.0021687000000003565

"""
from timeit import timeit
from memory_profiler import profile
from memory_profiler import memory_usage
import cProfile
import re


def fac(in_num):
    if in_num == 1: return 1
    return in_num * fac(in_num - 1)


def fib(in_num):
    if in_num == 1: return 0
    if in_num == 2: return 1
    return fib(in_num - 1) + fib(in_num - 2)


@profile
def fac_iter(in_num):
    res = 1
    counter = in_num
    while counter > 1:
        res = res * counter
        counter = counter - 1
    return res


@profile
def main_fib(in_num):
    return fib(in_num)


@profile
def main_fac(in_num):
    return fac(in_num)


print("Input index:")
num = int(input())
mem_before = memory_usage()
print(f'Before func: {mem_before}')
res = main_fib(num)
mem_after = memory_usage()
print(f'After func: {mem_after}')
print(str(res))
mem_before = memory_usage()
print(f'Before func: {mem_before}')
res = main_fac(num)
mem_after = memory_usage()
print(f'After func: {mem_after}')
print(str(res))
mem_before = memory_usage()
print(f'Before func: {mem_before}')
res = fac_iter(num)
mem_after = memory_usage()
print(f'After func: {mem_after}')
print(str(res))

cProfile.run('re.compile("main_fib|num")')
cProfile.run('re.compile("main_fac|num")')
cProfile.run('re.compile("fac_iter|num")')

print(
    timeit(
        "main_fib(num)",
        setup='from __main__ import main_fib, num',
        number=1))
print(
    timeit(
        "main_fac(num)",
        setup='from __main__ import main_fac, num',
        number=1))
print(
    timeit(
        "fac_iter(num)",
        setup='from __main__ import fac_iter, num',
        number=1))
