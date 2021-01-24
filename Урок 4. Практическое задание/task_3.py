"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
from cProfile import run
from time import sleep


nm = 1234567


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


print('reverse: ', timeit(stmt='revers(nm)', globals=globals()))
print('reverse_2: ', timeit(stmt='revers_2(nm)', globals=globals()))
print('reverse_3: ', timeit(stmt='revers_3(nm)', globals=globals()))


def main():
    nm = 1234567
    revers(nm)
    sleep(1)
    revers_2(nm)
    sleep(1)
    revers_3(nm)
    sleep(1)


run('main()')


"""
Самая тяжелая функция - reverse, так как она использует механизм рекурсии, а он очень тяжелый.
Вторая по оптимальности функция - reverse_2, так как она использует механизм цикла, но при этом является рукописной,
практически не используются встроенные механизмы языка python.
Самая оптимальная функция - reverse_3, так как она использует только встроенную возможность среза строки языка python.
При этом каких-то других более сложных действий, типа самописных циклов или рекурсий, не использует.

reverse:  4.722221369
reverse_2:  2.6442769640000003
reverse_3:  0.8351227689999989
         17 function calls (10 primitive calls) in 3.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.001    3.001 <string>:1(<module>)
      8/1    0.000    0.000    0.000    0.000 task_3.py:20(revers)
        1    0.000    0.000    0.000    0.000 task_3.py:30(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:38(revers_3)
        1    0.000    0.000    3.000    3.000 task_3.py:49(main)
        1    0.000    0.000    3.001    3.001 {built-in method builtins.exec}
        3    3.000    1.000    3.000    1.000 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
