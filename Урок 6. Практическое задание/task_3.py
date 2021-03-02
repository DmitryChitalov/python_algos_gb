from memory_profiler import profile

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

length = 900


@profile
def recursion(length):
    def sum_series_numbers(n, elem=1):
        if n <= 0:
            return 0
        return elem + sum_series_numbers(n - 1, -elem / 2)
    print(
        f'Сумма последовательности из {length} элементов равна {sum_series_numbers(length)}')


@profile
def for_in(length):
    elem = 1
    amount = 0
    for i in range(length):
        amount += elem
        elem = -elem / 2
    print(f'Сумма последовательности из {length} элементов равна {amount}')


for_in(length)
recursion(length)


'''
Результат работы функции for_in(900)
Line #    Mem usage    Increment   Line Contents
================================================
   131     15.8 MiB     15.8 MiB   @profile
   132                             def for_in(length):
   133     15.8 MiB      0.0 MiB       elem = 1
   134     15.8 MiB      0.0 MiB       amount = 0
   135
   136     15.8 MiB      0.0 MiB       for i in range(length):
   137     15.8 MiB      0.0 MiB           amount += elem
   138     15.8 MiB      0.0 MiB           elem = -elem / 2
   139
   140     15.8 MiB      0.0 MiB       print(f'Сумма последовательности из {length} элементов равна {amount}')


Результат работы функции recursion(900)
Line #    Mem usage    Increment   Line Contents
================================================
   121     15.8 MiB     15.8 MiB   @profile
   122                             def recursion(length):
   123     17.1 MiB      0.1 MiB       def sum_series_numbers(n, elem=1):
   124     17.1 MiB      0.0 MiB           if n <= 0:
   125     17.1 MiB      0.0 MiB               return 0
   126     17.1 MiB      0.0 MiB           return elem + sum_series_numbers(n - 1, -elem/2)
   127
   128     17.1 MiB      0.0 MiB       print(f'Сумма последовательности из {length} элементов равна {sum_series_numbers(length)}')
Рекурсия требует больше памяти , т.к. при ее работе хранится стек вызываемых функций.
'''
