"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""

# Рассмотрим решение задачи нахождения суммы максимума из чисел с четными номерами
# и минимума из чисел с нечетными номерами.
# Числа записаны в файл

from timeit import default_timer
from memory_profiler import memory_usage
from random import randint
from re import finditer


# Декоратор, который будет замерять время работы и используемую память
def meas(func):
    def wrapper():
        m1 = memory_usage()
        t1 = default_timer()
        res = func()
        t2 = default_timer()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = t2 - t1
        return res, mem_diff, time_diff
    return wrapper

# Решение через встроенные функции
@meas
def solution_1():
    with open("data.txt") as ff:
        st = ff.readline().split()
    ll = len(st)
    max_even, min_odd = max(int(st[i]) for i in range(1, ll, 2)), \
                        min(int(st[i]) for i in range(0, ll, 2))
    return max_even + min_odd

# Решение через генератор и регулярные выражения
@meas
def solution_2():
    with open("data.txt", "rb") as ff:
        st = finditer(b'-?\d+', ff.read())

    def next_num():
        return int(next(st).group())

    min_odd = next_num()
    max_even = next_num()

    while True:
        try:
            num = next_num()
            if min_odd > num:
                min_odd = num

            num = next_num()
            if max_even < num:
                max_even = num

        except StopIteration:
            break

    return max_even + min_odd


# Заполним файл данными
my_f = open("data.txt", "w")
N = randint(20000, 200000)
for i in range(N):
    print(f"{randint(-100000, 100000000)}", file=my_f, end=" ")

res, mem, tim = solution_1()
print(f"Результат #1: {res}. Время - {tim}. Память - {mem}")

res, mem, tim = solution_2()
print(f"Результат #2: {res}. Время - {tim}. Память - {mem}")

print(
    """
Через встроенные функции (вариант #1) чаще работает быстрее, но требует больше памяти.
Варинат #2 благодоря чтению файла как бинарного и использования генератора
использует существенно меньше памяти.
    """
)
