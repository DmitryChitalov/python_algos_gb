"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
        return revers_num


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


cProfile.run('revers(123456789)')
cProfile.run('revers_2(123456789)')
cProfile.run('revers_3(123456789)')
print(timeit('revers(123456789)', 'from __main__ import revers'))
print(timeit('revers_2(123456789)', 'from __main__ import revers_2'))
print(timeit('revers_3(123456789)', 'from __main__ import revers_3'))
print(revers(123456789))
print(revers_2(123456789))
print(revers_3(123456789))
'''
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     10/1    0.000    0.000    0.000    0.000 task_3.py:16(revers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:26(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:34(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


2.6212611
1.7330287000000002
0.38962450000000004

9.0
987654321.0
987654321

'''
'''
По времени очевидно, что reverse_3 эффективнее по скорости выполнения.
Замечу, что функции возвращают различный результат, где входное число: 123456789, а на выходе:
9.0 - при условии, что добавлен return, без него вообще None.
987654321.0
987654321

Из таблицы вывода сProfile я ничего не смог определить, везде 0.000, единственное различие это показ
рекурсии 10 раз в столбце ncalls первой функции.
Рекурсия не самый удачный вариант для решения данного примера.
'''