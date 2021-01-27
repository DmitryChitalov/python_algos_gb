from statistics import median
from random import randint
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


def shell(array):
    """ Алгоритм сортировки массива методом Шелла"""
    n = len(array) // 2
    while n:
        for i, el in enumerate(array):
            while i >= n and array[i - n] > el:
                array[i] = array[i - n]
                i -= n
            array[i] = el
        n = 1 if n == 2 else int(n * 5.0 / 11)
    return array[len(array) // 2]


if __name__ == '__main__':
    m = int(input('Введите длину половинки массива: '))
    lst = [randint(0, 100) for _ in range(2 * m + 1)]

    median_shell = shell(lst[:])
    median_statistics = median(lst[:])

    print(f'Медиана, найденная путем сортировки Шелла: {median_shell}')
    print(f'Медиана, найденная функцией median(): {median_statistics}')
