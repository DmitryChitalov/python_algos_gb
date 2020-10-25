"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from statistics import median
import random
from timeit import timeit

def quickselect(l, k, pivot_func=random.choice):
    # Базовый случай.
    if len(l) == 1:
        return l[0]
    # Выбираем индекс опорного элемента.
    pivot = pivot_func(l)
    # Разбиваем исходный список на больше/меньше опорного элемента.
    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]
    # Ищем медиану.
    if k < len(lows):
        return quickselect(lows, k, pivot_func)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_func)

if __name__ == '__main__':
    m = input('Введите m: ')
    l = [random.uniform(-1000, 1000) for i in range(2*int(m) + 1)]
    print('Исходный список:')
    print(l)
    print('Поиск медианы "быстрым выбором".')
    print(f'Медиана: {quickselect(l, len(l)/2)}')
    print('Время нахождения медианы "быстрым выбором": ',
          timeit(f'quickselect({l}, {len(l) / 2})',
                 setup='from __main__ import quickselect, l',
                 number=1000))
    print('Поиск медианы с помощью модуля statistics.')
    print(f'Медиана: {median(l)}')
    print('Время нахождения медианы встроенными средствами: ',
          timeit(f'median({l})',
                 setup='from __main__ import median, l',
                 number=1000))

"""
Несмотря на теоретическое превосходство "быстрого выбора" перед Timsort,
который используется в функции statistics.median (O(n) в лучшем случае
и O(n^2) в худшем), множественные запуски программы однозначно указывают
на превосходство встроенных средств. Могу объяснить это только лучшей
оптимизацией встроенных алгоритмов в python. Всё равно опыт был очень
интересным.
"""