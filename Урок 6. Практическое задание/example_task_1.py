"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!."""
from memory_profiler import profile

# профайл не выполняется, так как функция возвращает генератор, что есть хорошо
@profile
def fact(number):
    """Факториал числа
    :param number: int
    :return: generator
    """
    number_fact = 1
    for i in range(1, number+1):
        number_fact *= i
        yield number_fact


@profile
def fact_2(number):
    number_fact = 1
    for i in range(number):
        number_fact *= (i + 1)
    return number_fact
"""Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     13.0 MiB     13.0 MiB           1   @profile
    22                                         def fact_2(number):
    23     13.1 MiB      0.0 MiB           1       number_fact = 1
    24     13.1 MiB      0.0 MiB         101       for i in range(number):
    25     13.1 MiB      0.0 MiB         100           number_fact *= (i + 1)
    26     13.1 MiB      0.0 MiB           1       return number_fact"""


if __name__ == '__main__':
    n = 100
    i = 1
    for el in fact(n):
        print(f'{i}! = {el}')
        i += 1

    fact_2(n)
