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
import memory_profiler
from functools import reduce


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper

# №1
#  Реализовать формирование списка, используя функцию range() и возможности генератора!!!(спискового включения).
#  В список должны войти четные числа от 1 до 1000 (включая границы).
#  Необходимо получить результат вычисления произведения всех элементов списка.


@decor
def numbers(list):
    my_list = [number for number in range(1, 100000) if number % 2 == 0]
    print(reduce(lambda el, next_el: el * next_el, my_list))
    return my_list


res, mem_diff = numbers(range(100))
print(f"Выполнение заняло {mem_diff} Mib")


@decor
def real_generator(numbers):
    for num in range(1, 100000):
        if num % 2 == 0:
            yield reduce(lambda el, next_el: el * next_el, numbers)


generator, mem_diff = real_generator(range(100))
print(f"Выполнение через генератор заняло {mem_diff} Mib")

# Выводы
# Пример с ленивыми вычислениями
# Генераторы не возвращают любое количество элементов сразу вместе, как списки, они возвращают элементы один за другим.
#
# для наглядности эксперимента for num in range(1, 100000):
# Выполнение заняло 1.328125 Mib
# Выполнение через генератор заняло 0.0 Mib

# №2
# Программа принимает действительное положительное число x и целое отрицательное число y.
#  Необходимо выполнить возведение числа x в степень y.
#   Задание необходимо реализовать в виде функции my_func(x, y).
#   При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
#  Первый — возведение в степень с помощью оператора **.+
#   Второй — более сложная реализация без оператора **, предусматривающая использование цикла.+


@profile
def my_func():
    # returns the result of raising to a negative power
    global x, y
    x = float(input('enter float: '))
    y = int(input('enter negative integer: '))
    return x ** y


@profile
def my_func_2():
    global x, y
    result = 1
    x = float(input('enter float: '))
    y = int(input('enter negative integer: '))
    for i in range(abs(y)):
        result *= x
    return 1 / result


print(my_func())
print(my_func_2())

# enter float: 0.2
# enter negative integer: -10

#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     78     24.7 MiB     24.7 MiB           1   @profile
#     79                                         def my_func():
#     80                                             """returns the result of raising to a negative power"""
#     81                                             global x, y
#     82     24.7 MiB      0.0 MiB           1       x = float(input('enter float: '))
#     83     24.7 MiB      0.0 MiB           1       y = int(input('enter negative integer: '))
#     84     24.7 MiB      0.0 MiB           1       return x ** y
#
#
# 9765624.999999994

# enter float: 0.2
# enter negative integer: -300

#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     87     24.7 MiB     24.7 MiB           1   @profile
#     88                                         def my_func_2():
#     89                                             global x, y
#     90     24.7 MiB      0.0 MiB           1       result = 1
#     91     24.7 MiB      0.0 MiB           1       x = float(input('enter float: '))
#     92     24.7 MiB      0.0 MiB           1       y = int(input('enter negative integer: '))
#     93     24.7 MiB      0.0 MiB         301       for i in range(abs(y)):
#     94     24.7 MiB      0.0 MiB         300           result *= x
#     95     24.7 MiB      0.0 MiB           1       return 1 / result
#
#
# 4.909093465297644e+209
#
# Выводы: даже при больших приращениях аргументов основную память этой задачи занимает импортированный @profile,
# остальные вычисления происходят с константами, пусть и большого порядка

# №3
# Приведен код, который позволяет сохранить в
# массиве индексы четных элементов другого массива


@decor
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@decor
def func_2(nums):
    new_arr = [i for i in nums if not i % 2]
    return new_arr


nums1 = range(10000)
nums2 = [i for i in range(10000)]

print(func_1(nums1))
print(func_1(nums2))
print(func_2(nums1))
print(func_2(nums2))


# в плане времени выполнения выигрывает функция 2, заполнение массива через списковое включение,
# однако на память метод построения списка не влияет.

# 0.7578125 MiB
# 0.625 MiB
# 0.625 MiB
# 0.0 MiB

# По моему мнению, такие значения получились оттого, что результат выполнения сохранялся в памяти,
# то есть создавалась ссылка на хранение результатов вычислений,
# из-за чего дополнительное место в памяти не резервировалось.

# Python 3.8
# Win 10, x-64, Intel i7, 8GB
