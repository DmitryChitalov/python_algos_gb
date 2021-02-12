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


def find_median(lst, k):
    """
    Ищем медиану через рекурсию. При первом запуске k ставим половине списка, в нашем случае N
    """

    # Если в списке один элемент, то он и будет медианой
    if len(lst) == 1:
        return lst[0]

    middle = lst[len(lst) // 2]

    left_lst = [el for el in lst if el < middle]
    right_lst = [el for el in lst if el > middle]
    middle_lst = [el for el in lst if el == middle]

    # Если в левом списке больше чисел, то запускаем для него еще раз поиск
    if k < len(left_lst):
        return find_median(left_lst, k)
    # Если k больше длины left_lst, но меньше длинны left_lst и middle_lst, то в middle_lst будет медиана
    elif k < len(left_lst) + len(middle_lst):
        return middle_lst[0]
    # Иначе запускаем поиск по правой части
    else:
        return find_median(right_lst, k - len(left_lst) - len(middle_lst))


N=10

my_list = [randint(0, 100) for i in range(2*N + 1)]

print(my_list)
print(f"Медиана через рекурсию = {find_median(my_list, N)}")
my_list.sort()
print(f"Медиана на основе сортировки = {my_list[N]}")
