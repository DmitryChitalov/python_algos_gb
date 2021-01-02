"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
import timeit


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
    my_num = 90869854646980809695
    revers(my_num)
    revers_2(my_num)
    revers_3(my_num)


cProfile.run('main()')

my_num = 90869854646980809695
print('Время работы функции revers')
print(timeit.timeit(f"revers({my_num})", setup="from __main__ import revers", number=1000))
print('Время работы функции revers_2')
print(timeit.timeit(f"revers_2({my_num})", setup="from __main__ import revers_2", number=1000))
print('Время работы функции revers_3')
print(timeit.timeit(f"revers_3({my_num})", setup="from __main__ import revers_3", number=1000))
'''
По результату работы видно, что revers_3 быстрее остальных функций, 
т.к. использует встроенные возможности языка,а именно,  срезы. 
    Насколько я понял использование внутренних функций всегда лучше,
 т.к. они уже оптимизированы под скорость выполнения.
'''
