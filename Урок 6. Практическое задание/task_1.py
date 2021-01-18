"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
"""Состав: 5 частей

1 "Программы вывода на 'экран' таблицы умножения"

"""

from memory_profiler import profile


@profile()
def pifagor():
    for i in range(1, 11):
        for j in range(1, 11):
            print("{:4}".format(i * j), end='')
        print()


@profile()
def pifagor_2():
    [print("{:4}".format(i * j), end='') if j != 11 else print() for i in range(1, 11) for j in range(1, 12)]


# pifagor()
# print()
# pifagor_2()

"""
pifagor()
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     4     16.1 MiB     16.1 MiB           1   @profile()
     5                                         def pifagor():
     6     16.1 MiB      0.0 MiB          11       for i in range(1, 11):
     7     16.1 MiB      0.0 MiB         110           for j in range(1, 11):
     8     16.1 MiB      0.0 MiB         100               print("{:4}".format(i * j), end='')
     9     16.1 MiB      0.0 MiB          10           print()

pifagor_2()
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     16.1 MiB     16.1 MiB           1   @profile()
    13                                         def pifagor_2():
    14     16.1 MiB      0.0 MiB         123       [print("{:4}".format(i * j), end='') if j != 11 else ...

Изменения в использовании памяти не заметны, т.к. работа кода минимальна
Хорошо заметна разница в количестве 'событий' 
"""

#######################################################################################
"""2
Использование декоратора @profile на функциях сложения 16-ти ричных чисел"""
from collections import deque
from memory_profiler import profile


@profile()
def standard(first, second, func='+'):  # подаются два 16-ричных числа в виде строк
    """Функция сложения, умножения двух 16-ричных цифр (для проверки результатов)"""
    if func == '+':
        result = hex(int(first, 16) + int(second, 16))
    elif func == '*':
        result = hex(int(first, 16) * int(second, 16))
    print('Эталон -> ', result)
    return result


def transform_16_1(elem):  # Подается строка
    """Функция преобразования 16-ричного объекта в 10-тичный"""
    n = 0
    elem = list(elem)
    for i in range(len(elem)):
        n += int(elem[i], 16) * (16 ** (len(elem) - i - 1))

    # n = sum(int(elem[i], 16) * (16 ** (len(elem) - i - 1)) for i in range(len(elem)))
    return n  # Десятичное число


def transform_16_2(elem, n=0):  # Подается объект deque
    """Функция преобразования 16-ричного объекта в 10-ричный. Рекурсия"""
    if len(elem) == 0:
        return n  # Десятичное число
    n = n + int(elem.popleft(), 16) * (16 ** (len(elem)))
    return transform_16_2(elem, n)


@profile()
def summation16(first, second):
    result = str(hex(transform_16_2(first) + transform_16_2(second)))[2:]
    return result


@profile()
def multiplication16(first, second):
    result = str(hex(transform_16_2(first) * transform_16_2(second)))[2:]
    return result


class Hex_number():
    def __init__(self, number):     # number -> 16-ичное число, строка
        self.number_16 = number
        self.numder_10 = sum(int(number[i], 16) * (16 ** (len(number) - i - 1)) for i in range(len(number)))

    def __add__(self, other):
        return Hex_number(str(hex(self.numder_10 + other.numder_10))[2:])

    def __mul__(self, other):
        return Hex_number(str(hex(self.numder_10 * other.numder_10))[2:])

    def __repr__(self):
        return self.number_16


@profile()
def checking_class():
    print("Проверка работы класса обработки 16-ричных чисел")
    # a, b = input("Введите 16-ричное число "), input("Введите второе 16-ричное число ")
    a, b = '4fd', 'ff'
    a16 = Hex_number(a)
    b16 = Hex_number(b)
    # a16 = Hex_number('4fd')
    # b16 = Hex_number('ff')
    print('Сумма чисел -', (a16 + b16), "-, произведение -", (a16 * b16))


