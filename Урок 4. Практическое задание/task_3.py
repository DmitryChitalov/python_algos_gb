"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import timeit, cProfile

enter_num = 12345


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
    revers(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)


## через timeit
print('Время для 1 функции составило:')
print(
    timeit.timeit(
        "revers(enter_num)",
        setup="from __main__ import revers, enter_num",
        number=1000))  ## 0.0035573980057961307

print('Время для 2 функции составило:')
print(
    timeit.timeit(
        "revers_2(enter_num)",
        setup="from __main__ import revers_2, enter_num",
        number=1000))  ## 0.0021882380024180748

print('Время для 3 функции составило:')
print(
    timeit.timeit(
        "revers_3(enter_num)",
        setup="from __main__ import revers_3, enter_num",
        number=1000))  ## 0.0007074290042510256

## через cProfile

cProfile.run('main()')
"""
Проанализировав функции разными способами видно, что функция revers_3 выполняется быстрее остальных. Первая функция затрачивает много времени, так как используется рекурсия (нужно оптимизировать). 
Во 2 функции используется цикл, что усложняет код. В 3 варианте используются срезы, а так как это встроенная функция, время затрачивается меньше остальных.
"""
