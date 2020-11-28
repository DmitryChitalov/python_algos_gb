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
from random import randint


def get_left_and_right_list_median(in_list):
    left_list = []
    right_list = []
    med = median(in_list)
    for i in range(len(in_list)):
        if in_list[i] <= median(in_list):
            left_list.append(in_list[i])
        if in_list[i] >= median(in_list):
            right_list.append(in_list[i])

    return left_list, right_list, med


def main():
    pass
    try:
        print("gen list")
        rand_list = [randint(-100, 100) for _ in range(10)]
        left_of_median, right_of_median, med = get_left_and_right_list_median(rand_list)
        print(f"""in list: {rand_list}
Меньше медианы: {left_of_median}
Больше медианы: {right_of_median}
Медиана: {med}""")
        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()

"""
Думал зачем сортировать массив, так и не нашел зачем нужна сортировка. 
Т.к. это дополнительный проход по массиву, пользу от сортировки никакой. При всех алгоритмах, что мне пришли в голову 
действий было больше, а необходимость в переборе элементов сохранялась. Это как сортировка сначала в одном порядке, а 
потом в другом.

#########
gen list
in list: [-81, 52, -39, 12, -12, 76, -63, -55, 15, -89]
Меньше медианы: [-81, -39, -63, -55, -89]
Больше медианы: [52, 12, -12, 76, 15]
Медиана: -25.5

Программа завершена!

Process finished with exit code 0
"""