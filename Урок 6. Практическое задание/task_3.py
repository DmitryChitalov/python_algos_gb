"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from memory_profiler import profile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


@profile
def func(enter_num):
    revers(enter_num)


func(123456)


"""
Профилировать с рекурсией напрямую не получится, потому что профилировка будет вызываться то количество раз, которое 
будет вызываться рекурсия. А если обернуть в еще одну функцию, то работает
"""