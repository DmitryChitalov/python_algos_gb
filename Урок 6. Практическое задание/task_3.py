"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile


@profile()
def my_func():
    def rev(number, n_rev='16378163509'):
        if number == 0:
            return n_rev
        else:
            n = str(number % 10)
            return rev(number//10, n_rev + n)


my_func()


"""
Для профилирования памяти скрипта с рекурсией следует
рекурсию реализовать как вложенную функцию, что позволит нам избежать
многократного профилирования памыти при каждом вызове рекурсивной функции.
"""