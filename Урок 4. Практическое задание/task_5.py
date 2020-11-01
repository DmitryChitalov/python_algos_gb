"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
from functools import wraps  # для устранения конфликтов имен в цепочках декораторов
from timeit import default_timer, timeit
import math
import logging


def time_decorator(some_func):
    """Вычисляет время выполения декорируемой функции"""

    @wraps(some_func)
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = some_func(*args, **kwargs)
        print(f'Время выполенения функции {some_func.__name__} c i = {args[0]} составило {default_timer() - start}. ')
        return result

    return wrapper


def log_decorator(some_func):
    """Логгирует события (какая функция и с какими параметрами запускалась)"""
    logging.basicConfig(filename='alg.log', level=logging.INFO)  # записываем событие в лог файл

    @wraps(some_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Запускалась функция {some_func.__name__} c параметром n = {args}')
        return some_func(*args, **kwargs)

    return wrapper


@log_decorator
@time_decorator
def simple(i):
    """Без использоания «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return f'Искомое число: {n}'


@log_decorator
@time_decorator
def sieve_of_eratosthenes(n):
    """С использованием «Решета Эратосфена»"""
    a = []
    for i in range(round(n * math.log2(n))):
        """
        Верхняя граница n-того простого числа лежит в пределах: (n log n, n (log n + log log n)). Взял нижний предел
        границы. Для нашего случая и диапазона значений отрабатывает верно.
        """
        a.append(i)
    a[1] = 0
    i = 2
    while i <= len(a) - 1:
        if a[i] != 0:
            j = i + i
            while j <= len(a) - 1:
                a[j] = 0
                j = j + i
        i += 1
    a = sorted(list(set(a)))  # убираем все нули кром одного и сортируем в порядке возрастания
    return f'Искомое число: {a[n]}'


if __name__ == '__main__':
    nums = [10, 100, 1000, 3000]
    for num in nums:
        print(simple(num))

    print('-' * 100)
    for num in nums:
        print(sieve_of_eratosthenes(num))

"""
Наивный алгоритм имеет квадратичную сложность. Классический алгоритм «Решето Эратосфена» имеет сложность 
O(N log (log N)).
Чем дальше в списке простых чисел находится искомое простое число, тем больше наивный алгоритм в скорости
проигрывает алгоритму с «Решетом Эратосфена», так как сложность наивного растет с квадратичной зависимостью.
У «Решета Эратосфена» рост линейно-логарифмический.
"""
