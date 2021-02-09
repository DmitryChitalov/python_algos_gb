"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
import random
from timeit import timeit

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

num_100 = random.randint(10,100)
num_1000 = random.randint(100,1000)
num_10000 = random.randint(1000,10000)


def call_func():
    """ 
    Вызывает по порядку каждую функцию с заданным аргументом
    """
    print(
    timeit(
        'revers(num_1000)',
        setup='from __main__ import revers, num_1000',
        number=1000))

    print(
    timeit(
        'revers_2(num_1000)',
        setup='from __main__ import revers_2, num_1000',
        number=1000))

    print(
    timeit(
        'revers_3(num_1000)',
        setup='from __main__ import revers_3, num_1000',
        number=1000))
    return


# замеряем через сProfile


if __name__ == '__main__':
    cProfile.run('call_func()')

"""
cProfile также замеряет вызовы библиотечных функций внутри тестируемых. Очевидно третья релазация оказалась наиболее быстродействующей.

 python3 'Урок 4. Практическое задание/task_3.py'
0.002843235997715965
0.0013991379964863881
0.0009559980026097037
         6069 function calls (3066 primitive calls) in 0.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 <timeit-src>:2(<module>)
        1    0.000    0.000    0.001    0.001 <timeit-src>:2(inner)
4000/1000    0.002    0.000    0.002    0.000 task_3.py:16(revers)
     1000    0.001    0.000    0.001    0.000 task_3.py:26(revers_2)
     1000    0.001    0.000    0.001    0.000 task_3.py:34(revers_3)
        1    0.000    0.000    0.008    0.008 task_3.py:44(call_func)
        3    0.000    0.000    0.002    0.001 timeit.py:101(__init__)
        3    0.000    0.000    0.005    0.002 timeit.py:163(timeit)
        3    0.000    0.000    0.008    0.003 timeit.py:230(timeit)
        6    0.000    0.000    0.000    0.000 timeit.py:79(reindent)
        9    0.002    0.000    0.002    0.000 {built-in method builtins.compile}
      4/1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.globals}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        3    0.000    0.000    0.000    0.000 {built-in method gc.disable}
        3    0.000    0.000    0.000    0.000 {built-in method gc.enable}
        3    0.000    0.000    0.000    0.000 {built-in method gc.isenabled}
        6    0.000    0.000    0.000    0.000 {built-in method time.perf_counter}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        6    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
"""     



