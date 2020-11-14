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
        return revers(enter_num, revers_num)


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


# timeit:

'''
Вышло ожидаемо - особенно после замеров в task_2: последняя функция - revers_3 - отработала значительно быстрее, т.к.
использовала встроенные функции. Вторая - reverse_2 - "пришла" второй: в ней замедлил выполнение цикл. Первая - рекурсивная -
ожидаемо стала самой медленной в выполнении, т.к. отсутствует мемоизация.
'''

import timeit

enter_num = 12345

print(timeit.timeit('revers(enter_num)', setup = 'from __main__ import revers, enter_num', number= 1000))
print(timeit.timeit('revers_2(enter_num)', setup = 'from __main__ import revers_2, enter_num', number=1000))
print(timeit.timeit('revers_3(enter_num)', setup = 'from __main__ import revers_3, enter_num', number=1000))


# cProfile:

'''
Т.к. сложности функции - даже первой, рекурсивной - не велики, а время выполнения в итоге занимает меньше 1 сек, то 
ничего интрересного мне cProfile не показал. Только в таблице первой функции - revers - он мне выдал ncalls 6/1, но и только.
'''

import cProfile

cProfile.run('revers(enter_num)')
cProfile.run('revers_2(enter_num)')
cProfile.run('revers_3(enter_num)')




