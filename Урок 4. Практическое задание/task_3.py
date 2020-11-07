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


input_val = int(input("Введите целое число: "))

setup = f'from __main__ import revers, revers_2, revers_3, input_val'
print(f'Время работы функции revers: {timeit("revers(input_val)", setup, number=10000)}')
print(f'Время работы функции revers_2: {timeit("revers_2(input_val)", setup, number=10000)}')
print(f'Время работы функции revers_3: {timeit("revers_3(input_val)", setup, number=10000)}')

cProfile.run(f'revers({input_val})')
cProfile.run(f'revers_2({input_val})')
cProfile.run(f'revers_3({input_val})')

"Функция, которая работает на срезах работает значительно быстрее"
