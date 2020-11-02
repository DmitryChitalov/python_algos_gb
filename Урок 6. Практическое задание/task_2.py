"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов

python 3.8.2
Windows 10 64 bit

"""

from memory_profiler import profile
import memory_profiler
import time

numbers = range(1000)


@profile
def check_even_1(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num * num)
    return even


@profile
def check_even_2(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num


if __name__ == '__main__':
    m_1 = memory_profiler.memory_usage()
    t_1 = time.time()
    cubes_1 = check_even_1(range(100000))
    t_2 = time.time()
    m_2 = memory_profiler.memory_usage()
    time_diff_1 = t_2 - t_1
    mem_diff_1 = m_2[0] - m_1[0]
    print(f"Потребовалось {time_diff_1} сек. и { mem_diff_1} МБ для выполнения этого метода ")

    m1 = memory_profiler.memory_usage()
    t1 = time.time()
    cubes = check_even_2(range(10000000000))
    t2 = time.time()
    m2 = memory_profiler.memory_usage()
    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]
    print(f"Для выполнения этого метода потребовалось {time_diff} сек и {mem_diff} МБ")


"""
Для  обычного метода без генератора для числа 100000 потребовалось 7.757047414779663 1.734375 МБ

Для генератора с числом 10000000000  потребовалось 0.051045894622802734 сек и 0.1875 МБ



Преимущество генератора заключается в том, что генераторы не хранят все результаты в памяти, а генерируют их на лету, 
поэтому память используется только тогда, когда мы запрашиваем результат.
"""