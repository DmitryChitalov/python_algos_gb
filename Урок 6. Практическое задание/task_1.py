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

def measure(func):
    def wrapper(*args, **kwargs):
        t1 = default_timer()
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        t2 = default_timer()
        mem_diff = m2[0] - m1[0]
        tim_diff = t2 - t1
        return res, mem_diff, tim_diff
    return wrapper

@measure
def get_even_1(nums):
    new_arr = []
    i = 0
    for rec in nums:
        if rec % 2 == 0:
            new_arr.append(i)
        i += 1
    return new_arr

@measure
def get_even_2(nums):
    new_arr = ''
    i = 0
    for rec in nums:
        if rec % 2 == 0:
            new_arr = f'{new_arr}-{i}'
        i += 1
    return new_arr

g_res, g_mem, g_tim = get_even_1(list(range(100000)))
print(f"Выполнение заняло {g_mem} Mib, {g_tim} сек.")
g_res, g_mem, g_tim = get_even_2(list(range(100000)))
print(f"Выполнение заняло {g_mem} Mib, {g_tim} сек.")
# Задача: вернуть список индексов четных элементов массива.
# get_even_1 - неоптимизированный вариант.
# get_even_2 - оптимизированный вариант.
# Вывод данной задачи:
#Выполнение заняло 2.3515625 Mib, 0.21003900000000003 сек.
#Выполнение заняло 1.12109375 Mib, 0.49328999999999995 сек.
# Оптимизация произведена по памяти(get_even_2) за счет того, что
# индексы возвращены через строку(ее можно потом распарсить),
# а не через список.
# Разрядность ОС: 64, python версии 3.9.0.
# Программы 2, 3, 4 в файлах task_1-2.py, task_1-3.py, task_1-4.py.
