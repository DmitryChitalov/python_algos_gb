"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

from timeit import timeit
import cProfile


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


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


def print_timeit(func: str, text: str, number=100000):
    print(f"{text} {timeit(func, globals=globals(), number=number)}")


n = 10000
cProfile.run(f'revers_1({n})')
cProfile.run(f'revers_2({n})')
cProfile.run(f'revers_3({n})')
print_timeit(f'revers_1({n})', 'revers_1')
print_timeit(f'revers_2({n})', 'revers_2')
print_timeit(f'revers_3({n})', 'revers_3')

"""
revers_1 0.3041899
revers_2 0.15316120000000005
revers_3 0.0661872
revers_3 быстрее видимо в виду того, что арифм.операции с числами не выполняются
"""
