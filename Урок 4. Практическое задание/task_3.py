"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from timeit import timeit, default_timer, repeat, Timer
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

number = int(input("Введите число: "))

print("This is revers() time:", timeit("revers(number)", "from __main__ import revers, number", number=1000))

print("This is revers_2() time:", repeat("revers_2(number)",
                                         "from __main__ import revers_2, number", default_timer, 5, 1000))

t1 = Timer("revers_3(number)", "from __main__ import revers_3, number")
print("This is revers_3() time:", t1.timeit(number=1000))


def run_all(enter_num):
    revers(number)
    revers_2(number)
    revers_3(number)


cProfile.run("run_all(number)")

"""
Быстрее всех выполняется функция с проходом списка в обратном направлении. 
В целом, как видно из сводки запуска cProfile, все функции выполняются быстро и не требуют дополнительной оптимизации
"""