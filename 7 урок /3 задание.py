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
import timeit
import random
from statistics import median

def bubble_sort_median(sort_lst):
    print(f'Изначальный список: {sort_lst}')
    n = 1
    count = 0
    while n < len(sort_lst):
        for i in range(len(sort_lst)-n):
            if sort_lst[i] < sort_lst[i+1]:
                sort_lst[i], sort_lst[i+1] = sort_lst[i+1], sort_lst[i]
                count += 1
        if count == 0:
            break
        n += 1
    print(f'Отсортированный список: {sort_lst}')
    print(f'Медина: {sort_lst[len(sort_lst)//2]}')
    return

def shell_sort(lst):
    inc = len(lst) // 2
    while inc:
        for i, el in enumerate(lst):
            while i >= inc and lst[i - inc] > el:
                lst[i] = lst[i - inc]
                i -= inc
            lst[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
 #   print(f'Медина: {lst[len(lst) // 2]}')
    return

def my_sort(lst):
    n = 0
    while n < len(lst):
        more = []
        equally = []
        less = []
        for i in lst:
            if lst[n] < i:
                more.append(i)
            elif lst[n] > i:
                less.append(i)
            else:
                equally.append(i)
        if len(more) == len(less) :
 #           print(f'Медиана: {lst[n]}')
            break
        n += 1
    return

def built_in_method(lst):
#    print(f'Медиана: {median(lst)}')
    return median(lst)


lst = [random.randint(-100, 100) for _ in range(11)]
print(f'Время затраченое на поиск медианы с помощью сортировки пузырьком: {timeit.timeit("bubble_sort_median(lst[:])", setup="from __main__ import bubble_sort_median, lst", number=100)}')
print(f'Время затраченое на поиск медианы с помощью сортировки методом Шелла: {timeit.timeit("shell_sort(lst[:])", setup="from __main__ import shell_sort, lst", number=100)}')
print(f'Время затраченое на поиск медианы без сортировки: {timeit.timeit("my_sort(lst[:])", setup="from __main__ import my_sort, lst", number=1)}')
print(f'Время затраченое на поиск медианы встроенным методом: {timeit.timeit("built_in_method(lst[:])", setup="from __main__ import built_in_method, lst", number=100)}')
"""
Запуск первый:
Время затраченое на поиск медианы с помощью сортировки пузырьком: 0.0053975340000000024
Время затраченое на поиск медианы с помощью сортировки методом Шелла: 0.0012786800000000043
Время затраченое на поиск медианы без сортировки: 1.1024999999997842e-05
Время затраченое на поиск медианы встроенным методом: 8.144699999999838e-05

Запиуск второй:
Время затраченое на поиск медианы с помощью сортировки пузырьком: 0.004328684999999999
Время затраченое на поиск медианы с помощью сортировки методом Шелла: 0.0013575580000000018
Время затраченое на поиск медианы без сортировки: 8.214200000000033e-05
Время затраченое на поиск медианы встроенным методом: 0.0002068989999999965

Замер третий:
Время затраченое на поиск медианы с помощью сортировки пузырьком: 0.006638113000000001
Время затраченое на поиск медианы с помощью сортировки методом Шелла: 0.0017621949999999942
Время затраченое на поиск медианы без сортировки: 2.3346000000000477e-05
Время затраченое на поиск медианы встроенным методом: 9.786200000000411e-05

По статистике самые быстрые методы нахождения медианы - это сортировка пузырьком и метод Шелла.
    
"""