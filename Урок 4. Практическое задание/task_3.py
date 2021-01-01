"""
Задание 3.
Приведен код, формирующий из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
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


number = int(input('Введите число: '))
print("revers", timeit.timeit("revers(number)", setup="from __main__ import revers, number", number=1000))
print("revers_2", timeit.timeit("revers_2(number)", setup="from __main__ import revers_2, number", number=1000))
print("revers_3", timeit.timeit("revers_3(number)", setup="from __main__ import revers_3, number", number=1000))

cProfile.run('revers(number)')
cProfile.run('revers_2(number)')
cProfile.run('revers_3(number)')

"""
Скорость работы функции реализованной через срез на порядок выше (из-за отсутствия вычислений), чем остальные, 
что указывает на ее эффективность.
"""