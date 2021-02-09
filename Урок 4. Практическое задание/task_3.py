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


number = 4264646724154745416546744124687464654351468764123164797

print('Функция revers:')
print(timeit(f"revers({number})", setup="from __main__ import revers", number=100000))
run('revers(number)')

print('Функция revers_2:')
print(timeit(f"revers_2({number})", setup="from __main__ import revers_2", number=100000))
run('revers_2(number)')

print('Функция revers_3:')
print(timeit(f"revers_3({number})", setup="from __main__ import revers_3", number=100000))
run('revers_3(number)')

"""
Функция revers сделана через рекурсию. Она выполняется дольше всего, так как вызывает себя же, cProfile показывает, 
что функция вызывается 59 раз и только 4 - без рекурсии. Запрос выполняется очень долго, в моем примере - 4.84 секунды.

Функция revers_2 сделана через цикл while. Выполняется быстрее чем функция, написанная через рекурсию - 3.31 секунды.

Лучше всего показывает себя функция revers_3, написанная без использования рекурсии или цикла - через конструкцию языка.
Выполняется всего 0.18 секунды и разрыв от остальных функций становится больше, если используется более длинное число.
"""
