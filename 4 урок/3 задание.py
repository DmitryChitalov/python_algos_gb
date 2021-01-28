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

def main():
    a = 12345
    revers__1 = revers(a)
    revers__2 = revers_2(a)
    revers__3 = revers_3(a)

cProfile.run('main()')
print(timeit("revers(12345)", setup = "from __main__ import revers", number = 1000000))
print(timeit("revers_2(12345)", setup = "from __main__ import revers_2", number = 1000000))
print(timeit("revers_3(12345)", setup = "from __main__ import revers_3", number = 1000000))

# Наиболее эфективна третья реализация так как она выполняется быстрее остальных