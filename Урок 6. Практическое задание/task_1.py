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
from memory_profiler import profile, memory_usage
from random import randint


@profile()
def reverse_num(num):
    while num != 0:
        print(num % 10, end='')
        num //= 10
    return ''


'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     17.9 MiB     17.9 MiB           1   @profile()
    28                                         def reverse_num(num):
    29     17.9 MiB      0.0 MiB          37       while num != 0:
    30     17.9 MiB      0.0 MiB          36           print(num % 10, end='')
    31     17.9 MiB      0.0 MiB          36           num //= 10
    32     17.9 MiB      0.0 MiB           1       return ''
'''


@profile()
def new_reverse_num(num):
    def reverse_num2(n):
        if n < 10:
            return n
        else:
            print(n % 10, end='')
            return reverse_num2(n // 10)
    return reverse_num2(num)


'''
ine #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     17.9 MiB     17.9 MiB           1   @profile()
    36                                         def new_reverse_num(num):
    37     17.9 MiB      0.0 MiB          37       def reverse_num2(n):
    38     17.9 MiB      0.0 MiB          36           if n < 10:
    39     17.9 MiB      0.0 MiB           1               return n
    40                                                 else:
    41     17.9 MiB      0.0 MiB          35               print(n % 10, end='')
    42     17.9 MiB      0.0 MiB          35               return reverse_num2(n // 10)
    43     17.9 MiB      0.0 MiB           1       return reverse_num2(num)
'''


@profile()
def reverse_num3(num):
    to_str = str(num)
    return to_str[::-1]


'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    46     17.9 MiB     17.9 MiB           1   @profile()
    47                                         def reverse_num3(num):
    48     17.9 MiB      0.0 MiB           1       to_str = str(num)
    49     17.9 MiB      0.0 MiB           1       return to_str[::-1]
'''

a = randint(1000000000000000000000000000000000, 999999999999999999999999999999999999)
print(reverse_num(a))
print(new_reverse_num(a))
print(reverse_num3(a))
'''
Все 3 скрипта быстродейственны и не требуют оптимизации, 
т.к. работают с неизменяемыми типами данных
'''

m0 = memory_usage()
my_list = (i for i in range(50000))
m1 = memory_usage()

m2 = memory_usage()
my_list2 = [i for i in range(50000)]
m3 = memory_usage()

m4 = memory_usage()
my_dict = {i: i for i in range(50000)}
m5 = memory_usage()

m6 = memory_usage()
my_list3 = []
for i in range(50000):
    my_list3.append(i)
m7 = memory_usage()

print(m1[0] - m0[0], type(my_list))
print(m3[0] - m2[0], type(my_list2))
print(m5[0] - m4[0], type(my_dict))
print(m7[0] - m6[0], type(my_list3))
del my_list2
del my_dict
'''
0.0 <class 'generator'>
1.89453125 <class 'list'>
4.03515625 <class 'dict'>
1.80078125 <class 'list'>
При использовании генератора памяти не потребовалось, 
т.к. массив сгенерируется только по вызову.
Список занял 1.89, а словарь 4.04, следовательно список экономичнее.
Заполнение списка через цикл (1.8) оказалось экономичнее, 
чем list comprehension (1.89)

Версия Python 3.8, OC - x64
'''
