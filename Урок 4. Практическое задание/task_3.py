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


if __name__ == '__main__':
    enter_num = 9876543210
    revers_num = 100

    print("- " * 50)
    print("TimeIT for revers(enter_num, revers_num)   = {}".format(
        timeit.timeit("revers(enter_num, revers_num)", setup="from __main__ import revers, enter_num, revers_num",
                      number=100000)))
    print("TimeIT for revers_2(enter_num, revers_num) = {}".format(
        timeit.timeit("revers_2(enter_num, revers_num)", setup="from __main__ import revers_2, enter_num, revers_num",
                      number=100000)))
    print("TimeIT for revers_3(enter_num)             = {}".format(
        timeit.timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num", number=100000)))

    print("- " * 50)
    cProfile.run('revers(enter_num, revers_num)')
    cProfile.run('revers_2(enter_num, revers_num)')
    cProfile.run('revers_3(enter_num)')

"""
    Выполнена профилировка каждого алгоритма через cProfile и через timeit
    Первая функция имеет узкое место, на мой взгляд это условный оператор IF..ELSE, это показывает cProfile и timeit 
    
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     11/1    0.000    0.000    0.000    0.000 task_3.py:16(revers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


    TimeIT for revers(enter_num, revers_num)   = 0.341959244
    TimeIT for revers_2(enter_num, revers_num) = 0.18957468700000002
    TimeIT for revers_3(enter_num)             = 0.04538022500000005
    
    Самой быстрой является реализация 3-я функция в которой используется получение среза. 
    Что соответсвует уровню сложности O(n) 
    
    Мне кажется что с cProfile тоже можно научиться понимать результат. 
    Мне нравится что он показывает строки
    
"""
