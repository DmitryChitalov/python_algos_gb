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
'''
def main():
    revers()
    revers_2()
    revers_3()
'''
print (timeit.timeit("revers()", setup="from_main_import revers", number=1000))

#cProfile.run('main()')
'''
  Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:38(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
'''
'''
Что то как то не идет у меня синтаксис timeit или я что то упустил или реально не вижу ошибку.
первый алгоритм средний по времени О(n) линейная переборка значений
второй алгоритм медленный, поскольку цикл, тоесть при больших объемах данных, время растет
третий быстрый  срез "строки" списка, что значительно уменьшает время на обработку данных и
снижает сложность 
'''