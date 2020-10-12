"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""


from memory_profiler import profile
from memory_profiler import memory_usage

# попробуем затестить пострение списка фибоначчи через цикл, yield, а заодно и через рекурсию (посмотрим что будет)


def f_1(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


gener = f_1(10)
for j in gener:
    print(j)

# тут через memory_usage сделал, получается 0 по памяти


@profile
def f_2(n):
    res = []
    a = b = 1
    res.append(a)
    res.append(b)
    for i in range(int(n - 2)):
        a, b = b, a + b
        res.append(b)
    return res


@profile
def f_3(n):
    a = 1
    if n > 2:
        a = f_3(n-1) + f_3(n-2)
    return a

# с рекурсией profiler использовать в таком виде не наглядно - он запускается каждый раз, когда мы вызываем функцию.
# Итого в данном примере если n = 10, то и функция вызывается внутри 10 раз, и профайлер запускается отдельно 10 раз.


if __name__ == "__main__":

    m1 = memory_usage()
    gener = f_1(10)
    for j in gener:
        print(j)
    m2 = memory_usage()
    print(f'память: {m2[0] - m1[0]}')

    f_2(10)
    f_3(10)


