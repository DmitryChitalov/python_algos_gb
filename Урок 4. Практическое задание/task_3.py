"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

# реализация со срезами эффективнее по скорости выполнения,
# поскольку отсутствуют арифметические действия
from timeit import timeit
import cProfile


# рекурсия
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


# цикл
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# срез
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


enter_num = int(input('Введите целое число: '))
revers(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)

print('число наоборот на рекурсиях ', timeit(f'revers({enter_num})',
                                             setup='from __main__ import revers', number=10000))
print('число наоборот на циклах ', timeit(f'revers_2({enter_num})',
                                          setup='from __main__ import revers_2', number=10000))
print('число наоборот на срезах ', timeit(f'revers_3({enter_num})',
                                          setup='from __main__ import revers_3', number=10000))

cProfile.run('revers(1000000000)')
cProfile.run('revers_2(1000000000)')
cProfile.run('revers_3(1000000000)')
