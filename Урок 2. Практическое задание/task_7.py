"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def natural_input():
    __natural = input('Введите натуральное число: ')
    try:
        __natural = int(__natural)
        assert __natural>0
        return __natural
    except ValueError:
        print('Вы ввели не число')
        return natural_input()
    except AssertionError:
        print('Вы ввели не натуральное число')
        return natural_input()

def sequnce_calc(n,sum=0):
    if(n>0):
        return sequnce_calc(n-1,sum+n)
    else:
        return sum

def assertion_seq_equal(n):
    __right_part = n*(n+1)/2
    __left_part = sequnce_calc(n)
    if(__left_part == __right_part):
        print(f'Выполняется равенство 1+2+...+n = n(n+1)/2 для натурального n={n} {__left_part} = {__right_part}')
    else:
        print('Что-то пошло не так')

assertion_seq_equal(natural_input())