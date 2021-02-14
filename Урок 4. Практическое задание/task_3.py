"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from cProfile import run
from timeit import timeit

num = 2143434


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


print("Рекурсия")
print(
    timeit("revers(num)",
           setup='from __main__ import revers, num',
           number=10000))
print("Цикл")
print(
    timeit(
        "revers_2(num)",
        setup='from __main__ import revers_2, num',
        number=10000))
print("встроенные операции")
print(
    timeit(
        "revers_3(num)",
        setup='from __main__ import revers_3, num',
        number=10000))


def main():
    revers(num)
    revers_2(num)
    revers_3(num)


run("main()")

"""
revers_3() самая быстрая так как в ней нет рекурсивного вызова и нет итераций.
профайлер показал что реверс чере рекурсию запускал функцию несколько раз.
реверс функциями revers_3 и  revers_2 вызывались по одному разу. но в revers_2 использовался цикл"""
