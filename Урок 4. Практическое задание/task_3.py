"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from timeit import timeit
from random import randint
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


nums = randint(100, 100000)
print('Замеры времени выполнения: ')
print(
    timeit(
        "revers(nums)",
        setup="from __main__ import revers, nums",
        number=1000))
print(
    timeit(
        "revers_2(nums)",
        setup="from __main__ import revers_2, nums",
        number=1000))
print(
    timeit(
        "revers_3(nums)",
        setup="from __main__ import revers_3, nums",
        number=1000))


"""def main():
    func_massive = {revers: nums,
                    revers_2: nums,
                    revers_3: nums
                    }
    for i in func_massive:
        print(i)
        return func_massive[i]
"""


def main():
    nums = randint(100, 100000)
    revers(num)
    revers_2(num)
    revers_3(num)


cProfile.run("main")

"""
Относитлеьно скорости == первая функция бустрее прочих (срезы)
сProfile - не может дать более точное предстваление
для проведения реальной аналитики
в сравнении с timeit
"""
