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


num = 123456789

print('Первый вариант:')
print(timeit(
    'revers(num)',
    setup='from __main__ import revers, num',
    number=10000))
cProfile.run('revers(num)')

print('Второй вариант:')
print(timeit(
    'revers_2(num)',
    setup='from __main__ import revers_2, num',
    number=10000))
cProfile.run('revers_2(num)')

print('Третий вариант:')
print(timeit(
    'revers_3(num)',
    setup='from __main__ import revers_3, num',
    number=10000))
cProfile.run('revers_3(num)')

"""
Самый быстрый - третий вариант, срез. Реверс самый меделенный, т.к. идет многократный вызов функции самой себя.
Профалер это показывает, в моем случае функция вызывается 10 раз. Второй вариант работает быстрее, т.к. там идет
просто перебор каждой цифры в цикле, но третий вариант самый быстрый, т.к. используется одна единственна функция
среза строки.
"""