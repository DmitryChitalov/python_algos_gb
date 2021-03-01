"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
"""
стандартные задачки по комбинаторике отлично подойдут для массовости рекурсивных функций.
Замечане: Я прекрасно понимаю, что это не оптимальный алгоритм. Что n!/(n-m)! = n*...*(n-m+1) и тд
моя задача была использовать рекурсию.
Дополнительный замер памяти до и после, по профеллировщику не оч видно, с другой стороны разность замеров после и до
может быть не очень объективна.
"""
from memory_profiler import profile
from memory_profiler import memory_usage


@profile
def recurs_decorator(func_name):
    def wrapper(*arg, **kwargs):
        func_name(*arg, **kwargs)
    return wrapper


# число размещений n элементов по m A = n!/(n-m)!
# @recurs_decorator
def placements(num_n, num_m, result):
    if num_m == 1:
        print(f"Число комбинаций: {int(result)}")
        return result
    num_sub = num_m-num_n if num_m-num_n > 1 else 1
    result *= num_m/num_sub
    num_m -= 1
    return placements(num_n, num_m, result)


# число сочетаний из n элементов по m С = n!/ k!(n-k)!
def combinations_no_repetitions(num_n, num_m, num_sub, result):
    if num_n == 1:
        print(f"Число комбинаций: {int(result)}")
        return result
    num_mult = num_m * num_sub if num_m * num_n > 1 else 1
    result *= num_n/num_mult
    num_n -= 1
    if num_m > 1:
        num_m -= 1
    if num_sub > 1:
        num_sub -= 1
    return combinations_no_repetitions(num_n, num_m, num_sub, result)


# число сочетаний с повторениями из n элементов по m C = (n+m-1)!/m!(n-1)!
def combinations_with_repetitions(num_n, num_m, num_add, result):
    if num_add == 1:
        print(f"Число комбинаций: {int(result)}")
        return result
    num_mult = num_m * (num_n - 1) if num_m * (num_n - 1) > 1 else 1
    result *= (num_add - 1)/num_mult
    num_add -= 1
    if num_n > 1:
        num_n -= 1
    if num_m > 1:
        num_m -= 1
    return combinations_with_repetitions(num_n, num_m, num_add, result)


print("Найдем количество вариантов размещения n шаров по m ячейкам. n < m")
try:
    n = int(input("Задайте n: "))
    m = int(input("Задайте m: "))
except ValueError:
    print("Некорректный ввод")
    exit()
if n > m:
    print("Бессмысленна задача")
else:
    try:
        m1 = memory_usage()
        print(recurs_decorator(placements(int(n), int(m), 1)))
        # print(placements(int(n), int(m), 1)) # в декоратор заходит, но профилировщик не отрабатывает.
        m2 = memory_usage()
        print(f"Использовано {m2[0] - m1[0]} Mb памяти.")
    except RecursionError:
        print("Великоваты числа для рекурсивных функций")
        exit()

print("Найдем количество вариантов выбора m из n. n > m")
try:
    n = int(input("Задайте n (общее количество объектов): "))
    m = int(input("Задайте m (сколько выбираем): "))
except ValueError:
    print("Некорректный ввод")
    exit()
if n < m:
    print("Бессмысленна задача")
else:
    try:
        print("Без возвращений ")
        m1 = memory_usage()
        print(recurs_decorator(combinations_no_repetitions(int(n), int(m), int(n) - int(m), 1)))
        m2 = memory_usage()
        print(f"Использовано {m2[0] - m1[0]} Mb памяти.")
        print("С возвращением ")
        m1 = memory_usage()
        print(recurs_decorator(combinations_with_repetitions(int(n), int(m), int(n) + int(m), 1)))
        m2 = memory_usage()
        print(f"Использовано {m2[0] - m1[0]} Mb памяти.")
    except RecursionError:
        print("Великоваты числа для рекурсивных функций")
        exit()


# recurs_decorator(placements())
