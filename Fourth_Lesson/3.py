"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile, random
from timeit import  default_timer , repeat

"""
def memorize(func):
    cache = {}
    def wrapper(*args):
        if cache.get(args[0]):
           return cache[args[0]]
        else:
            cache[args[0]]=func(*args)
            return cache[args[0]]
    return wrapper

@memorize"""
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num) # было просто return, добавил revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)  # не было ключевого слова return, поэтому данная ф-я возвращала None


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

enter_n = random.randint(999999, 999999999)

print(repeat("revers(enter_n)",setup="from __main__ import revers, enter_n",timer=default_timer,repeat=3,number=100000))
print(repeat("revers_2(enter_n)",setup="from __main__ import revers_2, enter_n",timer=default_timer,repeat=3,number=100000))
print(repeat("revers_3(enter_n)",setup="from __main__ import revers_3, enter_n",timer=default_timer,repeat=3,number=100000))

"""
[0.41694265599999997, 0.41520307799999995, 0.4234878770000001]          reverse
[0.267906094, 0.26427915299999993, 0.2588705579999999]                  reverse_2
[0.05898345100000002, 0.060626554999999804, 0.061340346999999795]       reverse_3

Можно сделать вывод, что рекурсивный способ(первый) - самый медленный,
а оператор получения среза с шагом -1 - самый быстрый.
Я написал декоратор, который выполняет мемоизацию, что позволяет рекурсии опередить по скорости обе другие функции.
Вот новые результаты:

[0.037944323999999995, 0.037731878999999996, 0.03674458]  рекурсивная функция, но с мемоизацией
[0.261835535, 0.25437177699999997, 0.26000615800000004]
[0.05926722299999998, 0.05971879399999991, 0.05978088500000012]
"""


print(cProfile.run("revers(enter_n)"))
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      9/1    0.000    0.000    0.000    0.000 3.py:27(revers)    видим 9 вызовов рекурсии
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
print(cProfile.run("revers_2(enter_n)"))
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 3.py:37(revers_2)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
print(cProfile.run("revers_3(enter_n)"))
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 3.py:45(revers_3)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
Так как все функции за 1 выполнение требуют немного времени(даже рекурсивная функция), то закономерно можно видеть
результаты, представленные выше
"""