# checking_class()
#
# a = '4fd'
# b = 'ff'
# a1 = deque(a)
# b1 = deque(b)
# standard(a, b)
# summation16(a1, b1)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    88     16.1 MiB     16.1 MiB           1   @profile()
    89                                         def checking_class():
    90     16.1 MiB      0.0 MiB           1       print("Проверка работы класса обработки 16-ричных чисел")
    91                                             # a, b = input("Введите 16-ричное число ")...
    92     16.1 MiB      0.0 MiB           1       a, b = '4fd', 'ff'
    93     16.1 MiB      0.0 MiB           1       a16 = Hex_number(a)
    94     16.1 MiB      0.0 MiB           1       b16 = Hex_number(b)
    95                                             # a16 = Hex_number('4fd')
    96                                             # b16 = Hex_number('ff')
    97     16.1 MiB      0.0 MiB           1       print('Сумма чисел -', (a16 + b16), "-, произведение -", (a16 * b16))


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     16.1 MiB     16.1 MiB           1   @profile()
     6                                         def standard(first, second, func='+'):  # подаются ...
     7                                             "Функция сложения, умножения двух 16-ричных цифр (...
     8     16.1 MiB      0.0 MiB           1       if func == '+':
     9     16.1 MiB      0.0 MiB           1           result = hex(int(first, 16) + int(second, 16))
    10                                             elif func == '*':
    11                                                 result = hex(int(first, 16) * int(second, 16))
    12     16.1 MiB      0.0 MiB           1       print('Эталон -> ', result)
    13     16.1 MiB      0.0 MiB           1       return result


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     16.1 MiB     16.1 MiB           1   @profile()
    36                                         def summation16(first, second):
    37     16.1 MiB      0.0 MiB           1       result = str(hex(transform_16_2(first) + transform_16_2(second)))[2:]
    38     16.1 MiB      0.0 MiB           1       return result

Использование памяти тремя функциями на одном уровне. 
Чрезмерное использование памяти не выявлено. 
Результат функций одинаковый и конечное использование памяти должно быть одинаковым. 
"""

####################################################################################
"""3 Использование собственного декоратора"""
import timeit
import memory_profiler
from operator import mul
from itertools import accumulate


def my_decor_1(f):
    def wrap(n):
        m1 = memory_profiler.memory_usage()
        t1 = timeit.default_timer()
        f(n)
        print(timeit.default_timer() - t1)
        m2 = memory_profiler.memory_usage()
        print(m2[0] - m1[0])
        print('******')
    return wrap


@my_decor_1
def fact_0(n=10):
    work_list = list()
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
        work_list.append(fact)
    return work_list


@my_decor_1
def fact_3(n=10):
    return list(accumulate(range(1, n + 1), func=mul))


def fact_1(n=10):
    fact = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        fact = fact * i
        yield fact


def fact_2(n=10):
    if n == 1:
        return 1
    return n * fact_2(n - 1)


@my_decor_1
def print_factorial_1(n=10):  # Функция вывода значений факториала на основе 'генератора'
    return [i for i in fact_1(n)]


@my_decor_1
def print_factorial_2(n=10):  # Функция вывода значений факториала на основе 'рекурсии'
    return [fact_2(i + 1) for i in range(n)]


"""Результаты ВРЕМЯ и занимаемая память указаны в комментариях к каждой функции"""
# fact_0(10000)               # 0.09      1.3
# fact_3(10000)               # 0.10      1.37
# print_factorial_1(10000)    # 0.1       1.28
# print_factorial_2(800)    # RecursionError
"""Отклонения в результатах измерений не значительны. Только рекурсия не стала работать по 
аргументу 10000
Еще один вывод: Запускать функции профилирования необходимо по отдельности, независимо от других исследуемых"""
###############################################################################################################
"""
4 Профилирование кода Функций поиска простого числа по его номеру по двум алгоритмам"""
from memory_profiler import profile
import numpy


@profile()
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


@profile()
def erat_1(n_user, n=200000):
    # Функция поиска простого числа по его номеру в воображаемом списке по алгоритму 'решето Эратосфена'
    a = list(range(n + 1))  # список заполняется значениями от 0 до n
    a[1] = 0    # Вторым элементом является единица, которую не считают простым числом забиваем ее нулем.
    k = 0       # Счетчик простых чисел
    i = 2       # начинаем с 3-го элемента

    while i <= n:
        if a[i] != 0:  # Если значение ячейки до этого не было обнулено, в этой ячейке содержится простое число.
            k += 1
            if n_user == k:
                break
            j = i + i       # первое кратное ему будет в два раза больше
            while j <= n:
                a[j] = 0    # это число составное, поэтому заменяем его нулем
                j = j + i   # переходим к следующему числу, которое кратно i (оно на i больше)
        i += 1

    return i


"""Здесь применим array() из NumPy"""
@profile()
def erat_2(n_user, n=200000):
    # Функция поиска простого числа по его номеру в воображаемом списке по алгоритму 'решето Эратосфена'
    # a = list(range(n + 1))  # список заполняется значениями от 0 до n
    a = numpy.array(list(range(n + 1)))
    a[1] = 0
    k, i = 0, 2

    while i <= n:
        if a[i] != 0:
            k += 1
            if n_user == k:
                break
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    del a

    return i


# simple(120)
# erat_1(120)
# erat_2(120)
"""
simple(120)
 6     24.5 MiB     24.5 MiB           1   @profile()
 7                                         def simple(i):
 8                                             "Без использования «Решета Эратосфена»"
 9     24.5 MiB      0.0 MiB           1       count = 1
 ...
