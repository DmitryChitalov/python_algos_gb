"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from random import randint
from timeit import default_timer, repeat, timeit


def time_decorator(some_func):
    """ Вычисляет время выполения декорируемой функции"""

    def wrapper(*args, **kwargs):
        start = default_timer()
        result = some_func(*args, **kwargs)
        print(f'Время выполнения функции {some_func.__name__} замеренное декоратором: {default_timer() - start}.')
        return result

    return wrapper


lst = [randint(-100, 100) for _ in range(10000)]
# делаем три одинаковые копии, чтобы все три функции работали с одинковыми по наполнению списками
lst1 = lst.copy()
lst2 = lst.copy()
lst3 = lst.copy()


# 1 вариант
@time_decorator
def bubble_sort_unoptimized(some_lst):
    """Выполняет самую простую сортировку пузырьком"""
    print(some_lst)
    for i in range(len(some_lst)):
        for j in range(len(some_lst) - 1):
            if some_lst[j] < some_lst[j + 1]:
                some_lst[j], some_lst[j + 1] = some_lst[j + 1], some_lst[j]
    return print(some_lst)


# 2 вариант
@time_decorator
def bubble_sort_optimized1(some_lst):
    """Сортировка пузырьком с использованием маркера"""
    print(some_lst)
    flag = True
    while flag:
        flag = False
        for i in range(len(some_lst) - 1):
            if some_lst[i] < some_lst[i + 1]:
                some_lst[i], some_lst[i + 1] = some_lst[i + 1], some_lst[i]
                flag = True
    return print(some_lst)


# 3 вариант
@time_decorator
def bubble_sort_optimized2(some_lst):
    """Сортировка пузырьком с использованием маркера и сокращением числа итераций"""
    print(some_lst)
    flag = True
    iter_counter = 0  # счетчик итераций
    while flag:
        flag = False
        for i in range(len(some_lst) - iter_counter - 1):  # уменьшаем число итераций на 1 каждый раз
            if some_lst[i] < some_lst[i + 1]:
                some_lst[i], some_lst[i + 1] = some_lst[i + 1], some_lst[i]
                flag = True
        iter_counter += 1
    return print(some_lst)


bubble_sort_unoptimized(lst1)
print('-' * 160)
bubble_sort_optimized1(lst2)
print('-' * 160)
bubble_sort_optimized2(lst3)
print('-' * 160)

"""
Проводил несколько измерений. Третий вариант, в котором используем маркер (показывает, была ли проведена перестановка) и
также сокращем количество на 1 после каждого прохода (так как уже знаем что после первой итерации крайний левый элемент
самый большой, после второй итерации самый большой из оставшихся - второй слева и тд, то есть их уже нет необходимости
сравнивать) работает всегда быстрее (11.573743899999997).
Второй вариант вариант (когда используем только маркер), не дает выигрыша существенного выигрыша в скорости по сравению 
с первым (18.1884085 против 19.1428449).
"""

# Протестируем на меньшей длине списка (1000 элементов) и сравним замеры, сделанные самодельным декоратором и timeit
small_lst = [randint(-100, 100) for _ in range(1000)]

# делаем три одинаковые копии, чтобы все три функции работали с одинковыми по наполнению списками
lst4 = small_lst.copy()
lst5 = small_lst.copy()
lst6 = small_lst.copy()

setup = """
from __main__ import bubble_sort_unoptimized, bubble_sort_optimized1, bubble_sort_optimized2, lst4, lst5, lst6
"""
statements = [
    ['Время выполнения bubble_sort_unoptimized, замеренное timeit: ', 'bubble_sort_unoptimized(lst4)'],
    ['Время выполнения bubble_sort_unoptimized1, замеренное timeit: ', 'bubble_sort_optimized1(lst5)'],
    ['Время выполнения bubble_sort_unoptimized2, замеренное timeit: ', 'bubble_sort_optimized2(lst6)']
]

for info, st in statements:
    print(info, max(repeat(st, setup, default_timer, 1, 1)))
