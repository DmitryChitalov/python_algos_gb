"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from timeit import repeat, default_timer
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


def main():
    revers(8452)
    revers_2(8452)
    revers_3(8452)


if __name__ == '__main__':
    print(repeat("revers(8452)", "from __main__ import revers", default_timer, 3, 1000))
    print(repeat("revers_2(8452)", "from __main__ import revers_2", default_timer, 3, 1000))
    print(repeat("revers_3(8452)", "from __main__ import revers_3", default_timer, 3, 1000))
    cProfile.run('main()')

"""
по timeit видим, что третья реализация самая быстрая, поскольку использует встроенные механизмы питона для строк.
по cProfile видим, что revers_2 и revers_3 выполняется по одному разу, в то время как revers выполняется 5 раз, 
что позволяет сделать вывод, что из трех вариантов рекурсия самая меделенная.
в целом можно сделать вывод, что алгоритмы рекурсий медленне алгоритмов с циклами, 
алгоритмы с циклами медленне алгоритом в сипользованием встроенных механизов работы с данными.
"""