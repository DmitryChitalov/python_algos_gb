"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import profile


@profile
def simple(i):
    """Перебор делителей"""
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
Line #    Mem usage    Increment   Line Contents
================================================
    19     40.2 MiB     40.2 MiB   @profile
    20                             def simple(i):
    21     40.2 MiB      0.0 MiB       count = 1
    22     40.2 MiB      0.0 MiB       n = 2
    23     40.2 MiB      0.0 MiB       while count <= i:
    24     40.2 MiB      0.0 MiB           t = 1
    25     40.2 MiB      0.0 MiB           is_simple = True
    26     40.2 MiB      0.0 MiB           while t <= n:
    27     40.2 MiB      0.0 MiB               if n % t == 0 and t != 1 and t != n:
    28     40.2 MiB      0.0 MiB                   is_simple = False
    29     40.2 MiB      0.0 MiB                   break
    30     40.2 MiB      0.0 MiB               t += 1
    31     40.2 MiB      0.0 MiB           if is_simple:
    32     40.2 MiB      0.0 MiB               if count == i:
    33     40.2 MiB      0.0 MiB                   break
    34     40.2 MiB      0.0 MiB               count += 1
    35     40.2 MiB      0.0 MiB           n += 1
    36     40.2 MiB      0.0 MiB       return n


Line #    Mem usage    Increment   Line Contents
================================================
    39     40.2 MiB     40.2 MiB   @profile
    40                             def eratosfen(i):
    41     40.2 MiB      0.0 MiB       n = 2
    42     40.2 MiB      0.0 MiB       l = 10000
    43     40.8 MiB      0.1 MiB       sieve = [x for x in range(l)]
    44     40.8 MiB      0.0 MiB       sieve[1] = 0
    45     40.8 MiB      0.0 MiB       while n < l:
    46     40.8 MiB      0.0 MiB           if sieve[n] != 0:
    47     40.8 MiB      0.0 MiB               m = n*2
    48     40.8 MiB      0.0 MiB               while m < l:
    49     40.8 MiB      0.0 MiB                   sieve[m] = 0
    50     40.8 MiB      0.0 MiB                   m += n
    51     40.8 MiB      0.0 MiB           n += 1
    52     40.9 MiB      0.1 MiB       return [p for p in sieve if p != 0][i-1]
    
Незначительный инкремент обусловлен необходимостью генерации списка
Величина инкремента может изменяться, в зависимости от объема списка
При этом в целом инкремент находится в рамках нормы
Оптимизация не требуется
"""
