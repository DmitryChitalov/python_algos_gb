"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

"""
Модуль pickle предоставляет мощный алгоритм сериализации и десериализации структур данных Python.
Но имеется и cPickle (_pickle для Python 3), который является результатом работы по оптимизации первого (написан на C).
Он в некоторых случаях может быть быстрее оригинального pickle. Однако интерфейс
самих модулей почти не отличается. Этот модуль хорошо использовать в Python 2, однако в Python 3,
на сколько мне известно, он интегрирован.
"""

"""
Конкатенация строк идет медленно. Вместо этого лучше использовать метод join или функцию форматирования
для формирования унифицированной строки.
"""

from timeit import timeit


def make_str_1():
    symbs = 'abcdefghijklmnopqrstuvwxyz'
    my_string = ''
    for _ in range(10):
        my_string = my_string + symbs
    return my_string


def make_str_2():
    symbs = 'abcdefghijklmnopqrstuvwxyz'
    my_string = []
    for _ in range(10):
        my_string.append(symbs)
    return ''.join(my_string)


result_1 = timeit("make_str_1()", "from __main__ import make_str_1", number=1000000)
result_2 = timeit("make_str_2()", "from __main__ import make_str_2", number=1000000)

print(f'Результат выполнения make_str_1(): {result_1} сек.')
print(f'Результат выполнения make_str_2(): {result_2} сек.')
print(f'Функция make_str_1() выполняется быстрее make_str_2() на: {round(100 - result_1 / result_2 * 100, 1)}%')

"""
Результат выполнения make_str_1(): 0.764898222
Результат выполнения make_str_2(): 0.890023692
Функция make_str_1() выполняется быстрее make_str_2() на: 14.1%
"""
