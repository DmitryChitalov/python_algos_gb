"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

1 Сделайте профилировку каждого алгоритма через 1a) cProfile и через 1b) timeit

2 Сделайте вывод, какая из трех реализаций эффективнее и почему
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


enter_user_num = 716362327915

# 1b
print('Профилировка через timeit:')
print(timeit('revers(enter_user_num)',
             setup='from __main__ import revers, enter_user_num',
             number=1000),
      'секунд для первой реализации')
print(timeit('revers_2(enter_user_num)',
             setup='from __main__ import revers_2, enter_user_num',
             number=1000),
      'секунд для второй реализации')
print(timeit('revers_3(enter_user_num)',
             setup='from __main__ import revers_3, enter_user_num',
             number=1000),
      'секунд для третьей реализации')

"""
результат:
0.004503299999999995 секунд для первой реализации
0.0026931999999999998 секунд для второй реализации
0.00036289999999999933 секунд для третьей реализации
значит третья реализация эффективнее второй и первой.
"""

# 1a


def profile_func():
    res_1 = revers(enter_user_num)
    res_2 = revers_2(enter_user_num)
    res_3 = revers_3(enter_user_num)


print('Профилировка через cProfile')
cProfile.run('profile_func()')
