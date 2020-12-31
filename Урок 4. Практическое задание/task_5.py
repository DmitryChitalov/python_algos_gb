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
from timeit import timeit
max_num = 10000


def simple(i):
    """Без использования «Решета Эратосфена»"""
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
    return n


def simple_er(num):
    arr = [i for i in range(max_num)]
    arr[1] = 0
    for el in arr:
        if el > 1:
            for multiple in range(el + el, max_num, el):
                arr[multiple] = 0
    simple_arr = [el for el in arr if el != 0]
    return simple_arr[num-1]


number1 = 100
number2 = 1000

print(f"Функция simple 100: {timeit('simple(number1)', 'from __main__ import simple, number1', number=1000)}")
print(f"Функция simple_er 100: {timeit('simple_er(number1)', 'from __main__ import simple_er, number1', number=1000)}")
print(f"Функция simple 1000: {timeit('simple(number2)', 'from __main__ import simple, number2', number=1000)}")
print(f"Функция simple_er 1000: {timeit('simple_er(number2)', 'from __main__ import simple_er, number2', number=1000)}")

# По результатам замеров алгоритм с решетом заметно выйгрывает на на больших числах.
# Но при этом он ограничен (в данном случае  замеры были сделаны при max_num = 10000),
# что не всегда удобно: нужно либо отслеживать как-то, чтобы запрашиваемый элемент
# попадал в диапазон рассматриваемых чисел, и расширять его по необходимости,
# либо ограничивать пользователя.
# На больших простых числах в заранее известном диапазоне лучше алгоритм с решетом Эратосфена.
# На малых числах алгоритм без решета быстрее.
"""
Функция simple 100: 1.6866692360000002
Функция simple_er 100: 1.9815407189999998
Функция simple 1000: 315.06458363499996
Функция simple_er 1000: 2.099473922999948
"""