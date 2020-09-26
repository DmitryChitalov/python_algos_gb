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


print(timeit.timeit('revers', setup='from __main__ import revers', number=1000))
cProfile.run('revers')
print(timeit.timeit('revers_2', setup='from __main__ import revers_2', number=1000))
cProfile.run('revers_2')
print(timeit.timeit('revers_3', setup='from __main__ import revers_3', number=1000))
cProfile.run('revers_3')

'''
Последняя функция более эффективнее, так как использует встроенныую функцию(срез), а они всегда быстрее.
'''
