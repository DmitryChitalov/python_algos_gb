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

import random
from timeit import timeit


def bubble_sort(in_list):
    n = 1
    while n < len(in_list):
        for i in range(len(in_list) - n):
            if in_list[i] < in_list[i + 1]:
                in_list[i], in_list[i + 1] = in_list[i + 1], in_list[i]
        n += 1
    return in_list


def bubble_sort_2(in_list):
    n = 1
    while n < len(in_list):
        count = 0
        for i in range(len(in_list) - n):
            if in_list[i] < in_list[i + 1]:
                in_list[i], in_list[i + 1] = in_list[i + 1], in_list[i]
                count += 1
        if count == 0:
            n = len(in_list)
        n += 1
    return in_list


def bench_buble_sort(in_list):
    action = f"bubble_sort({in_list})"
    setup = "from __main__ import bubble_sort"
    number = 10000
    return timeit(action, setup, number=number, globals=globals())

def bench_buble_sort_2(in_list):
    action = f"bubble_sort_2({in_list})"
    setup = "from __main__ import bubble_sort_2"
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


def main():
    pass
    try:
        print("gen list")
        rand_list = [random.randint(-100, 100) for _ in range(2000)]
        print("sort list")
        time_sort_1 = bench_buble_sort([rand_list[:]])
        sorted_1 = bubble_sort(rand_list[:])
        print(f"first 10 unsorted \t\t{rand_list[:10]}")
        print(f"first 10 sorted \t\t{sorted_1[:10]}")
        print(f"optimized variant")
        time_sort_2 = bench_buble_sort([rand_list[:]])
        sorted_2 = bubble_sort_2(rand_list[:])
        print(f"first 10 unsorted \t\t{rand_list[:10]}")
        print(f"first 10 sorted \t\t{sorted_2[:10]}")
        if time_sort_1 > time_sort_2:
            print(f"Time sort of not optimized list is faster then optimized: {time_sort_1} > {time_sort_2}")
        else:
            print(f"Time sort of optimized list is faster then simple: {time_sort_2} > {time_sort_1}")
        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()

"""
/home/nek/projects/GeekBrains/python_algos_gb/venv/bin/python "/home/nek/projects/GeekBrains/python_algos_gb/Урок 7. Практическое задание/task_1.py"
gen list
sort list
first 10 unsorted 		[56, -89, 57, -54, 67, -18, 57, -91, 68, -44]
first 10 sorted 		[100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
optimized variant
first 10 unsorted 		[56, -89, 57, -54, 67, -18, 57, -91, 68, -44]
first 10 sorted 		[100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
Time sort of not optimized list is faster then optimized: 0.06603594299986071 > 0.058172805000140215

Программа завершена!

Process finished with exit code 0


"""