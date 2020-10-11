"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки) оптимизации и
доказать (наглядно, кодом) их эффективность
"""

from timeit import timeit


def conc(str1, str2, str3):
    return 'str1: ' + str1 + ' str2: ' + str2 + ' str3: ' + str3


def percent(str1, str2, str3):
    return 'str1: %s str2: %s str3: %s' % (str1, str2, str3)


def format(str1, str2, str3):
    return 'str1: {} str2: {} str3: {}'.format(str1, str2, str3)


def format2(str1, str2, str3):
    return 'str1: {0} str2: {1} str3: {2}'.format(str1, str2, str3)


def join(str1, str2, str3):
    return "".join(['str1: ', str1, 'str2: ', str2, 'str3: ', str3])


def fstring(str1, str2, str3):
    return f'str1: {str1} str2: {str2} str3: {str3}'


str1 = 'abc'
str2 = 'def'
str3 = 'ghi'

print(f'conc: {timeit("conc(str1, str2, str3)", setup="from __main__ import conc, str1, str2, str3", number=100_000)}')  # -> 0.07
print(f'percent: {timeit("percent(str1, str2, str3)", setup="from __main__ import percent, str1, str2, str3", number=100_000)}')  # -> 0.06
print(f'format: {timeit("format(str1, str2, str3)", setup="from __main__ import format, str1, str2, str3", number=100_000)}')  # -> 0.09
print(f'format2: {timeit("format2(str1, str2, str3)", setup="from __main__ import format2, str1, str2, str3", number=100_000)}')  # -> 0.11
print(f'join: {timeit("join(str1, str2, str3)", setup="from __main__ import join, str1, str2, str3", number=100_000)}')  # -> 0.06
print(f'fstring: {timeit("fstring(str1, str2, str3)", setup="from __main__ import fstring, str1, str2, str3", number=100_000)}')  # -> 0.04
print('')

""" самый банальный пример - f-строки. Приемущества: 

    1. удобство написания относительно знаков препинания и пробелов
    2. краткость записи
    3. скорость:
        сonc: 0.071766686
        percent: 0.060387205
        format: 0.09108891800000002
        format2: 0.11187386500000002
        join: 0.062946
        fstring: 0.04868191099999997 <--    
"""


def zipit(keys, vals):
    return dict(zip(keys, vals))


def mkdict(keys, vals):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = vals[i]
    return result


keys = ['a', 'b', 'c']
vals = [1, 2, 3]

print(f'zipit: {timeit("zipit(keys, vals)", setup="from __main__ import zipit, keys, vals", number=100_000)}')  # -> 0.08
print(f'mkdict: {timeit("mkdict(keys, vals)", setup="from __main__ import mkdict, keys, vals", number=100_000)}')  # -> 0.12
print('')

""" самый первый пункт оптимизации - использовать внутренние функции, которые максимально оптимизированы.
    на примери функции Zip
    
    zipit: 0.08553044700000001
    mkdict: 0.12254074100000001
"""


def sub_def1(i):
    global x
    x = x + i


def my_def1(test_list):
    for i in test_list:
        sub_def1(i)


def my_def2(test_list):
    global x
    for i in test_list:
        x = x + i


x = 0
my_list = range(100000)

print(f'my_def1: {timeit("my_def1(my_list)", setup="from __main__ import my_def1, my_list", number=1)}')  # -> 0.033
print(f'my_def2: {timeit("my_def2(my_list)", setup="from __main__ import my_def2, my_list", number=1)}')  # -> 0.016

""" По возможности функии должны сами заниматься агригацией данных, т.к. сам вызов функций также занимает время
    my_def1: 0.03362102099999997
    my_def2: 0.01615237700000005
"""