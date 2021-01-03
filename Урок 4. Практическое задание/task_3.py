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


def main():
    revers(10000000000)
    revers_2(10000000000)
    revers_3(10000000000)


if __name__ == '__main__':
    print(timeit('revers(10000000000)', 'from __main__ import revers'))
    print(timeit('revers_2(10000000000)', 'from __main__ import revers_2'))
    print(timeit('revers_3(10000000000)', 'from __main__ import revers_3'))

    cProfile.run('main()')


"""
Результаты:

2.6250392000000002
1.7766324
0.31328650000000025
         18 function calls (7 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     12/1    0.000    0.000    0.000    0.000 test.py:16(revers)
        1    0.000    0.000    0.000    0.000 test.py:26(revers_2)
        1    0.000    0.000    0.000    0.000 test.py:34(revers_3)
        1    0.000    0.000    0.000    0.000 test.py:40(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


    В задачах использовались Рекурсия, цикл и срез
    Исходя из полученных результатов срез - самый быстрый, а
    рекурсия и цикл имеют дополнительные действия, как следствие
    в скорости работы проигрывают срезу.
"""



