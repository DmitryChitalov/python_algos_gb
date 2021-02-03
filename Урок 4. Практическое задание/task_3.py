"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
from random import randint
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


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def revers_plus_memo(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


my_lst = randint(10 ** 30, 10 ** 40)

print(timeit("revers(my_lst)", globals=globals(), number=10000))  # 0.1543315
print(timeit("revers_2(my_lst)", globals=globals(), number=10000))  # 0.1096354
print(timeit("revers_3(my_lst)", globals=globals(), number=10000))  # 0.0067128
print(timeit("revers_plus_memo(my_lst)", globals=globals(), number=10000))  # 0.0023492


def main():
    revers(my_lst)
    revers_2(my_lst)
    revers_3(my_lst)
    revers_plus_memo(my_lst)


run('main()')

"""
ещё добавил вариант с мемоизацией рекурсии, что сократило время её работы более чем в 65 раз
за счёт сокращения количества подсчетов.
 
Самой долго конечно будет рекурсия revers, т.к. приходитися каждый раз высчитывать значения
Далее идет revers_2, тут тоже нужны математические расчеты, потому она занимает определенное время
а в revers_3 просто срезы, потому время минимальное
хотя рекурсия с мемоизацией работает ещё в 3 раза быстрее, чем срезы...
"""
