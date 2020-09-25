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

enter_num = 12355498754323578345908234572348967324

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

print(f'func_1(timeit) = {timeit("revers(enter_num)", setup="from __main__ import revers, enter_num")}')
print(f'func_2(timeit) = {timeit("revers_2(enter_num)", setup="from __main__ import revers_2, enter_num")}')
print(f'func_3(timeit) = {timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num")}')

cProfile.run('revers')
cProfile.run('revers_2')
cProfile.run('revers_3')

"""
timeit показывает большее время выподнения кода, в отличии от cprofile, за счет большего 
количества повторений кода.
Согласно cprofile - во всех 3 вариантах нет потерь времени при выполнении кода.
При замерах timeit: наиболее эффективен 3 вариант за счет использования срезов, в оставшихся 2 варантах 
постоянно перебираем существующий массив и так же дополняем новый, так же постоянно его перечитывая.
"""