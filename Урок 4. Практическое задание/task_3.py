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


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


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


user_in = 1223334444555556666667777777888888889999999990  # int(input('Введите число: '))
print(f'Введенное число = {user_in}')

print(f'Перевернутое число через "revers_1" = {revers_1(user_in)}')
print(f'Перевернутое число через "revers_2" = {revers_2(user_in)}')
print(f'Перевернутое число через "revers_3" = {revers_3(user_in)}')

print(f'revers_1 = '
      f'{timeit("revers_1(user_in)", setup="from __main__ import revers_1, user_in")}')

print(f'revers_2 = '
      f'{timeit("revers_2(user_in)", setup="from __main__ import revers_2, user_in")}')

print(f'revers_3 = '
      f'{timeit("revers_3(user_in)", setup="from __main__ import revers_3, user_in")}')

cProfile.run('revers_1(user_in)')
cProfile.run('revers_2(user_in)')
cProfile.run('revers_3(user_in)')

'''
Вывод: 3 метод самый эффективный т.к. отрабатывает быстрее всего и к тому же парвильно
'''
