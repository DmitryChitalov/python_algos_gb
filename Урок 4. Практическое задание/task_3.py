"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from random import randint
import timeit
import cProfile


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


# Срез
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num = randint(100000, 100000000)

print(timeit.timeit("reverse(num)", setup="from __main__ import reverse, num", number=1000))
print(timeit.timeit("reverse_2(num)", setup="from __main__ import reverse_2, num", number=1000))
print(timeit.timeit("reverse_3(num)", setup="from __main__ import reverse_3, num", number=1000))


cProfile.run('revers(num)')
cProfile.run('revers_2(num)')
cProfile.run('revers_3(num)')


'''Не могу определить, в чем проблема - PyCharm выводит ошибку, посчитать время не смог. По логике первая функция должна
 быть самая долгая, т.к. это рекурсия. Функция revers_2 использует циклы, это не оптимальный вариант, но быстрее 
 рекурсии. Третья функция использует встроенные функции: срез (должен быть самым быстрым)'''