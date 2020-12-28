"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


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


print(timeit('revers(10000)', setup='from __main__ import revers', number=10000))
print(timeit('revers_2(10000)', setup='from __main__ import revers_2', number=10000))
print(timeit('revers_3(10000)', setup='from __main__ import revers_3', number=10000))

cProfile.run('revers(10000)')
cProfile.run('revers_2(10000)')
cProfile.run('revers_3(10000)')


"""
Время revers 0.0132986
Время revers_2 0.008235300000000001
Время revers_3 0.0032940999999999943

Для revers:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      6/1    0.000    0.000    0.000    0.000 task_3.py:16(revers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Для revers_2:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:26(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Для revers_3
  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:34(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
        По результатам замеров timeit можно сделать вывод, что самым быстрым решением является
        revers_3(Решение через срез), а самыс долгим revers(Решение через рекурсию)
        Модуль cProfile показывает, что все функции работают быстро. Но количество вызовов функции при
        решении через рекурсию наибольшее, что в совокупности с замерами через timeit говорит, что самое опти-
        мальное решение через срез, самое неоптимальное - через рекурсию.
"""