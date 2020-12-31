"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
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


def main():
    # number = 456789987654321
    revers(number)
    revers_2(number)
    revers_3(number)


# number = int(input("Введите число "))
number = 23456
# print(revers(number))
# print(revers_2(number))
# print(revers_3(number))

# В комментариях время исполнения:
print(timeit.timeit("revers(number)", setup="from __main__ import revers, number"))         # 1.88
print(timeit.timeit("revers_2(number)", setup="from __main__ import revers_2, number"))     # 1.22
print(timeit.timeit("revers_3(number)", setup="from __main__ import revers_3, number"))     # 0.56


cProfile.run('main()')
""" 
1. Самая эффективная функция 'revers_3' По сложности самая простая - берется срез строки, встроенная функция
2. По замерам функция 'revers_3' меньше всех затрачивает времени
3. Вызовов рекурсивной функции 6 раз (ncalls; number = 23456)
"""
