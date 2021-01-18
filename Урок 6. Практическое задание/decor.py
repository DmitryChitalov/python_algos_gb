from memory_profiler import  memory_usage
from timeit import default_timer
from random import randint


def decor(func):
    def memory_prof(*args):
        m1 = memory_usage()
        t1 = default_timer()
        func(args[0])
        m2 = memory_usage()
        t2 = default_timer()
        return f'заняло памяти - {m2[0] - m1[0]}, заняло времени - {t2 - t1}'
    return memory_prof


@decor
def simple_num(s):
    n = s * 100
    simple_list = [el for el in range(n+1)]
    simple_list[1] = 0
    i = 2
    while i <= n:
        if simple_list[i] != 0:
            m = i * 2
            while m <= n:
                simple_list[m] = 0
                m += i
        i += 1
    simple_list = sorted(list(set(simple_list)))
    simple_list.remove(0)
    return simple_list[s-1]


@decor
def palindrome(word):
    reverse_word = word[::-1]
    if reverse_word == word:
        # del reverse_word
        return True
    else:
        # del reverse_word
        return False


@decor
def palindrome_2(word):
    i = 0
    j = -1
    while len(word)-1 != i:
        if word[i] == word[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


@decor
def even_num(num):
    num_list = [randint(0, 100) for i in range(num)]
    even = 0
    odd = 0
    for i in range(len(num_list)):
        if num_list.pop() % 2 == 0:
            even += 1
        else:
            odd += 1
    return f'Кол-во четных чисел в массиве - {even}, нечетных - {odd}'


print(f'Функция подсчета четных и нечетных чисел: {even_num(1000000)}')
print(f'Функция палиндром версия 1: {palindrome("шалаш"*10000000)}')
print(f'Функция палиндром версия 2: {palindrome_2("шалаш"*10000000)}')
print(f'Функция решето Эратосфена: {simple_num(5000)}')

"""
Функция подсчета четных и нечетных чисел: заняло памяти - 0.00390625, заняло времени - 1.4810056
Функция палиндром версия 1: заняло памяти - 0.0, заняло времени - 0.33347950000000015
Функция палиндром версия 2: заняло памяти - 0.03125, заняло времени - 28.845938699999998
Функция решето Эратосфена: заняло памяти - 0.0, заняло времени - 0.5756783999999975

Тут очень странный момент, почему то palindrome версии 1, не показывает выделения памяти
хотя через profiler показывает.
Windows 10/x64 
Python 3.8.3
"""