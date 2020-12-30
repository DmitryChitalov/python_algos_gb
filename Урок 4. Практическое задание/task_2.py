"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

1 Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?  <<<--- !!
2 Если у вас есть идеи, предложите вариант оптимизации.
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return ''  # str(number % 10)
    """
    str(number % 10) будет ошибкой, т.к. например 7163623279150 вернет 05197232636170 лишний 0 на конце
    """
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print(recursive_reverse(num_10000))  # 7163623279150
print(recursive_reverse(num_1000))
print(recursive_reverse(num_100))

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


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
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

"""
1 Мемоизация значительно улучшает работу кода. 
  Результат работы кода:
                    Не оптимизированная функция recursive_reverse
                    0.017806
                    0.020412800000000002
                    0.038603200000000004
                    Оптимизированная функция recursive_reverse_mem
                    0.0019209000000000032
                    0.0018451000000000023
                    0.0020043999999999895
  По результатам видно, что мемоизация улучшает работу кода на порядок.  
"""


"""
2 попытаемся оптимизировать код. преобразуем число к строке и восплоьзуемся извлечением среза.
"""
print(str(num_100)[::-1])


def func_opt(num):
    number = str(num)[::-1]
    return number


print('Моя функция func_opt')
print(
    timeit(
        "func_opt(num_100)",
        setup='from __main__ import func_opt, num_100',
        number=10000))
print(
    timeit(
        "func_opt(num_1000)",
        setup='from __main__ import func_opt, num_1000',
        number=10000))
print(
    timeit(
        "func_opt(num_10000)",
        setup='from __main__ import func_opt, num_10000',
        number=10000))


@memoize
def func_opt_mem(num):
    number = str(num)[::-1]
    return number


print('Та же функция с мемоизацией')
print(
    timeit(
        "func_opt_mem(num_100)",
        setup='from __main__ import func_opt_mem, num_100',
        number=10000))

print(
    timeit(
        "func_opt_mem(num_1000)",
        setup='from __main__ import func_opt_mem, num_1000',
        number=10000))
print(
    timeit(
        "func_opt_mem(num_10000)",
        setup='from __main__ import func_opt_mem, num_10000',
        number=10000))

"""
Результат:
Моя функция func_opt
0.0028903000000000123
0.0029244999999999965
0.0031798999999999994
Моя функция с мемоизацией func_opt
0.001841399999999993
0.001850500000000005
0.001992899999999992

Как видим реверс строки методом извлечения среза значительно эфективнее рекурсии.
Однако мемоизация значительно ускоряет выполнение рекурсии и делает ее практически сопоставимой
по времени выполнения с другими более быстрыми методами.
Таким образом можем сделать вывод, что в предложенном примере мемоизация была необходима.
"""