"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""


from memory_profiler import profile

@profile
def rec_numbers_count(number, even_count=0, uneven_count=0):
    if number == 0:
        return print(f'Количество четных и нечетных цифр в числе равно: ({even_count}, {uneven_count})')

    else:
        if number % 2 == 0:
            even_count += 1
        else:
            uneven_count += 1
        rec_numbers_count(number//10, even_count, uneven_count)


@profile
def numbers_count(number):
    even_count, uneven_count = 0, 0
    for i in number:
        if i % 2 == 0:
            even_count += 1
        else:
            uneven_count += 1

    return print(f'Количество четных и нечетных цифр в числе равно: ({even_count}, {uneven_count})')


num = 123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789
num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

rec_numbers_count(num)
numbers_count(num2)

""" Касаемо памяти - рекурсия хранит стек вызовов, который увеличивается до базового случая.
    Касаемо @profile - метод срабатывает на каждую итерацию, что крайне неудобно для анализа, особенно если код большой

Количество четных и нечетных цифр в числе равно: (64, 80)

Line #    Mem usage    Increment   Line Contents
================================================
    10     13.1 MiB     13.0 MiB   @profile
    11                             def rec_numbers_count(number, even_count=0, uneven_count=0):
    12     13.1 MiB      0.0 MiB       if number == 0:
    13     13.1 MiB      0.0 MiB           return print(f'Количество четных и нечетных цифр в числе равно: ({even_count}, {uneven_count})')
    14                             
    15                                 else:
    16     13.0 MiB      0.0 MiB           if number % 2 == 0:
    17     13.0 MiB      0.0 MiB               even_count += 1
    18                                     else:
    19     13.0 MiB      0.0 MiB               uneven_count += 1
    20     13.1 MiB      0.1 MiB  <--      rec_numbers_count(number//10, even_count, uneven_count)


Количество четных и нечетных цифр в числе равно: (64, 80)

Line #    Mem usage    Increment   Line Contents
================================================
    23     13.1 MiB     13.1 MiB   @profile
    24                             def numbers_count(number):
    25     13.1 MiB      0.0 MiB       even_count, uneven_count = 0, 0
    26     13.1 MiB      0.0 MiB       for i in number:
    27     13.1 MiB      0.0 MiB           if i % 2 == 0:
    28     13.1 MiB      0.0 MiB               even_count += 1
    29                                     else:
    30     13.1 MiB      0.0 MiB               uneven_count += 1
    31                             
    32     13.1 MiB      0.0 MiB       return print(f'Количество четных и нечетных цифр в числе равно: ({even_count}, {uneven_count})')

"""
