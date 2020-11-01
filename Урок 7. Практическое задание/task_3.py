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

from random import randint
from statistics import median


def my_median(lst):
    """
    Функция поиска медианы без использования сортировки

    :param lst: Массив чисел, из которых необходимо найти медиану
    :return: Возвращает медиану
    """
    c = len(lst) // 2
    i, m = 0, 0
    while i < len(lst):
        j, m = 0, lst[i]
        left, medium, right = [], [], []
        while j < len(lst):
            if j != i:
                if len(left) < c and lst[j] < m:
                    left.append(lst[j])
                elif len(right) < c and lst[j] > m:
                    right.append(lst[j])
                elif lst[j] == m:
                    medium.append(lst[j])
            j += 1
        if len(left) + len(medium) + len(right) == c * 2:
            break
        i += 1
    return m


def my_sort_shella(lst):
    """
    Функция сортировки списка по убыванию алгоритмом Шелла.
    Сам по себе алгоритм не дал однозначного результата, иногда появляляась ошибка,
    по-этому дополнен алгшоритмом пузырька.

    :param lst: Исходный список
    :return: Отсортированный список
    """
    step = (len(lst) * 3) // 4
    while step > 0:
        for i in range(len(lst) - 1):
            j = i + step
            if j > len(lst) - 1:
                break
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
        step = (step * 3) // 4
    n = 1
    while n < len(lst):
        changed = False
        for i in range(len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                changed = True
        if not changed:
            break
        n += 1
    return lst


###########################################
# Позиция медианы
source_m = 5

# Генерация массива
source_list = [randint(0, 10) for _ in range(source_m * 2 + 1)]
# Вывод исходного массива
print(source_list)

# Поиск медианы с помощью собственной функции
mediana_1 = my_median(source_list)
print(f"Медиана исходного массива my_median(): {mediana_1}")

# Поиск медианы с помощью встроенной функции
mediana_2 = median(source_list)
print(f"Медиана исходного массива median(): {mediana_2}")

# Сортировка списка алгоримом Шелла
sorted_list = my_sort_shella(source_list[:])
print(f"Список, сортированный алгоритмом Шелла, комбинированный Пузырьком:\n{sorted_list}")
print(f"Медиана сортированного списка: {sorted_list[source_m]}")

# Стандартная сортировка
source_list.sort()
print(source_list)

"""
Алгоритм сортировки Шелла реализовал, скомбинировав с алгоритмом Пузырька,
т.к. не удалось подобрать оптимальный шаг сдвига.  
"""
