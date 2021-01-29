"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""


from timeit import timeit
from cProfile import run
from random import randint


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


num = randint(10, 1000)
print('Меряем при помощи timeit')
print(f'Результаты работы функции revers: {timeit("revers(num)", globals=globals())}')
print(f'Результаты работы функции revers_2: {timeit("revers_2(num)", globals=globals())}')
print(f'Результаты работы функции revers_3: {timeit("revers_3(num)", globals=globals())}')

print('Меряем при помощи cProfile')
print(f'Результаты работы функции revers:')
run('revers(num)')
print(f'Результаты работы функции revers_2:')
run('revers_2(num)')
print(f'Результаты работы функции revers_3:')
run('revers_3(num)')

"""
Вывод: вариант 3 - лучшее решение
по результатам cProfile вариант 1 проигрывает по количеству вызовов, вырианты 2 и 3 идентичны
по результатам timeit вариант 3 показал лучший результат
"""
