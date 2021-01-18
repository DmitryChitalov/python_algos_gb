"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile


# Python 3.8.4
# Win10 x64

@profile
def eratosfen(n):
    """Адаптированное решето под условие задачи, что на ввод получаем
    порядковый номер простого числа
    Сложность - O(n**2)
    """
    simples = [2]
    next_num = simples[0] + 1
    while len(simples) < n:
        for i in simples:
            if next_num % i == 0:
                next_num += 1
                break
        else:
            simples.append(next_num)
            next_num += 1
    return simples[-1]


@profile
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


simple(20)
eratosfen(20)


# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     37     18.9 MiB     18.9 MiB           1   @profile
#     38                                         def simple(i):
#     39                                             """Без использования «Решета Эратосфена»"""
#     40     18.9 MiB      0.0 MiB           1       count = 1
#     41     18.9 MiB      0.0 MiB           1       n = 2
#     42     18.9 MiB      0.0 MiB          70       while count <= i:
#     43     18.9 MiB      0.0 MiB          70           t = 1
#     44     18.9 MiB      0.0 MiB          70           is_simple = True
#     45     18.9 MiB      0.0 MiB         787           while t <= n:
#     46     18.9 MiB      0.0 MiB         767               if n % t == 0 and t != 1 and t != n:
#     47     18.9 MiB      0.0 MiB          50                   is_simple = False
#     48     18.9 MiB      0.0 MiB          50                   break
#     49     18.9 MiB      0.0 MiB         717               t += 1
#     50     18.9 MiB      0.0 MiB          70           if is_simple:
#     51     18.9 MiB      0.0 MiB          20               if count == i:
#     52     18.9 MiB      0.0 MiB           1                   break
#     53     18.9 MiB      0.0 MiB          19               count += 1
#     54     18.9 MiB      0.0 MiB          69           n += 1
#     55     18.9 MiB      0.0 MiB           1       return n
#

#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     19     18.9 MiB     18.9 MiB           1   @profile
#     20                                         def eratosfen(n):
#     21                                             """Адаптированное решето под условие задачи, что на ввод получаем
#     22                                             порядковый номер простого числа
#     23                                             Сложность - O(n**2)
#     24                                             """
#     25     18.9 MiB      0.0 MiB           1       simples = [2]
#     26     18.9 MiB      0.0 MiB           1       next_num = simples[0] + 1
#     27     18.9 MiB      0.0 MiB          70       while len(simples) < n:
#     28     18.9 MiB      0.0 MiB         281           for i in simples:
#     29     18.9 MiB      0.0 MiB         262               if next_num % i == 0:
#     30     18.9 MiB      0.0 MiB          50                   next_num += 1
#     31     18.9 MiB      0.0 MiB          50                   break
#     32                                                 else:
#     33     18.9 MiB      0.0 MiB          19               simples.append(next_num)
#     34     18.9 MiB      0.0 MiB          19               next_num += 1
#     35     18.9 MiB      0.0 MiB           1       return simples[-1]
# Одинаковы по памяти, но большая разница по количеству вызовов внутри функций
# более чем в 4 раза

def find_sum(number, start=1):
    if number == 1:
        return start
    else:
        return start + find_sum(number - 1, start / -2)


@profile
def find_sum_1(number):
    find_sum(number, start=1)
    return


find_sum_1(30)


