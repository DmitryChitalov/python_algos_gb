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
import sys
from memory_profiler import profile
import timeit

print(sys.version)  # 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]

# пример номер 1: Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива. Н
print('замеры задачи 1: ')


@profile()
def work_with_indexes():
    array = [i for i in range(10000)]
    res = []
    if len(array) == 0:
        return 0
    for i in range(len(array)):
        if i % 2 == 0:
            res.append(array[i])
    return sum(res) * array[-1]


def work_with_indexes_time():
    array = [i for i in range(10000)]
    res = []
    if len(array) == 0:
        return 0
    for i in range(len(array)):
        if i % 2 == 0:
            res.append(array[i])
    return sum(res) * array[-1]


@profile()
def work_with_indexes_2():
    array = [i for i in range(10000)]
    return sum(array[0::2]) * array[-1] if 0 < len(array) else 0


def work_with_indexes_2_time():
    array = [i for i in range(10000)]
    return sum(array[0::2]) * array[-1] if 0 < len(array) else 0


@profile()
def work_with_indexes_3():
    array = [i for i in range(10000)]
    if len(array) > 0:
        return sum([array[n] for n in range(0, len(array), 2)]) * array[-1]
    else:
        return 0


def work_with_indexes_3_time():
    array = [i for i in range(10000)]
    if len(array) > 0:
        return sum([array[n] for n in range(0, len(array), 2)]) * array[-1]
    else:
        return 0


print(timeit.timeit("work_with_indexes_time()", setup="from __main__ import work_with_indexes_time", number=1000))
print(timeit.timeit("work_with_indexes_2_time()", setup="from __main__ import work_with_indexes_2_time", number=1000))
print(timeit.timeit("work_with_indexes_3_time()", setup="from __main__ import work_with_indexes_3_time", number=1000))

work_with_indexes()
work_with_indexes_2()
work_with_indexes_3()
print(100 * '*')

# вывод из примера 1 : по затратам памяти все три примера работаю одинакого( памяти не расходуют),
# но если смотреть на время, то второй пример самый эффективный, в то время как первый в 1000 раз медленней
# потому что он использует создание новго списка. Второй и третий пример используют генераторные выражения
# второй вариант быстрее, потому исп срез, в то время как 3ий вариант перебирает элементы исх. списка


# пример номер 2 : Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом.
# Если число является частью слова, то его суммировать не нужно.
print('замеры задачи 2: ')


@profile()
def sum_numbers():
    text = 'This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year'
    new_l = []
    l = text.split()
    for el in l:
        try:
            new_l.append(int(el))
        except ValueError:
            new_l.append(0)
    return sum(new_l)


def sum_numbers_time_check():
    text = 'This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year'
    new_l = []
    l = text.split()
    for el in l:
        try:
            new_l.append(int(el))
        except ValueError:
            new_l.append(0)
    return sum(new_l)


@profile()
def sum_numbers_2():
    text = 'This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year'
    return sum(int(word) for word in text.split() if word.isdigit())


def sum_numbers_2_time():
    text = 'This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year'
    return sum(int(word) for word in text.split() if word.isdigit())


@profile()
def sum_numbers_3():
    import re
    text = 'This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year'
    line = re.findall(r'\b\d+\b', text)
    sum = 0
    if len(line) > 0:
        for i in line:
            sum = sum + int(i)
        return sum
    else:
        return 0


def sum_numbers_3_time_check():
    import re
    text = 'This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year'
    line = re.findall(r'\b\d+\b', text)
    sum = 0
    if len(line) > 0:
        for i in line:
            sum = sum + int(i)
        return sum
    else:
        return 0


print(timeit.timeit("sum_numbers_time_check()", setup="from __main__ import sum_numbers_time_check", number=1000))
print(timeit.timeit("sum_numbers_2_time()", setup="from __main__ import sum_numbers_2_time", number=1000))
print(timeit.timeit("sum_numbers_3_time_check()", setup="from __main__ import sum_numbers_3_time_check", number=1000))
sum_numbers()
sum_numbers_2()
sum_numbers_3()
print(100 * '*')

# вывод: по памяти все три задачи не занимют много места, однако, если замерить по времени, то
# самый эффективый способ, это использование list comprehension, а самый медленный это создание нового списка чисел


# пример номер 3 : Вам дано положительное целое число. Определите сколько цифр оно имеет.
print('замеры задачи 3: ')


@profile()
def number_length():
    a = 100
    str_a = str(a)
    return len(str_a)


def number_length_time_check():
    a = 100
    str_a = str(a)
    return len(str_a)


@profile()
def number_length_2():
    a = 100
    import math
    return int(math.log10(a)) + 1 if a else 1


def number_length_2_time_check():
    a = 100
    import math
    return int(math.log10(a)) + 1 if a else 1


@profile()
def number_length_3():
    a = 100
    from itertools import count
    for i in count(1, 1):
        if a / 10 ** i < 1:
            return i


def number_length_3_time_check():
    a = 100
    from itertools import count
    for i in count(1, 1):
        if a / 10 ** i < 1:
            return i


def number_length_4():
    a = 100
    from itertools import count
    for i in count(1, 1):
        if a / 10 ** i < 1:
            yield i


print(timeit.timeit("number_length_time_check()", setup="from __main__ import number_length_time_check", number=1000))
print(
    timeit.timeit("number_length_2_time_check()", setup="from __main__ import number_length_2_time_check", number=1000))
print(timeit.timeit("number_length_3_time_check()", setup="from __main__ import number_length_3_time_check",
                    number=1000))

print(timeit.timeit("number_length_4()", setup="from __main__ import number_length_4",
                    number=1000))

number_length()
number_length_2()
number_length_3()

# вывод: самый быстрый выриант = это решение через преобразование в строку, так как используются встроенные функции
# не сильно отстает по времени решение через модуль math, самое медленное рещение это с помощью итерации,
# по памяти так же не занимею много места все 3 варианта.
# так же добавл четвертый вариант с исп yield и итерирования(генератор)
# и мы сразу получили из самой  медленной функции, самую быструю
