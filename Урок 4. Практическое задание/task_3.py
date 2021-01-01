"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from random import randint
import timeit
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


num = randint(100000000, 1000000000)

print(timeit.timeit("revers(num)", setup="from __main__ import revers, num", number=1000))
print(timeit.timeit("revers_2(num)", setup="from __main__ import revers_2, num", number=1000))
print(timeit.timeit("revers_3(num)", setup="from __main__ import revers_3, num", number=1000))

def main():
    revers(num)
    revers_2(num)
    revers_3(num)

cProfile.run('main()')



'''Первая функция -  самая долгая, т.к. это рекурсия. Функция revers_2 использует циклы, это не оптимальный вариант, но 
быстрее рекурсии. Первая и вторая функции используют в своем теле матемачиеские вычисления, что требует определенного 
времени Третья функция самая быстрая: использует встроенные функции - срез, соответственно лучше использовать его
для решения задачи. сProfile показывает, что все функции по времени отрабатывают одинаково по нулям. Но и модуль timeit,
 если считать до сотых, выводит одни и те же значения'''
