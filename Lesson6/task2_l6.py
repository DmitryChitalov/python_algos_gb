"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""


from memory_profiler import profile


@profile
def simple(i):
    """Наивный алгоритм"""
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


@profile
def eratosfen(i):
    """Решето Эратосфена"""
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1


    return [p for p in sieve if p != 0][i-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(eratosfen(i))


"""
Python 3.8, Windows 10 x64.

Выполнен запуск функции Решето Эратосфена двумя вариантами (Лекция 4, задача 5)
Результаты для порядкого числа 27:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    20     18.3 MiB     18.3 MiB           1   @profile
    21                                         def simple(i):
    22                                             """Наивный алгоритм"""
    23     18.3 MiB      0.0 MiB           1       count = 1
    24     18.3 MiB      0.0 MiB           1       n = 2
    25     18.3 MiB      0.0 MiB         102       while count <= i:
    26     18.3 MiB      0.0 MiB         102           t = 1
    27     18.3 MiB      0.0 MiB         102           is_simple = True
    28     18.3 MiB      0.0 MiB        1490           while t <= n:
    29     18.3 MiB      0.0 MiB        1463               if n % t == 0 and t != 1 and t != n:
    30     18.3 MiB      0.0 MiB          75                   is_simple = False
    31     18.3 MiB      0.0 MiB          75                   break
    32     18.3 MiB      0.0 MiB        1388               t += 1
    33     18.3 MiB      0.0 MiB         102           if is_simple:
    34     18.3 MiB      0.0 MiB          27               if count == i:
    35     18.3 MiB      0.0 MiB           1                   break
    36     18.3 MiB      0.0 MiB          26               count += 1
    37     18.3 MiB      0.0 MiB         101           n += 1
    38     18.3 MiB      0.0 MiB           1       return n



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    41     18.3 MiB     18.3 MiB           1   @profile
    42                                         def eratosfen(i):
    43                                             """Решето Эратосфена"""
    44     18.3 MiB      0.0 MiB           1       n = 2
    45     18.3 MiB      0.0 MiB           1       l = 10000
    46     18.8 MiB      0.4 MiB       10003       sieve = [x for x in range(l)]
    47     18.8 MiB      0.0 MiB           1       sieve[1] = 0
    48     18.8 MiB      0.0 MiB        9999       while n < l:
    49     18.8 MiB      0.0 MiB        9998           if sieve[n] != 0:
    50     18.8 MiB      0.0 MiB        1229               m = n*2
    51     18.8 MiB      0.0 MiB       24298               while m < l:
    52     18.8 MiB      0.0 MiB       23069                   sieve[m] = 0
    53     18.8 MiB      0.0 MiB       23069                   m += n
    54     18.8 MiB      0.0 MiB        9998           n += 1
    55                                         
    56                                         
    57     18.8 MiB      0.0 MiB       10003       return [p for p in sieve if p != 0][i-1]

В первом варианте память выделяется один раз; во втором - есть незначительный 
прирост памяти в процесс для генерации списка (0.4MiB)
*При этом по времени второй вариант несравненно (на два порядка) выигрышнее на больших числах.
        
[Незначительный инкремент обусловлен необходимостью генерации списка
Величина инкремента может изменяться, в зависимости от объема списка
При этом в целом инкремент находится в рамках нормы
Оптимизация не требуется]
"""
