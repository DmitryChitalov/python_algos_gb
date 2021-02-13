"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import memory_usage
from timeit import default_timer
from random import randint


# from numpy import array

def measure(func):
    def wrapper(*args, **kwargs):
        m_start = memory_usage()
        t_start = default_timer()
        res = func(*args, **kwargs)
        t_end = default_timer()
        m_end = memory_usage()
        mem_diff = m_end[0] - m_start[0]
        tim_diff = t_end - t_start
        return res, mem_diff, tim_diff

    return wrapper


@measure
def even_1(n):
    var_list = []
    for i in range(n):
        if i % 2 == 0:
            var_list.append(i)
    return var_list


@measure
def even_2(n):
    var_list = [i for i in range(n) if i % 2 == 0]
    return var_list


@measure
def simple_1(i):
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


@measure
def simple_2(n):
    i = 2
    nums = []
    end_elem = n * 10
    for item in range(n * 10):
        nums.append(item)

    nums[1] = 0
    while i < end_elem:
        if nums[i] != 0:
            j = i + i
            while j < end_elem:
                nums[j] = 0
                j = j + i
        i = i + 1

    res = []
    for item in nums:
        if item != 0:
            res.append(item)

    return res[n - 1]


array = [randint(0, 10) for i in range(20000)]


@measure
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@measure
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


res, mem_diff, time_diff = even_1(200000000)
print(f'Выполнение even_1 заняло {mem_diff} MiB и {time_diff} секунд')
del (res)
del (mem_diff)
del (time_diff)

res, mem_diff, time_diff = even_2(200000000)
print(f'Выполнение even_2 заняло {mem_diff} MiB и {time_diff} секунд')
del (res)
del (mem_diff)
del (time_diff)

res, mem_diff, time_diff = simple_1(5000)
print(f'Выполнение simple_1 заняло {mem_diff} MiB и {time_diff} секунд')
del (res)
del (mem_diff)
del (time_diff)

res, mem_diff, time_diff = simple_2(5000)
print(f'Выполнение simple_2 заняло {mem_diff} MiB и {time_diff} секунд')
del (res)
del (mem_diff)
del (time_diff)

res, mem_diff, time_diff = func_1()
print(f'Выполнение func_1 заняло {mem_diff} MiB и {time_diff} секунд')
del (res)
del (mem_diff)
del (time_diff)

res, mem_diff, time_diff = func_2()
print(f'Выполнение func_2 заняло {mem_diff} MiB и {time_diff} секунд')
del (res)
del (mem_diff)
del (time_diff)

# Выполнение even_1 заняло 3864.05078125 MiB и 37.7986929 секунд
# Выполнение even_2 заняло 3862.9296875 MiB и 21.763604900000004 секунд
#
# функции even_1 и even_2 заняли памяти одинаково, т.к. формируется одинаковый
# список, но even_2 выполняется немного быстрее
#
#
# Выполнение simple_1 заняло 0.0 MiB и 17.2393301 секунд
# Выполнение simple_2 заняло 1.5234375 MiB и 0.07218179999999919 секунд
# simple_1 выполняется долше, но при этом требуется меньше памяти
# (т.к. не формируется List)
#
# Выполнение func_1 заняло 0.0 MiB и 8.219181299999999 секунд
# Выполнение func_2 заняло 0.35546875 MiB и 8.246644700000001 секунд
# Вторая функция использует дополнительный список, поэтому требуется больше памяти
