"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile

a = 123456789


# это рекурсивный метод решения и он гораздо больше затрачивает время чем другие варианты из-за стека вызовов
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


# здесь поступающее число переводиться в строку и с помощью среза с шагом -1 присваивается переменной revers_num
# этот вариант быст из-за встроенных функций и среза
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(cProfile.run(revers_3(a)))
print(timeit(stmt='revers(a)', setup='from __main__ import revers,a', number=100000))
print(timeit(stmt='revers_2(a)', setup='from __main__ import revers_2,a', number=100000))
print(timeit(stmt='revers_3(a)', setup='from __main__ import revers_3,a', number=100000))
