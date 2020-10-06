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
a = 123456789


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


print(timeit.timeit(
    'revers(a)',
    setup='from __main__ import revers, a',
    number=10000))
print(timeit.timeit(
    'revers_2(a)',
    setup='from __main__ import revers_2, a',
    number=10000))
print(timeit.timeit(
    'revers_3(a)',
    setup='from __main__ import revers_3, a',
    number=10000))
cProfile.run('revers(a)')
cProfile.run('revers_2(a)')
cProfile.run('revers_3(a)')


# последняя функция самая эффективная, потому что она использует встроенные фунцкии и срезы,
# сама медленная это первая (там рекурсия)
