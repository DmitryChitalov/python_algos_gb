"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""


from random import randint
from timeit import timeit, default_timer
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return ''
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        num = f"{num}{revers(enter_num, revers_num)}"
    return num


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


#################################
num_10000 = randint(100000000, 10000000000000)
print(f"Исходное число: {num_10000}")

print(f"revers: {revers(num_10000)}")
print(f"revers_2: {revers_2(num_10000)}")
print(f"revers_3: {revers_3(num_10000)}")
print()


#################################
print(f"timeit revers: {timeit('revers(num_10000)', 'from __main__ import revers, num_10000', default_timer, 10000)}")
# >>> timeit revers: 0.11998919999999999
print(f"timeit revers_2: {timeit('revers_2(num_10000)', 'from __main__ import revers_2, num_10000', default_timer, 10000)}")
# >>> timeit revers_2: 0.0639102
print(f"timeit revers_3: {timeit('revers_3(num_10000)', 'from __main__ import revers_3, num_10000', default_timer, 10000)}")
# >>> timeit revers_3: 0.008097799999999988
print()

"""
Оценка времени с помощью timeit():
Первый вариант самый неудачный из-за рекурсии.
Второй вариант лучше, но третий вариант (через реверс строки) самый быстрый.
"""


#################################
cProfile.run('revers(num_10000)')
cProfile.run('revers_2(num_10000)')
cProfile.run('revers_3(num_10000)')

"""
Аналитика с помошью cProfile:
На первом варианте явно видна рекурсия, из-за чего первый вариант и показал худшее время.
Второй и третий варианты не имеют различий с точки зрения cProfile.
По этому выбрать между вторым и третьим вариантом помогает модуль trimeit.
"""
