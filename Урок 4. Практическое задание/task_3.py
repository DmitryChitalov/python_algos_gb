"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit, cProfile


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


def main():
    number = 654789654984312489651187435498465187451968463519864515641984654986521784165187416518974132484654151298
    revers(number)
    revers_2(number)
    revers_3(number)


cProfile.run("main()")

num = 654789
print(timeit.timeit("revers(num)", setup="from __main__ import revers, num"))
print(timeit.timeit("revers_2(num)", setup="from __main__ import revers_2, num"))
print(timeit.timeit("revers_3(num)", setup="from __main__ import revers_3, num"))

"""
cProfile:
    Все по нулям, это значит, что нет задач с потерями времени.
timeit:
    При многократном запуске видно, что рекурсия работает медленее всего, а revers_3 работает быстрее всего,
    т.к. там используются только встроенные фун-ии.
Вывод:
    При многократном замере времени через timeit мы видим, что есть разница во времени и что фун-я revers_3
    самая быстрая. Но cProfile дает понять, что задач с потерями времени нет, поэтому спокойно можно 
    писать и рекурсию(красивее, интереснее, профессиональее и престижнее). А revers_2 вообще while.
"""
