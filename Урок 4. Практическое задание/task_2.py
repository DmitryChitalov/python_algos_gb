"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


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


def main():
    pass
    try:
        global num_100
        global num_1000
        global num_10000
        num_100 = randint(10000, 1000000)
        num_1000 = randint(1000000, 10000000)
        num_10000 = randint(100000000, 10000000000000)

        time_recursive_100 = timeit(
            "recursive_reverse(num_100)",
            setup='from __main__ import recursive_reverse, num_100',
            number=10000)

        time_recursive_1000 = timeit(
            "recursive_reverse(num_1000)",
            setup='from __main__ import recursive_reverse, num_1000',
            number=10000)
        time_recursive_10000 = timeit(
            "recursive_reverse(num_10000)",
            setup='from __main__ import recursive_reverse, num_10000',
            number=10000)

        mem_time_recursive_100 = timeit(
            'recursive_reverse_mem(num_100)',
            setup='from __main__ import recursive_reverse_mem, num_100',
            number=10000)

        mem_time_recursive_1000 = timeit(
            'recursive_reverse_mem(num_1000)',
            setup='from __main__ import recursive_reverse_mem, num_1000',
            number=10000)
        mem_time_recursive_10000 = timeit(
            'recursive_reverse_mem(num_10000)',
            setup='from __main__ import recursive_reverse_mem, num_10000',
            number=10000)

        print(f"""Не оптимизированная функция recursive_reverse:
100: {time_recursive_100} ms
1000: {time_recursive_1000} ms
10000: {time_recursive_10000} ms

Оптимизированная функция recursive_reverse_mem:
100: {mem_time_recursive_100} ms
1000: {mem_time_recursive_1000} ms
10000: {mem_time_recursive_10000} ms

Эффективность recursive_reverse_mem:
На 100 элементов recursive_reverse_mem в {time_recursive_100 / mem_time_recursive_100} раз эффективнее
На 1000 элементов recursive_reverse_mem в {time_recursive_1000 / mem_time_recursive_1000} раз эффективнее
На 10000 элементов recursive_reverse_mem в {time_recursive_10000 / mem_time_recursive_10000} раз эффективнее

Программа завершена!""")

    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()

"""
Не оптимизированная функция recursive_reverse:
100: 0.018494445997930598 ms
1000: 0.020004111000162084 ms
10000: 0.03676897099649068 ms

Оптимизированная функция recursive_reverse_mem:
100: 0.0015667580009903759 ms
1000: 0.0015920080004434567 ms
10000: 0.0016585630000918172 ms

Эффективность recursive_reverse_mem:
На 100 элементов recursive_reverse_mem в 11.804277358877329 раз эффективнее
На 1000 элементов recursive_reverse_mem в 12.565333211007673 раз эффективнее
На 10000 элементов recursive_reverse_mem в 22.169173552319187 раз эффективнее

Программа завершена!

Вывод:
RAM - самая быстрая память в ПК после кэша процессора. 
Мемоизация имеет смысл. Производительность выросла в разы! Более подробные результаты в третье таблице выше. 
Но нужно понимать, что оперативка не резиновая. При работе со встроенными типами данных - отличный паттерн! 
Но при работе с video, фото, звуком и друми большими фрагментами данных, нужно быть аккуратным!

"""
