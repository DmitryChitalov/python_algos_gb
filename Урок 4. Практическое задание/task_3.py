"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
from random import randint
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


test_num = randint(100000, 10000000)


def main():
    num = randint(1000, 10000)
    revers(num)
    revers_2(num)
    revers_3(num)


print("Оценка скорости работы функций с помощью модуля timeit")

print(timeit("revers(test_num)", setup="from __main__ import revers, test_num", number=1000))
print(timeit("revers_2(test_num)", setup="from __main__ import revers_2, test_num", number=1000))
print(timeit("revers_3(test_num)", setup="from __main__ import revers_3, test_num", number=1000))

print('Оценка скорости работы функций с помощью модуля cProfile')

cProfile.run("main()")

"""
Анализ скорости выполнения приведённых алгоритмов показал, что функция revers_3, использующая срез, наиболее эффективна 
для решения данной задачи. Рекурсивная функция revers показала самые плохие результаты по времени. 
Модуль timeit в данном случае более информативен, чем модуль cProfile и позволяет оценить скорость работы по 
конкретным значениям временных замеров, тогда как cProfile 
демонстрирует общую картину эффективности всех трёх алгоритмов. 
"""



