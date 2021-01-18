from memory_profiler import profile, memory_usage
from random import randint


# решето Эратосфена
@profile
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


#функция палиндром
@profile
def palindrome(word):
    reverse_word = word[::-1]
    if reverse_word == word:
        del reverse_word
        return True
    else:
        del reverse_word
        return False

# функция палиндром версия 2
@profile
def palindrome_2(word):
    i = 0
    j = -1
    while len(word)-1 != i:
        if word[i] == word[j]:
            i += 1
            j -= 1
            continue
        else:
            return False
    return True


# подсчет четных и нечетных чисел в массиве
@profile
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



print(even_num(1000000))
print(palindrome('шалаш'*1000000))
print(palindrome_2('шалаш'*1000000))
simple_num(500)

"""

1. Подсчет четных и нечетных чисел в массиве
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    58     16.0 MiB     16.0 MiB           1   @profile
    59                                         def even_num(num):
    60     19.9 MiB  -2774.6 MiB     1000003       num_list = [randint(0, 100) for i in range(num)]
    61     19.9 MiB      0.0 MiB           1       even = 0
    62     19.9 MiB      0.0 MiB           1       odd = 0
    63     19.9 MiB -1340787.7 MiB     1000001       for i in range(len(num_list)):
    64     19.9 MiB -1347847.5 MiB     1000000           if num_list.pop() % 2 == 0:
    65     19.9 MiB -677862.8 MiB      505473               even += 1
    66                                                 else:
    67     19.9 MiB -662924.9 MiB      494527               odd += 1
    68     16.0 MiB     -3.9 MiB           1       return f'Кол-во четных чисел в массиве - {even}, нечетных - {odd}'


Кол-во четных чисел в массиве - 505473, нечетных - 494527

Как мы видим основное выделение памяти идет при создании массива, но при получении результата, 
массив освобождает память, так как в нем не остается элементов


2. Функция палиндром версия 1

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33     25.6 MiB     25.6 MiB           1   @profile
    34                                         def palindrome(word):
    35     35.1 MiB      9.5 MiB           1       reverse_word = word[::-1]
    36     35.1 MiB      0.0 MiB           1       if reverse_word == word:
    37     25.6 MiB     -9.5 MiB           1           del reverse_word
    38     25.6 MiB      0.0 MiB           1           return True
    39                                             else:
    40                                                 del reverse_word
    41                                                 return False

True

В функцию подаем строку из большого кол-ва символов, память выделяется на создание перевернутой строки,
Память оптимизируется после сравнения строк.


3. Функция палиндром версия 2

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    44     25.6 MiB     25.6 MiB           1   @profile
    45                                         def palindrome_2(word):
    46     25.6 MiB      0.0 MiB           1       i = 0
    47     25.6 MiB      0.0 MiB           1       j = -1
    48     25.6 MiB -377295.4 MiB     5000000       while len(word)-1 != i:
    49     25.6 MiB -377295.3 MiB     4999999           if word[i] == word[j]:
    50     25.6 MiB -377295.4 MiB     4999999               i += 1
    51     25.6 MiB -377295.4 MiB     4999999               j -= 1
    52     25.6 MiB -377295.4 MiB     4999999               continue
    53                                                 else:
    54                                                     return False
    55     25.4 MiB     -0.1 MiB           1       return True

True

Как мы видим палиндром версии 2 совсем не занимает памяти, так как идет сравнение по 1 элементу.
!!! Немного не понятно почему освободилась память в конце

4. Решето Эратосфена

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    15     15.9 MiB     15.9 MiB           1   @profile
    16                                         def simple_num(s):
    17     15.9 MiB      0.0 MiB           1       n = s * 100
    18     16.9 MiB     -7.8 MiB       50004       simple_list = [el for el in range(n+1)]
    19     16.9 MiB      0.0 MiB           1       simple_list[1] = 0
    20     16.9 MiB      0.0 MiB           1       i = 2
    21     16.9 MiB      0.0 MiB       50000       while i <= n:
    22     16.9 MiB      0.0 MiB       49999           if simple_list[i] != 0:
    23     16.9 MiB      0.0 MiB        5133               m = i * 2
    24     16.9 MiB      0.0 MiB      129954               while m <= n:
    25     16.9 MiB      0.0 MiB      124821                   simple_list[m] = 0
    26     16.9 MiB      0.0 MiB      124821                   m += i
    27     16.9 MiB      0.0 MiB       49999           i += 1
    28     16.6 MiB     -0.3 MiB           1       simple_list = sorted(list(set(simple_list)))
    29     16.6 MiB      0.0 MiB           1       simple_list.remove(0)
    30     16.6 MiB      0.0 MiB           1       return simple_list[s-1]
    
Как мы видим, выделение памяи идет на создание массива,
Память частично освобождается, когда мы список превращаем в множество (все 0 удлаяются, кроме 1), 
тем самым освобождают память.
Windows 10/x64 
Python 3.8.3
"""