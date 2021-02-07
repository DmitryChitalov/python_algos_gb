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

"""
from statistics import median
import random
from timeit import timeit

m = int(input(' Задайте положительное натуральное число m,\
nКоличество элементов массива строится по формуле 2m + 1: '))

random_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]



""" Сортировка Шелла (Shell sort, Shellsort),  ~ O(n)
Сортируем вставкой подгруппы элементов, но только в подгруппе они идут не в ряд, а равномерно выбираются с
некоторой дельтой по индексу. После первоначальных грубых проходов, дельта методично уменьшается, пока расстояние
между элементами этих несвязных подмножеств не достигнет единицы. Благодаря первоначальным проходам с большим шагом,
большинство малых по значению элементов перебрасываются в левую часть массива, большинство крупных элементов массива
попадают в правую.
 """

def shell_sort(input_list):
    n = 1
    last_index = len(input_list) - 1
    step = len(input_list) // 2
    while step > 0:
        for i in range (step, last_index + 1):
            j = i
            difference = j - step
            while difference >= 0 and input_list[difference] > input_list[j]:
                input_list[difference], input_list[j] = input_list[j], input_list[difference]
                j = difference
                difference = j - step
        step //= 2
        n += 1
    return input_list, f'Median: {input_list[len(input_list)//2]} , ' \
                       f'This list has been sorted for {n} iterations'

"""	Гномья сортировка (Gnome sort), ~ O(n2)
В  гномьей сортировке происходит просмотр массива слева-направо, при этом сравниваются (и меняются,
если это неотсортированная пара) соседние элементы. Если происходит обмен элементов, то проиходит возвращение на один
шаг назад. Если обменов не происходит, то алгоритм продолжает просмотр массива слева-направо в поиске
неотсортированных пар. """

def gnome(input_list):
    n = 1
    i = 1
    size = len(input_list)
    while i < size:
        if input_list[i - 1] <= input_list[i]:
            i += 1
        else:
            input_list[i - 1], input_list[i] = input_list[i], input_list[i - 1]
            if i > 1:
                i -= 1
        n += 1
    return input_list, f'Median: {input_list[m]} , '\
                       f'This list has been sorted for {n} iterations'



"""Алгоритм поиска медианы без сортировки, ~ O(n2) Принцип работы: По очереди берем элементы из списка, 
назначая медиане это значение, наполняем массивы( в левый то, что меньше медианы, в правый то, что больше. Далее 
сравниваем длины левого и правого списка, если они не равны, очищаем списки, присваиваем медиане следующее значение и 
т.д """

def get_median(input_list):
    unsorted_list = input_list
    n = 1
    left_side = []
    right_side = []
    for i in range(len(unsorted_list[:])):
        for j in range(len(unsorted_list[:])):
            if unsorted_list[i] < unsorted_list[j]:
                right_side.append(unsorted_list[j])
            if unsorted_list[i] > unsorted_list[j]:
                left_side.append(unsorted_list[j])
            if unsorted_list[i] == unsorted_list[j] and i < j:
                right_side.append(unsorted_list[j])
            if unsorted_list[i] == unsorted_list[j] and i > j:
                left_side.append(unsorted_list[j])
        if len(left_side) != len(right_side):
            left_side = []
            right_side = []
            n += i*j
        else:
            return f' Median: {unsorted_list[i]}, Left side: {left_side},  Right side : {right_side}',\
                   f' {n} iterations'


print(random_list)
print(shell_sort(random_list))
print(gnome(random_list))
print(get_median(random_list))
print(median(random_list))

print(timeit("shell_sort(random_list[:])", globals=globals(), number=1000))
print(timeit("gnome(random_list[:])", globals=globals(), number=1000))
print(timeit("get_median(random_list[:])", globals=globals(), number=1000))
print(timeit("median(random_list[:])", globals=globals(), number=1000))

"""
m = 5

[-16, 0, -22, -51, 86, -48, -99, -69, 75, 70, 37]
([-99, -69, -51, -48, -22, -16, 0, 37, 70, 75, 86], 'Median: -16 , This list has been sorted for 4 iterations')
([-99, -69, -51, -48, -22, -16, 0, 37, 70, 75, 86], 'Median: -16 , This list has been sorted for 11 iterations')
(' Median: -16, Left side: [-99, -69, -51, -48, -22],  Right side : [0, 37, 70, 75, 86]', ' 6 iterations')
-16
0.007309700000000002
0.0034004000000000117
0.05156000000000001
0.0007700999999999958

m = 100

0.2520527, 8 iterations
0.0547724,  201 iterations
13.7178887 , 990001 iterations
0.0031247000000007574

Выводы: алгоритмы с сортировками значительно быстрее по времени, 
Для разных задач применимы разные виды сортировки, у каких то больше быстродействие, какие то оптимизированы под
использование ресусов памяти, в данной задаче лучший результат поиска медианы показала встроенная функция median.
"""
