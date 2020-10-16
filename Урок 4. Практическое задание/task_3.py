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

enter_num = 12345678998745


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


print(revers(enter_num))
print(revers_2(enter_num))
print(revers_3(enter_num))

cProfile.run('revers(enter_num)')
cProfile.run('revers_2(enter_num)')
cProfile.run('revers_3(enter_num)')

print(timeit.timeit("revers(enter_num)", setup="from __main__ import revers, enter_num", number=100000))
print(timeit.timeit("revers_2(enter_num)", setup="from __main__ import revers_2, enter_num", number=100000))
print(timeit.timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num", number=100000))

# нагляднее видно через timeit. Быстрее третья функция так номер преобразовывают в строку
# и возвращают элементы с конца в начало. В отсальных случаях время дольше
# потому что используют пербор всех цифр
