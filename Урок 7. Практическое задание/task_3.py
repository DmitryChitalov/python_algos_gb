"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""

from random import randint
from timeit import timeit
import statistics as st
from argparse import ArgumentParser

p = ArgumentParser("Median functions")
p.add_argument(
    '-s', '--size',
    type=int, default=10000,
    help='Array size')
p.add_argument(
    '-n', '--number',
    type=int, default=100,
    help='Number of timeit runs')
p.add_argument(
    '-f', '--firsttry', action='store_true',
    help='Run only first function')
args = p.parse_args()


# Алгоритм состоит из двух частей.
# Во-первых, реализована основная часть алгоритма
# быстрой сортировки (quicksort), которая делит
# массив на две части по выделенному элементу (pivot).
# Справа от pivot большие числа, слева -- меньшие.
# Во-вторых, применяется бинарный поиск, который
# сужает окно сортировки на каждой итерации
# в зависимости от положения pivot по отношению
# к середине массива.
def median(arr):
    m = len(arr)//2
    b = arr[::]
    # Вначале делаем "окно" (winright, winleft) равным всему списку
    winleft = 0
    winright = len(b) - 1
    while True:
        # В начале цикла делаем копию списка, чтобы заполнять ее
        # справа и слева
        a = b[::]
        # Проходим по "окну".
        # Берем значение pivot из середины списка и формируем
        # новый список, в котором значения меньше pivot
        # слева, а больше -- справа.
        pivot = a[m]
        left = winleft
        right = winright
        for i in range(winleft, winright + 1):
            if i == m:
                continue
            if a[i] <= pivot:
                b[left] = a[i]
                left += 1
            else:
                b[right] = a[i]
                right -= 1
        b[left] = pivot
        # В зависимости от того, в какую часть попадает середина списка
        # сужаем "окно" или слева, или справа.
        # Повторяем до тех пор, пока границы окна не "сойдутся" в середине.
        if left == m:
            break
        if left < m:
            winleft = left + 1
        else:
            winright = left - 1
    return b[m]


# Проверим производительность
arr = [randint(1, 9999) for i in range(2*args.size + 1)]
# Эта переменная нужна, чтобы возвращать значение из timeit
res = [0]

if args.firsttry:
    print(
        "встроенная: ",
        timeit("res[0] = st.median(arr)", globals=globals(), number=100),
        "s, результат: ",
        res[0])
    print(
        "с копированием: ",
        timeit("res[0] = median(arr)", globals=globals(), number=100),
        "s, результат: ",
        res[0])
# ---
# встроенная:  0.28833733906503767 s, результат:  5012
# с копированием:  1.088268078980036 s, результат:  5012
# ---
# Хуже всего в 3 раза, чем встроенная функция,
# это отличный результат.


# Но у нас есть потенциал для оптимизации. Можно
# избежать копирования массива в начале цикла
def median_nocopy(arr):
    m = len(arr)//2
    a = arr[::]
    winleft = 0
    winright = len(a) - 1
    while True:
        # Тогда pivot будет в конце "окна", обозначим его
        # квадратными скобками
        # <front><i> 9 7 1 4 6 3 2 8 [5]
        # <i> показывает текущий элемент,
        # <front> -- границу малых и больших значений
        pivot = a[winright]
        front = winleft
        for i in range(winleft, winright):
            # Пока значения больше, чем pivot, просто
            # передвигаем индекс текущего элемента
            # <front> 9 7 <i> 1 4 6 3 2 8 [5]
            if a[i] > pivot:
                continue
            else:
                # В противном случае меняем текущий элемент
                # местами с числом перед front
                # 1 <front> 7 9 <i> 4 6 3 2 8 [5]
                a[i], a[front] = a[front], a[i]
                front += 1
        # В конце цикла должно получиться
        # 1 4 3 2 <front> [5] 9 7 8 <i> 6
        a[winright], a[front] = a[front], a[winright]
        # изменение границ окна полностью соответствует
        # предыдущей функции
        if front == m:
            return pivot
        if front < m:
            winleft = front + 1
        else:
            winright = front - 1


if not args.firsttry:
    print(
        "встроенная: ",
        timeit("res[0] = st.median(arr)", globals=globals(), number=100),
        "s, результат: ",
        res[0])
    print(
        "с копированием: ",
        timeit("res[0] = median(arr)", globals=globals(), number=100),
        "s, результат: ",
        res[0])
    print(
        "без копирования: ",
        timeit(
            "res[0] = median_nocopy(arr)",
            globals=globals(), number=100),
        "s, результат: ",
        res[0])

# ---
# встроенная:  0.293416955973953 s, результат:  5045
# с копированием:  0.9642031160183251 s, результат:  5045
# без копирования:  0.49384179897606373 s, результат:  5045
# ---

# Результат улучшился примерно вдвое, и стал медленнее
# встроенной функции всего в 1.6 раз
