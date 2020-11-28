"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import profile


@profile
def simple(i):
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
def eratosfen(number, l=100000):
    a = [el for el in range(l + 1)]
    a[1] = 0
    i = 2
    while i <= l:
        if a[i] != 0:
            j = i + i
            while j <= l:
                a[j] = 0
                j += i
        i += 1
    return [el for el in a if el != 0][number - 1]


i = 1
print(simple(i))
print(eratosfen(i))

'''
Решил использовать задачу из предыдущих уроков. Сразу видно что в циклах использование памяти меньше.
'''
