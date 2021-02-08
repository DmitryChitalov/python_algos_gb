"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
from cProfile import run


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


def test_1():
    return timeit(
        'revers(g_test_num)',
        setup='from __main__ import revers, g_test_num',
        number=10000)


def test_2():
    return timeit(
        'revers_2(g_test_num)',
        setup='from __main__ import revers_2, g_test_num',
        number=10000)


def test_3():
    return timeit(
        'revers_3(g_test_num)',
        setup='from __main__ import revers_3, g_test_num',
        number=10000)


def main():
    test_1()
    test_2()
    test_3()


g_test_num = 1234567890
print(test_1(), test_2(), test_3())
print()
run('main()')
# revers_2 лучше revers потому,что нет накладных расходов на стэк:
# это показывает столбец ncalls для строки "task_3.py:16(revers)",
# было 110000 вызовов функции revers.
# revers_3 лучше revers_2 потому, что нет ненужных делений на целое
# и остаток, а сразу перемещается символ, причем применяются
# встроенные функции питона, которые оптимизированы на
# быстродействие.
# Итого: revers_3 самая быстродействующая функция: это
# демонстрируют и timeit, и cProfile(столбец tottime) в параметре общего
# времени выполнения.
