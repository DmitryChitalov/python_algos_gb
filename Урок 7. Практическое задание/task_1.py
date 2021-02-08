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
from timeit import repeat


def bubble_reverted(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def bubble_reverted_opt(lst):
    n = 1
    changes = True
    while (n < len(lst)) and changes:
        for i in range(len(lst) - n):
            changes = False
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                changes = True
        n += 1
    return lst


my_list = [random.randint(-100, 100) for _ in range(1000)]  # такая большая длина, чтобы были повторяющиеся элементы
my_list_cp = [my_list[i] for i in range(len(my_list))]

"""
Исправил метод копирования списка, не думал, что данный скопированный тоже будет меняться при изменении оригинала
Просто представленный метод на вебинаре каждый раз создаёт разные списки, и на них сравнивать нелогично
"""

print(my_list)
print(bubble_reverted(my_list))
print(min(repeat(
    'bubble_reverted(my_list)',
    globals=globals(),
    repeat=5,
    number=50
)))
print(my_list_cp)
print(bubble_reverted_opt(my_list_cp))
print(min(repeat(
    'bubble_reverted_opt(my_list_cp)',
    globals=globals(),
    repeat=5,
    number=50
)))

"""
без оптимизации - 1.7335080000000005
с оптимизацией - 0.00761610000000168
разница колоссальная благодаря тому, что лишние разы не бегает по списку после того, как уже всё выстроено
"""
