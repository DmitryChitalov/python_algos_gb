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


try:
    m = int(input("Введите число m для созадния массива длиной 2m + 1 : "))
except ValueError:
    print("Некорректный ввод")
    exit()

my_list = [randint(-50, 50) for _ in range(2*m+1)]
# my_list = [3, 9, 2, 6, 4, 8, 1]
# my_list = [3, 9, 2, 1, 4, 8, 6]  # вариант с граничными значениями
# my_list = [3, 1, 1, 1, 1, 8, 6]  # повторы
# my_list = [1, 7, 8, 3, 5, 6, 9]
print(my_list)


def median_search():
    median = my_list[m]
    left_idx = 0
    right_idx = 2 * m

    while left_idx < right_idx:
        print(my_list)

        if my_list[left_idx] < median:
            left_idx += 1
            continue
        if my_list[right_idx] > median:
            right_idx -= 1
            continue

        print(left_idx, right_idx, my_list.index(median))
        print(my_list[left_idx], my_list[right_idx], median)

        if my_list[left_idx] >= median & my_list[right_idx] <= median:
            if my_list[left_idx] == my_list[right_idx]:
                print(f"Медиана = {median}")
                break
            my_list[left_idx], my_list[right_idx] = my_list[right_idx], my_list[left_idx]
            left_idx += 1
            right_idx -= 1
            print("3", left_idx, right_idx, my_list.index(median))
            continue

        elif my_list[left_idx] > median & my_list[right_idx] > median:
            print("4", my_list[left_idx], my_list[right_idx], median)
            my_list.insert(0, my_list.pop(my_list.index(median)))

        elif my_list[left_idx] < median & my_list[right_idx] < median:
            print("5", my_list[left_idx], my_list[right_idx], median)
            my_list.append(my_list.pop(my_list.index(median)))

        median_search()

    else:
        if my_list.index(median) == m:    # если медиана не переместилась
            print(f"Нашли медиану! Медиана = {median}")
            print(my_list)
        else:
            median_search()


median_search()

print("Проверим результат воспользовавшись сортировкой:")
print(sorted(my_list)[m])

