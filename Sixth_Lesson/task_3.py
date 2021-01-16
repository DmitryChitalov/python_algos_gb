"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import  profile

def wrapper(numb: int, even_count=0, odd_count=0):
    if numb < 10:
        if numb % 2:
            return f"Количество четных и нечетных цифр в числе равно: ({even_count}, {odd_count + 1})"
        else:
            return f"Количество четных и нечетных цифр в числе равно: ({even_count + 1}, {odd_count})"
    else:
        remainder = numb % 10  # вычисляем остаток
        numb //= 10
        if remainder % 2:
            return wrapper(numb, even_count, odd_count + 1)
        else:
            return wrapper(numb, even_count + 1, odd_count)

@profile
def even_or_odd_numbers(number: int):
    print(wrapper(number))

even_or_odd_numbers(34563)
"""Вывод программы:
Количество четных и нечетных цифр в числе равно: (2, 3)
Filename: E:/python_algos_gb/Sixth_Lesson/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    24     18.4 MiB     18.4 MiB           1   @profile
    25                                         def even_or_odd_numbers(number: int):
    26     18.4 MiB      0.0 MiB           1       print(wrapper(number))
 
Вывод: Чтобы таблица используемой памяти не вызывалась для каждого вызова при рекурсии,
то можно вызвать рекурсивную функцию в другой функции, и уже для это ДРУГОЙ функции использовать
декоратор @profile, который выведет 1 раз таблицу используемой памяти
"""