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
import timeit
from functools import wraps


class BubbleSort:
    def __init__(self, list_src):
        self.list_src = list_src
        self.list_sort = []

    def __str__(self):
        return f'Исходный список - {self.list_src}\n' \
               f'Результирующий список - {self.list_sort}'

    def _measurer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t1 = timeit.default_timer()
            func(*args, **kwargs)
            t2 = timeit.default_timer()
            return print(f'Выполнение заняло {(t2 - t1):.05} сек')
        return wrapper

    @_measurer
    def sort_list(self):
        n = 1
        self.list_sort = self.list_src[:]
        while n < len(self.list_sort):
            for i in range(len(self.list_sort) - n):
                if self.list_sort[i] < self.list_sort[i + 1]:
                    self.list_sort[i], self.list_sort[i + 1] = self.list_sort[i + 1], self.list_sort[i]
            n += 1
        return self.list_sort

    @_measurer
    def sort_list_mod(self):
        n = 1
        j = 0
        self.list_sort = self.list_src[:]
        while n < len(self.list_sort):
            for i in range(len(self.list_sort) - n):
                if self.list_sort[i] < self.list_sort[i + 1]:
                    self.list_sort[i], self.list_sort[i + 1] = self.list_sort[i + 1], self.list_sort[i]
                    j = 1
            if j == 0:
                break
            n += 1
        return self.list_sort


obj = BubbleSort([random.randint(-100, 100) for _ in range(1000)])
obj.sort_list()
print(obj)

obj.sort_list_mod()
print(obj)

obj_2 = BubbleSort([i for i in range(1000, 0, -1)])
obj_2.sort_list()
print(obj_2)

obj_2.sort_list_mod()
print(obj_2)

"""
В методе sort_list реализован алгорит пузырьковой сортировки.
В методе sort_list_mod реализован усовершенствованный алгоритм пузырьковой сортировки,
добавлено условие при котором если за проход не было перемещений елементов списка, происходит
остановка цикла и возврат сортированного списка.

-- Рандомный список --
Стандартный метод - Выполнение заняло 0.22195 сек
Модернизированный метод - Выполнение заняло 0.2278 сек

-- Сортированный список --
Стандартный метод - Выполнение заняло 0.12163 сек
Модернизированный метод - Выполнение заняло 0.00024915 сек

ВЫВОД: При подаче на сортировку рандомного списка время не примерно одинаково у обоих методов,
но если подать заранее отсортированный список, соответственно время выполнения у модернизированного метода
гораздо меньше.
"""


