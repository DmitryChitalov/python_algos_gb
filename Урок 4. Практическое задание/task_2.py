"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def recursive_reverse(number):
    if number < 10:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


n = 1234567890
print(recursive_reverse(n))
print(timeit.timeit('recursive_reverse(n)',
                    setup='from __main__ import recursive_reverse, n',
                    number=100000))

# 0.3832565870002327 без мемоизации
# 0.027926207999826147 с мемоизацией
# Вывод: в данном случае мемоизация нужна, т.к. значительно ускоряет работу функции
