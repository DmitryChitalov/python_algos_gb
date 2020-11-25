"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile
from timeit import default_timer


    # Example: recursive fibonacci sequence

n_th = 25

@profile
def rec(n_th):
    def fib_func_1(num):
        if num <= 1:
            return num
        else:
            return(fib_func_1(num - 1) + fib_func_1(num - 2))
    return f'The {n_th} element of the sequence is {fib_func_1(n_th)}'


start_time = default_timer()
rec(n_th)
print(f'The recursive fibonacci sequence runs for {default_timer() - start_time} sec.')



''' 
У меня сперва очень странный результат получился: profiler пробегает функцию (n*2 + 1) раз, каждый раз печатая отдельный результат.
Потом я вспомнил про обертку и решил сделать все через декоратор - но не вышло, т.к. постоянно вылезали ошибки. 
Затем уже я решил, что обертка - это функция в функции - и тут код начал работать (и оказалось, что сделал я схожим образом, как Вы
показали в разборе). 
Но у меня тут прям магия: на относительно крупных числах - вроде 25 - моя рекурсивная функция не ест, а освобождает память, например:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     13.1 MiB     13.1 MiB           1   @profile
    18                                         def rec(n_th):
    19     13.1 MiB -425788.5 MiB      242786       def fib_func_1(num):
    20     13.1 MiB -425789.8 MiB      242785           if num <= 1:
    21     13.1 MiB -212910.3 MiB      121393               return num
    22                                                 else:
    23     13.1 MiB -212932.3 MiB      121392               return(fib_func_1(num - 1) + fib_func_1(num - 2))
    24      9.8 MiB     -3.3 MiB           1       return f'The {n_th} element of the sequence is {fib_func_1(n_th)}'


The recursive fibonacci sequence runs for 31.003692609999998 sec.

    или 

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    17     13.0 MiB     13.0 MiB           1   @profile
    18                                         def rec(n_th):
    19     13.0 MiB -969277.5 MiB      392836       def fib_func_1(num):
    20     13.0 MiB -969278.4 MiB      392835           if num <= 1:
    21     13.0 MiB -484653.7 MiB      196418               return num
    22                                                 else:
    23     13.0 MiB -484682.7 MiB      196417               return(fib_func_1(num - 1) + fib_func_1(num - 2))
    24      9.6 MiB     -3.5 MiB           1       return f'The {n_th} element of the sequence is {fib_func_1(n_th)}'
    

- и вот тут я уже теряюсь в догадках, почему так...

'''
