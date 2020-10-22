"""Filename: /Users/And/Desktop/python_algos_gb/Урок 6. Практическое задание/sieve_example.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     13.2 MiB     13.2 MiB           1   @profile
     6                                         def simple(i):
     7                                             "Без использования «Решета Эратосфена»"
     8     13.2 MiB      0.0 MiB           1       count = 1
     9     13.2 MiB      0.0 MiB           1       n = 2
    10     13.2 MiB      0.0 MiB        1986       while count <= i:
    11     13.2 MiB      0.0 MiB        1986           t = 1
    12     13.2 MiB      0.0 MiB        1986           is_simple = True
    13     13.2 MiB      0.0 MiB      278385           while t <= n:
    14     13.2 MiB      0.0 MiB      278085               if n % t == 0 and t != 1 and t != n:
    15     13.2 MiB      0.0 MiB        1686                   is_simple = False
    16     13.2 MiB      0.0 MiB        1686                   break
    17     13.2 MiB      0.0 MiB      276399               t += 1
    18     13.2 MiB      0.0 MiB        1986           if is_simple:
    19     13.2 MiB      0.0 MiB         300               if count == i:
    20     13.2 MiB      0.0 MiB           1                   break
    21     13.2 MiB      0.0 MiB         299               count += 1
    22     13.2 MiB      0.0 MiB        1985           n += 1
    23     13.2 MiB      0.0 MiB           1       return n


Filename: /Users/And/Desktop/python_algos_gb/Урок 6. Практическое задание/sieve_example.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    26     13.2 MiB     13.2 MiB           1   @profile
    27                                         def sieve(n, m=1):
    28                                             "Решето"
    29     13.8 MiB      0.6 MiB       10303       a = [p for p in range(n+10000*m)]
    30     13.8 MiB      0.0 MiB           1       a[1] = 0
    31     13.8 MiB      0.0 MiB           1       i = 2
    32     13.8 MiB      0.0 MiB       10299       while i <= n+10000*m-1:
    33     13.8 MiB      0.0 MiB       10298           if a[i] != 0:
    34     13.8 MiB      0.0 MiB        1262               j = i + i
    35     13.8 MiB      0.0 MiB       25063               while j <= n+10000*m-1:
    36     13.8 MiB      0.0 MiB       23801                   a[j] = 0
    37     13.8 MiB      0.0 MiB       23801                   j = j + i
    38     13.8 MiB      0.0 MiB       10298           i += 1
    39
    40     13.8 MiB      0.0 MiB           1       if (len(set(a))) < n:
    41                                                 return sieve(n, m+2)
    42                                             else:
    43     13.8 MiB      0.0 MiB           1           a = sorted(list(set(a)))
    44     13.8 MiB      0.0 MiB           1           a.remove(0)
    45     13.8 MiB      0.0 MiB           1           return a[n-1]


1987 1987
"""

from memory_profiler import profile


@profile
def simple(i):
    """Без использования «Решета Эратосфена»"""
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
def sieve(n, m=1):
    """Решето"""
    a = [p for p in range(n+10000*m)]
    a[1] = 0
    i = 2
    while i <= n+10000*m-1:
        if a[i] != 0:
            j = i + i
            while j <= n+10000*m-1:
                a[j] = 0
                j = j + i
        i += 1

    if (len(set(a))) < n:
        return sieve(n, m+2)
    else:
        a = sorted(list(set(a)))
        a.remove(0)
        return a[n-1]


if __name__ == '__main__':
    n = 300
    print(simple(n),
          sieve(n))
