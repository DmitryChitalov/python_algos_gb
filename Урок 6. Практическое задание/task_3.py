"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


@profile
def revert_num(number, new_n):
    lst = list(range(100000))
    new_n = new_n * 10 + number % 10
    if number < 10:
        return new_n
    return revert_num(number // 10, new_n)


'''
Filename: /home/katrin/Geekbrains/ALGO Python/Урок 6. Практическое задание/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     28.6 MiB     28.6 MiB           1   @profile
    12                                         def revert_num(number, new_n):
    13     32.4 MiB      3.9 MiB           1       lst = list(range(100000))
    14     32.4 MiB      0.0 MiB           1       new_n = new_n * 10 + number % 10
    15     32.4 MiB      0.0 MiB           1       if number < 10:
    16     32.4 MiB      0.0 MiB           1           return new_n
    17                                             return revert_num(number // 10, new_n)


Filename: /home/katrin/Geekbrains/ALGO Python/Урок 6. Практическое задание/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     28.6 MiB     24.7 MiB           2   @profile
    12                                         def revert_num(number, new_n):
    13     32.4 MiB      7.7 MiB           2       lst = list(range(100000))
    14     32.4 MiB      0.0 MiB           2       new_n = new_n * 10 + number % 10
    15     32.4 MiB      0.0 MiB           2       if number < 10:
    16     32.4 MiB      0.0 MiB           1           return new_n
    17     28.8 MiB     -3.6 MiB           1       return revert_num(number // 10, new_n)


Filename: /home/katrin/Geekbrains/ALGO Python/Урок 6. Практическое задание/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     28.6 MiB     20.8 MiB           3   @profile
    12                                         def revert_num(number, new_n):
    13     32.4 MiB     11.6 MiB           3       lst = list(range(100000))
    14     32.4 MiB      0.0 MiB           3       new_n = new_n * 10 + number % 10
    15     32.4 MiB      0.0 MiB           3       if number < 10:
    16     32.4 MiB      0.0 MiB           1           return new_n
    17     28.8 MiB     -7.1 MiB           2       return revert_num(number // 10, new_n)


Filename: /home/katrin/Geekbrains/ALGO Python/Урок 6. Практическое задание/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     28.6 MiB     17.0 MiB           4   @profile
    12                                         def revert_num(number, new_n):
    13     32.4 MiB     15.5 MiB           4       lst = list(range(100000))
    14     32.4 MiB      0.0 MiB           4       new_n = new_n * 10 + number % 10
    15     32.4 MiB      0.0 MiB           4       if number < 10:
    16     32.4 MiB      0.0 MiB           1           return new_n
    17     28.8 MiB    -14.4 MiB           3       return revert_num(number // 10, new_n)
'''


@profile
def rev(num):
    def revert_num1(number, new_n):
        lst = list(range(100000))
        new_n = new_n * 10 + number % 10
        if number < 10:
            return new_n
        return revert_num1(number // 10, new_n)
    return revert_num1(num, 0)


'''
Filename: /home/katrin/Geekbrains/ALGO Python/Урок 6. Практическое задание/task_3.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22     18.0 MiB     18.0 MiB           1   @profile
    23                                         def rev(num):
    24     28.6 MiB      0.0 MiB           5       def revert_num1(number, new_n):
    25     32.5 MiB     14.4 MiB           4           lst = list(range(100000))
    26     32.5 MiB      0.0 MiB           4           new_n = new_n * 10 + number % 10
    27     32.5 MiB      0.0 MiB           4           if number < 10:
    28     32.5 MiB      0.0 MiB           1               return new_n
    29     29.6 MiB    -14.9 MiB           3           return revert_num1(number // 10, new_n)
    30     18.4 MiB    -11.2 MiB           1       return revert_num1(num, 0)
'''

print(revert_num(1234, 0))
print(rev(4321))

# При профилировании рекурсивной функции, статистика выводится отдельно на каждый вызов, что может быть
# крайне неудобно при большой глубине рекурсии, ненаглядно. Чтобы этого избежать, можно обернуть рекурсивную
# функцию в другую функцию и профилировать уже её. Таким образом выведется одна общая статистика.