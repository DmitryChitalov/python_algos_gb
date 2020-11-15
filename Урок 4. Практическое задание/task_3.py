"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from timeit import Timer
import cProfile

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

enter_num = int(input('Введите число: '))

revers(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)


rev = Timer(f"revers({enter_num})", "from __main__ import revers")
print("рекурсия ", rev.timeit(number=1000), "milliseconds")

rev_2 = Timer(f"revers_2({enter_num})", "from __main__ import revers_2")
print("цикл ", rev_2.timeit(number=1000), "milliseconds")

rev_3 = Timer(f"revers_3({enter_num})", "from __main__ import revers_3")
print("срез ", rev_3.timeit(number=1000), "milliseconds")


cProfile.run('revers(1000000)')
cProfile.run('revers_2(1000000)')
cProfile.run('revers_3(1000000)')

# Третья функция самма быстрая так как имеет констатнтную сложность