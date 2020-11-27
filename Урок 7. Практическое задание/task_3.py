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



my_list = [random.randint(0, 40) for i in range(5)]


print(my_list)
print(median(my_list))


def my_median(any_list):
    my_set = set(my_list)
    avg = sum(my_set) / len(my_set)
    result_list = []

    for i in my_set:
        result_list.append(abs(avg - i))

    x = min(result_list)

    for i in my_set:
        if i == avg:
            result_list.remove(min(result_list))
            y = min(result_list)
            if (avg - y) in my_list:
                my_med = avg - y
            else:
                my_med = y - avg

        elif x == avg - i:
            my_med = i
        elif x == i - avg:
            my_med = i

    return my_med

print(my_median(my_list)) #Cначала мне казалось, что это сработает, но потом я поняла, что слишком много исключений


def my_median1(any_list):
    temprorary_copy = any_list
    for i in range(len(any_list) // 2):
        temprorary_copy.remove(min(temprorary_copy))
    return min(temprorary_copy)


print(my_median1(my_list))

