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
        return revers_num
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


enter_num = 50058585

print(timeit("revers(enter_num)", setup="from __main__ import revers, enter_num", number=10000))
print(timeit("revers_2(enter_num)", setup="from __main__ import revers_2, enter_num", number=10000))
print(timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num", number=10000))

def main():
    enter_num = 121345451232323123234545859859500585857798989787878787879898977878798978787989
    res_revers = revers(enter_num)
    res_revers_2 = revers_2(enter_num)
    res_revers_3 = revers_3(enter_num)


main()
cProfile.run('main()')
"""
0.04707900000000001
0.03310759999999999
0.007375300000000001
         85 function calls (7 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     79/1    0.000    0.000    0.000    0.000 task_3.py:18(revers)
        1    0.000    0.000    0.000    0.000 task_3.py:28(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:36(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:48(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
Дольше всего отрабатывает рекурсивный метод.
Срез без циклов быстрее.
"""