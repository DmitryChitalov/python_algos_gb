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


# from task_2 import memoize


def revers(enter_num, revers_num=0):  # почему-то из коробки возвращает None
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = revers_num * 10 + num  # так вроде тоже самое
        enter_num //= 10
        # print(revers_num, enter_num)
        # revers(enter_num, revers_num) # в таком варианте функция вызывается, но  значение не возврашает
        return revers(enter_num, revers_num)  # дело было в этом ретурне, надеюсь это просто опечатка
        #  я не перемудрил и не сломал все, результаты по профайлеру не отличаются


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


def memoize(f):  # не получилось импортировать  из task_2 потому что  там структура не очень правильная,
    # а переделывать не стал чтобы проверять проще было, наверное. поэтому скопипастим декоратор из task_2
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            # print(cache[args])
            return cache[args]

    return decorate


@memoize
def revers_4(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = revers_num * 10 + num
        enter_num //= 10
        return revers_4(enter_num, revers_num)


if __name__ == '__main__':
    my_num = 12345678901234567890123456789012345678901234567890
    cProfile.run('revers(my_num)')
    cProfile.run('revers_2(my_num)')
    cProfile.run('revers_3(my_num)')

    """
     для всех 3х реализаций по профайлеру время не значительное, только в варианте рекурсии количество вызовов растет с 
     увеличением входного числа
     54 function calls (4 primitive calls) in 0.000 seconds
     4 function calls in 0.000 seconds
     4 function calls in 0.000 seconds 
    """

    print(
        timeit(
            'revers(my_num)',
            setup='from __main__ import revers, my_num',
            number=10000))
    print(
        timeit(
            'revers_2(my_num)',
            setup='from __main__ import revers_2, my_num',
            number=10000))
    print(
        timeit(
            'revers_3(my_num)',
            setup='from __main__ import revers_3, my_num',
            number=10000))
"""
0.15596929999999998
0.10461079999999998
0.005684599999999984
тестирование timeit-ом ожидаемо показало что рекурсия самая медленная, цикл побыстрее, обратный слайс в 
данном случае самое быстрое решение. Эффективнее всего - revers_3 т.к. самая быстрая, а быстрее цикла она скорее всего 
потому что внутри цикла еще математические действия производятся на каждой итерации. 
Но возможно все изменится если добавить мемоизацию для рекурсии все изменится. Попробуем:
"""

print(
    timeit(
        'revers_4(my_num)',
        setup='from __main__ import revers_4, my_num',
        number=10000))
"""
0.00224089999999999
Да мемоизация знатно помогла, время в 2 раза лучше чем у слайса.

Итог: из 3х представленых примеров по умолчанию - лучше версия со слайсом, т.к при тойже сложности что и у цикла O(n) 
она производит меньше операций в самой функции.
"""
