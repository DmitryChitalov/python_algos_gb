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
"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
10000    0.571    0.000    0.607    0.000 task_1.py:27(sort_bubble_smart)
10000    0.585    0.000    0.628    0.000 task_1.py:47(sort_bubble)

умная сортировка быстрее
"""
import random
import cProfile


def create_list():
    """
    функция создает список и заполняет его случайными значениями [-100; 100)
    :return: list
    """
    return [random.randint(-100, 100) for _ in range(200)]


def sort_bubble_smart(my_list_in: list) -> list:
    """
    функция получает список, сортирует его пузырькои по убывание и возвращяет.
    на каждой итерации идет проверка на сортированнсть списка
    :param my_list_in: list
    :return: list
    """
    count = 1
    while count < len(my_list_in):
        flag = True
        for i in range(len(my_list_in) - count):
            if my_list_in[i] < my_list_in[i + 1]:
                my_list_in[i], my_list_in[i + 1] = my_list_in[i + 1], my_list_in[i]
                flag = False
        if flag:
            break
        count += 1
    return my_list_in


def sort_bubble(my_list_in: list) -> list:
    """
    функция получает список, сортирует его пузырькои по убывание и возвращяет.
    :param my_list_in: list
    :return: list
    """
    count = 1
    while count < len(my_list_in):
        for i in range(len(my_list_in) - count):
            if my_list_in[i] < my_list_in[i + 1]:
                my_list_in[i], my_list_in[i + 1] = my_list_in[i + 1], my_list_in[i]
        count += 1
    return my_list_in


def main():
    for _ in range(1000):
        my_list = create_list()
        print(my_list)
        print(sort_bubble_smart(my_list.copy()))
        print(sort_bubble(my_list.copy()))


cProfile.run('main()')