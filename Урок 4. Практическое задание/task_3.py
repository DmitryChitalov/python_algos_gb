"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile
"""
Результаты профилировки через cProfile:

 ncalls          tottime  percall  cumtime  percall filename:lineno(function)
700000/100000    0.343    0.000    0.343    0.000   task_3.py:15(revers)
   100000        0.164    0.000    0.164    0.000   task_3.py:25(revers_2)
   100000        0.047    0.000    0.047    0.000   task_3.py:33(revers_3)
   
Результаты профилировки через timeit: 
0.17308659999999998
0.11594280000000001
0.03763439999999996

Самая эффективная реализация через срезы(почти в 4 раза быстрее), встроенные функции в питоне работают быстро.
"""


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


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


def main(x):
    for _ in range(100000):
        revers(x)
        revers_2(x)
        revers_3(x)


number = 123456
cProfile.run('main(number)')
print(timeit.timeit("revers(number)", setup="from __main__ import revers, number", number=100000))
print(timeit.timeit("revers_2(number)", setup="from __main__ import revers_2, number", number=100000))
print(timeit.timeit("revers_3(number)", setup="from __main__ import revers_3, number", number=100000))


