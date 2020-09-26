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


print(
    timeit(
        'revers(1000000)',
        setup='from __main__ import revers',
        number=10000))
print(
    timeit(
        'revers_2(1000000)',
        setup='from __main__ import revers_2',
        number=10000))
print(
    timeit(
        'revers_3(1000000)',
        setup='from __main__ import revers_3',
        number=10000))


cProfile.run("""
for i in range(0, 100000):
    revers(1000000)
""")
cProfile.run("""
for i in range(0, 100000):
    revers_2(1000000)
""")
cProfile.run("""
for i in range(0, 100000):
    revers_3(1000000)
""")


"""
Вывод: реализации идут по эффективности в порядке от худшей к лучшей. 
Наиболее эффективна 3 реализация, т.к. она переворачивает число в виде строки в одно действие, 
не используя циклы и рекурсии. 
"""
