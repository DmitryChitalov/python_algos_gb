"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
import timeit


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


n = 1234567890

print(cProfile.run('revers(n)'))
print(cProfile.run('revers_2(n)'))
print(cProfile.run('revers_3(n)'))
''' Через cProfile все функции дали хороший результат,
в функции revers идёт большее количество вызовов из-за рекурсии.
'''

print(timeit.timeit('revers(n)', setup='from __main__ import revers, n', number=100000))
print(timeit.timeit('revers_2(n)', setup='from __main__ import revers_2, n', number=100000))
print(timeit.timeit('revers_3(n)', setup='from __main__ import revers_3, n', number=100000))
'''Через модуль timeit видно, что:
фун revers_3 быстрее всех, т.к. используется срез строки
фун revers_2 средняя по скорости из-за вычислений в цикле
а фун revers медленнее из-за использования рекурсии
Вывод для решения такой задачи использовать функцию revers_3, со срезом строки
revers    # 0.29408631600017543
revers_2  # 0.18526349599960668
revers_3  # 0.040194991000134905
'''