def reverse_number(number):
    if number // 10 == 0:
        return str(number)
    else:
        return str(number % 10) + (reverse_number(number // 10))


@profile
def reverse_number_1(number):
    reverse_number(number)
    return


reverse_number_1(12423534457567576456)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    117     18.9 MiB     18.9 MiB           1   @profile
#    118                                         def find_sum_1(number):
#    119     18.9 MiB      0.0 MiB           1       find_sum(number, start=1)
#    120     18.9 MiB      0.0 MiB           1       return
#
#
# Filename: D:/Study/Python algorythm/python_algos_gb/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    133     18.9 MiB     18.9 MiB           1   @profile
#    134                                         def reverse_number_1(number):
#    135     18.9 MiB      0.0 MiB           1       reverse_number(number)
#    136     18.9 MiB      0.0 MiB           1       return
# На всех алгоритмах получаю данные без изменений по памяти...
# до этого подставлял функции из других ДЗ, результат одинаковый

"""Write a method that takes an array of consecutive (increasing) letters as
input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter
be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!)
"""


@profile
def find_missing_letter_v1(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    try:
        start = alphabet.index(chars[0])
    except ValueError:
        alphabet = alphabet.upper()
        start = alphabet.index(chars[0])
    chars = ''.join(chars)
    for letter in chars:
        if letter == alphabet[start]:
            start += 1
            continue
        else:
            return alphabet[start]


@profile
def find_missing_letter_v2(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n + 1]) - 1:
        n += 1
    return chr(1 + ord(chars[n]))


find_missing_letter_v1(["a", "b", "c", "d", "f"])
find_missing_letter_v1(['O', 'Q', 'R', 'S'])
find_missing_letter_v2(["a", "b", "c", "d", "f"])
find_missing_letter_v2(['O', 'Q', 'R', 'S'])


# Нет затрат по памяти

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    199     18.8 MiB     18.8 MiB           1   @profile
#    200                                         def find_missing_letter_v2(chars):
#    201     18.8 MiB      0.0 MiB           1       n = 0
#    202     18.8 MiB      0.0 MiB           1       while ord(chars[n]) == ord(chars[n + 1]) - 1:
#    203                                                 n += 1
#    204     18.8 MiB      0.0 MiB           1       return chr(1 + ord(chars[n]))
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    182     18.8 MiB     18.8 MiB           1   @profile
#    183                                         def find_missing_letter_v1(chars):
#    184     18.8 MiB      0.0 MiB           1       alphabet = 'abcdefghijklmnopqrstuvwxyz'
#    185     18.8 MiB      0.0 MiB           1       try:
#    186     18.8 MiB      0.0 MiB           1           start = alphabet.index(chars[0])
#    187     18.8 MiB      0.0 MiB           1       except ValueError:
#    188     18.8 MiB      0.0 MiB           1           alphabet = alphabet.upper()
#    189     18.8 MiB      0.0 MiB           1           start = alphabet.index(chars[0])
#    190     18.8 MiB      0.0 MiB           1       chars = ''.join(chars)
#    191     18.8 MiB      0.0 MiB           2       for letter in chars:
#    192     18.8 MiB      0.0 MiB           2           if letter == alphabet[start]:
#    193     18.8 MiB      0.0 MiB           1               start += 1
#    194     18.8 MiB      0.0 MiB           1               continue
#    195                                                 else:
#    196     18.8 MiB      0.0 MiB           1               return alphabet[start]

def my_factorial(n):
    new_list = [1] + [0] * n
    for i in range(1, n + 1):
        new_list[i] = new_list[i - 1] * i
    return new_list[n]


@profile
def factorial(n):
    return my_factorial(n)


n = 900
factorial(n)

def my_generator(n):
    for i in range(1, n):
        yield my_factorial(i)

@profile
def custom_generator(n):
    iter_gen = my_generator(n + 1)
    for i in range(n - 1):
        next(iter_gen)
    return next(iter_gen)

custom_generator(n)
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    247     18.9 MiB     18.9 MiB           1   @profile
#    248                                         def factorial(n):
#    249     20.0 MiB      1.1 MiB           1       return my_factorial(n)
#
#
# Filename: D:/Study/Python algorythm/python_algos_gb/Урок 6. Практическое задание/task_1.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    259     20.0 MiB     20.0 MiB           1   @profile
#    260                                         def custom_generator(n):
#    261     20.0 MiB      0.0 MiB           1       iter_gen = my_generator(n + 1)
#    262     20.2 MiB     -9.9 MiB         900       for i in range(n - 1):
#    263     20.2 MiB     -9.6 MiB         899           next(iter_gen)
#    264     20.2 MiB      0.0 MiB           1       return next(iter_gen)
# Расчет факториала через рекурсию и генератор. Если у рекурсии память идет +,
# то в генераторе стоит -. Пытался разобраться как достучаться до нужного
# результата через генератор, не нашел ничего кроме next, for, или send().
# Но это все не подходит, приходится делать много итераций для достижения
# результата, проще выполнить обычную функцию. А примеров для работы с большими
# потоками данных, где генераторы показывают свою эффективность, у меня нет.