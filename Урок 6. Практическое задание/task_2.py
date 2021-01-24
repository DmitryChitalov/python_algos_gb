"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import profile


@profile
def add_string_with_plus(iters):
    s = ""
    for i in range(iters):
        s += "xyz"

@profile
def add_string_with_format(iters):
    fs = "{}"*iters
    s = fs.format(*(["xyz"]*iters))

@profile
def add_string_with_join(iters):
    l = []
    for i in range(iters):
        l.append("xyz")
    s = "".join(l)



add_string_with_join(60000)
add_string_with_plus(60000)
add_string_with_format(60000)

'''
нашел на зарубежном форуме  о сложении строк разными методами и потреблением памяти этими методами
"""
Don't use + for generating long strings — In Python, str is immutable, so the left and right strings have to be copied 
into the new string for every pair of concatenations. If you concatenate four strings of length 10, you'll be copying 
(10+10) + ((10+10)+10) + (((10+10)+10)+10) = 90 characters instead of just 40 characters. Things get quadratically worse
 as the number and size of the string increases. Java optimizes this case by transforming the series of concatenations 
 to use StringBuilder some of the time , but CPython doesn't.
Therefore, it's advised to use .format or % syntax (however, they are slightly slower than + for short strings). 
Or better, if already you've contents available in the form of an iterable object, then use ''.join(iterable_object) 
which is much faster.
"""
Подразумевается что .join  при увеличении складываемых элементов в строку будет потреблять меньше памяти и работать быстрее
попробовал проверить, в результате не очень получилось это увидеть...
Filename: E:/gb/gbtasks/python_algos_gb/Урок 6. Практическое задание/gfdhjd.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    16     18.7 MiB     18.7 MiB           1   @profile
    17                                         def add_string_with_join(iters):
    18     18.7 MiB      0.0 MiB           1       l = []
    19     19.7 MiB      0.0 MiB       60001       for i in range(iters):
    20     19.7 MiB      1.0 MiB       60000           l.append("xyz")
    21     19.7 MiB      0.0 MiB           1       s = "".join(l)


Filename: E:/gb/gbtasks/python_algos_gb/Урок 6. Практическое задание/gfdhjd.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     18.7 MiB     18.7 MiB           1   @profile
     6                                         def add_string_with_plus(iters):
     7     18.7 MiB      0.0 MiB           1       s = ""
     8     19.6 MiB      0.0 MiB       60001       for i in range(iters):
     9     19.6 MiB      0.9 MiB       60000           s += "xyz"


Filename: E:/gb/gbtasks/python_algos_gb/Урок 6. Практическое задание/gfdhjd.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     19.0 MiB     19.0 MiB           1   @profile
    12                                         def add_string_with_format(iters):
    13     19.1 MiB      0.1 MiB           1       fs = "{}"*iters
    14     19.3 MiB      0.2 MiB           1       s = fs.format(*(["xyz"]*iters))



Process finished with exit code 0

'''