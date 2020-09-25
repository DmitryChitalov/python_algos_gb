"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""


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



print(timeit("revers(123456789)", setup="from __main__ import revers", number=10000))
print(timeit("revers_2(123456789)", setup="from __main__ import revers_2", number=10000))
print(timeit("revers_3(123456789)", setup="from __main__ import revers_3", number=10000))
print()


def main():
    revers(123456789)
    revers_2(123456789)
    revers_3(123456789)


cProfile.run('main()')


# Время выполнения revers: 0.036882399999999996
# Время выполнения revers_2: 0.02354300000000001
# Время выполнения revers_3: 0.0055225
#
# Исходя из вышепредставленных чисел, можно сделать вывод о том,
# что решение задачи через срезы (revers_3) является самым оптимальным и быстрым способом, 
# в то время, как решение через рекурсию (revers) показало наихудший результат по времени
#
#
#
#    16 function calls (7 primitive calls) in 0.000 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      10/1    0.000    0.000    0.000    0.000 3.py:14(revers)
#         1    0.000    0.000    0.000    0.000 3.py:24(revers_2)
#         1    0.000    0.000    0.000    0.000 3.py:32(revers_3)
#         1    0.000    0.000    0.000    0.000 3.py:43(main)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Профилировщик не выявил уязвимых мест у функций, однако, стоит отметить,
# что функция revers вызывалась 10 раз, в то время, как остальные функции -
# всего по одному разу, что лишний раз подтверждает то, что решение через
# рекурсию - не самое оптимальное, с точки зрения производительности
