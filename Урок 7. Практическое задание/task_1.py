"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint
from timeit import timeit


def bubbled(alist):
    a = alist[::]
    for j in range(len(a)-1, 1, -1):
        for i in range(j):
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a


def smartbubbled(alist):
    a = alist[::]
    # Добавляем этот флаг ...
    issorted = True
    for j in range(len(a)-1, 1, -1):
        for i in range(j):
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                # ... и эту проверку
                issorted = False
        if issorted:
            return a
    return a


SIZE = 1000

# сначала проверим на отсортированных данных
a = list(range(999, -1, -1))
print(
    'с оптимизацией',
    timeit("smartbubbled(a)", globals=globals(), number=100))
print(
    'без оптимизации',
    timeit("bubbled(a)", globals=globals(), number=100))
# ---
# с оптимизацией 0.008331865072250366
# без оптимизации 3.6351050139637664
# ---

# а потом на случайных
a = [randint(-100, 100) for i in range(SIZE)]
print(
    'с оптимизацией',
    timeit("smartbubbled(a)", globals=globals(), number=100))
print(
    'без оптимизации',
    timeit("bubbled(a)", globals=globals(), number=100))
# ---
# с оптимизацией 6.508605795097537
# без оптимизации 6.436502464930527
# ---
# Как и ожидалось, получаем небольшой проигрыш
# из-за дополнительной проверки