24     24.5 MiB      0.0 MiB           1       return n
Использование памяти в роцессе работы simple почти не изменяется

erat_1(120)
28     24.4 MiB     24.4 MiB           1   @profile()
29                                         def erat_1(n_user, n=200000):
30                                             # Функция поиска ... алгоритму 'решето Эратосфена'
31     28.2 MiB      3.8 MiB           1       a = list(range(n + 1))  # список заполняется значениями от 0 до n
...
47     28.3 MiB      0.0 MiB           1       return i

Код работает быстрее, использует больше памяти
Строка 28 добавляет к используемой памяти 3.8 MiB, после изменения не значительны
---------------------------------------------------------------------------------
Следственно для уменьшения использования памяти надо менять код в строке 28
Используем NumPy.array и удалим в завершении оставшийся массив: функция erat_2

erat_2(120)
50     24.4 MiB     24.4 MiB           1   @profile()
51                                         def erat_2(n_user, n=200000):
52                                             # Функция поиска ... алгоритму 'решето Эратосфена'
53                                             # a = list(range(n + 1))  # список заполняется значениями от 0 до n
54     25.2 MiB      0.9 MiB           1       a = numpy.array(list(range(n + 1)))
...
67     25.3 MiB      0.0 MiB         657           i += 1
68     24.5 MiB     -0.8 MiB           1       del a
69                                         
70     24.5 MiB      0.0 MiB           1       return i
------------------------------ВЫВОД-----------------------------------------
Использование array в 3 раза уменьшило размер памяти для рабочего массива,
del удалила его остатки. В данном 'учебном' случае del как действие влияющее на 
изменения в памяти.
Применение array позволило увеличить размер исходного массива 
"""
###############################################################################

"""
5 Применю мой декоратор (@my_decor_1) к функциям поиска простого числа"""
@my_decor_1
def erat_10(n_user, n=200000):
    # Функция поиска простого числа по его номеру в воображаемом списке по алгоритму 'решето Эратосфена'
    a = list(range(n + 1))  # список заполняется значениями от 0 до n
    a[1] = 0    # Вторым элементом является единица, которую не считают простым числом забиваем ее нулем.
    k = 0       # Счетчик простых чисел
    i = 2       # начинаем с 3-го элемента

    while i <= n:
        if a[i] != 0:  # Если значение ячейки до этого не было обнулено, в этой ячейке содержится простое число.
            k += 1
            if n_user == k:
                break
            j = i + i       # первое кратное ему будет в два раза больше
            while j <= n:
                a[j] = 0    # это число составное, поэтому заменяем его нулем
                j = j + i   # переходим к следующему числу, которое кратно i (оно на i больше)
        i += 1

    return i


@my_decor_1
def simple_1(i):
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


@my_decor_1
def erat_20(n_user, n=200000):
    # Функция поиска простого числа по его номеру в воображаемом списке по алгоритму 'решето Эратосфена'
    # a = list(range(n + 1))  # список заполняется значениями от 0 до n
    a = numpy.array(list(range(n + 1)))
    a[1] = 0
    k, i = 0, 2

    while i <= n:
        if a[i] != 0:
            k += 1
            if n_user == k:
                break
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    del a

    return i


# simple_1(1000)      # 0.7192769     Время
#                     # 0.00390625    Память
# erat_10(1000)           # 0.10128499999999985
#                         # 0.00390625
# erat_20(1000)       # 0.14310599999999996 Время несколько увеличилось
                    # 0.00390625
"""Применение оптимизации для использования памяти несколько увеличило время посика
По сранению с simple_1 незначительно
Итог чуть проиграли по времени. Выиграли по использованию памяти и функциональности (размер начального массива) 
"""