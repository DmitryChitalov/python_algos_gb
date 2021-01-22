"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import timeit

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
    return revers_num


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

my_numb = 94567889288928437556748793865032759134854350439751707359183459

def reverse():
    my_numb = 94567889288928437556748793865032759134854350439751707359183459
    res_count = revers(my_numb)
    res_sum = revers_2(my_numb)
    res_sum = revers_3(my_numb)


cProfile.run('reverse()')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     75/1    0.000    0.000    0.000    0.000 task_3.py:14(revers)
#        1    0.000    0.000    0.000    0.000 task_3.py:25(revers_2)
#        1    0.000    0.000    0.000    0.000 task_3.py:33(revers_3)
#        1    0.000    0.000    0.000    0.000 task_3.py:38(reverse)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit("revers(my_numb)", setup="from __main__ import revers, my_numb", number=1000))     # 0.021938457
print(timeit("revers_2(my_numb)", setup="from __main__ import revers_2, my_numb", number=1000)) # 0.017449446
print(timeit("revers_3(my_numb)", setup="from __main__ import revers_3, my_numb", number=1000)) # 0.000739713000000003


# Для данных функций лучше использовать модуль timeit, т.к. сProfile не может проверить такое небольшое кол-во данных. 
# Проверка времени работы 3-х вариантов показала, что третья функция - revers_3() намного эффективнее, чем две другие.