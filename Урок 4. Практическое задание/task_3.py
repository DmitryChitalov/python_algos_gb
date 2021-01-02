"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import timeit

enter_num = 1234567890123456789


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


def mein():
    num = 1234567890123456789
    revers(num)
    revers_2(num)
    revers_3(num)


cProfile.run('mein()')
cProfile.run('revers(1234567890123456789)')
cProfile.run('revers_2(1234567890123456789)')
cProfile.run('revers_3(1234567890123456789)')

# Через cProfile ничего не видно, везде только 0.

num = 1234567890123456789

print('revers : ', timeit(f'revers({num})', setup='from __main__ import revers', number=10000))
print('revers_1 : ', timeit(f'revers_2({num})', setup='from __main__ import revers_2', number=10000))
print('revers_2 : ', timeit(f'revers_3({num})', setup='from __main__ import revers_3', number=10000))

# Результаты через timeit
# revers :  0.10920490000000001
# revers_1 :  0.06533070000000002
# revers_2 :  0.006191900000000028
# Видно, что саммый эффективный способ revers_2, через срез. Оно объясняется тем, что тут нет циклов, еслить только
# присвоение одного символа. Самый неэффективный, как всегда, рекурсия, revers. Занимает больше памяти чтобы пройти
# туда-обратно по сравнению с циклом.
