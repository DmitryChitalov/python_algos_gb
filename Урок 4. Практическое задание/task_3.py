"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit, cProfile

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
    num = 1234567891234567891247821
    res_1 = revers(num)
    res_2 = revers_2(num)
    res_3 = revers_3(num)

cProfile.run('main()')
print(timeit.timeit("revers(1234567891234567891247821459663457)", setup="from __main__ import revers", number = 100000))
print(timeit.timeit("revers_2(1234567891234567891247821459663457)", setup="from __main__ import revers_2", number = 100000))
print(timeit.timeit("revers_3(1234567891234567891247821459663457)", setup="from __main__ import revers_3", number = 100000))

"""Третья реализация эффективнее, так как применяется встроенная
функция str и срез строки, а первая наиболее затратная по времени, 
так как применяется рекурсия"""