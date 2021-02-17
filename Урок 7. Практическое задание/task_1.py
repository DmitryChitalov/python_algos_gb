

"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    origin_lst_obj = lst_obj[:]
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if origin_lst_obj == lst_obj:
            break
        n += 1
    return lst_obj


# # замеры 10
orig_list = [41, -80, 19, -41, 72, -40, 74, 94, -12, -77]
check_list = [-80, -77, -40, -41, -12, 19, 41, 72, 74, 94]

print(bubble_sort(orig_list))
(bubble_sort(check_list))
print(timeit.timeit("bubble_sort(orig_list[:])", globals=globals(), number=10000))  # 0.020
print(timeit.timeit("bubble_sort(check_list[:])", globals=globals(), number=10000))  # 0.016

# замеры 100
orig_list = [72, 42, -59, -78, 81, -60, -48, -27, -18, 90, 62, -12, -40, 53, -38, -25, -38, -20, 18, -31, 33, -16, -87, 82, -83, 21, 86, 22, 89, -56, -75, -96, -37, -77, 33, 13, 40, 81, -38, 81, -43, 69, 85, -73, -71, 18, -28, -66, -15, -65, 54, 83, 4, 42, -61, 82, -98, -56, -80, 75, 26, 51, 65, 60, 80, 50, -36, -95, 63, -44, 88, -18, 90, -9, -31, -16, -25, 96, 77, -22, 27, -97, -47, -62, -79, 89, -15, -13, 93, 88, -80, -67, 99, -49, -87, 46, 89, -77, 20, 9]
check_list = [-98, -97, -96, -95, -87, -87, -83, -80, -80, -78, -77, -77, -75, -73, 69, -71, -79, -67, -66, -65, -62, -61, -60, -59, -56, -56, -49, -48, -47, -44, -43, -40, -38, -38, -38, -37, -36, -31, -31, -28, -27, -25, -25, -22, -20, -18, -18, -16, -16, -15, -15, -13, -12, -9, 4, 9, 13, 18, 18, 20, 21, 22, 26, 27, 33, 33, 40, 42, 42, 46, 50, 51, 53, 54, 60, 62, 63, 65, 72, 75, 77, 80, 81, 81, 81, 82, 82, 83, 85, 86, 88, 88, 89, 89, 89, 90, 90, 93, 96, 99]

print(timeit.timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))  # 1.19
print(timeit.timeit("bubble_sort(check_list[:])", globals=globals(), number=1000))  # 0.65


# замеры 1000
orig_list = [75, 60, 94, -23, 50, -46, 8, -41, 20, 72, -24, 76, 95, 14, -32, 81, -14, -53, 11, 19, -44, -67, -30, -22, -93, 77, -29, 97, 95, -93, 31, 44, -55, 46, 8, -84, -88, 72, 68, 31, -58, -35, 18, 19, 31, -3, 59, -18, -34, 12, 23, -34, -55, -31, 93, -77, -51, 16, -57, -21, 16, -24, -95, 25, 62, 41, -92, -39, -22, 39, 63, 34, 5, 67, 49, -47, 91, 61, 23, 76, 59, -91, -93, 46, 99, -37, 68, -30, 57, -56, 1, 1, -64, -74, -78, -12, -75, 19, -67, -47, 2, -60, -51, -55, 40, 67, 84, 94, -68, -53, 77, 96, 51, -13, 14, -26, -93, 97, 73, 81, 91, -25, 33, -10, -88, -22, 0, -71, -61, 96, -18, 31, 8, -100, -73, 45, -74, 34, 83, -66, 4, 83, -81, -46, 16, 94, -5, -100, 79, -73, -58, -3, 63, 16, 86, 59, -48, -88, -45, 14, -95, 33, 75, -48, -67, 83, 91, -99, -79, 88, 96, 8, 71, 95, -94, 47, -96, 21, -62, 85, -87, 65, 89, 45, 2, 40, -89, 24, 55, -85, -59, -75, -95, -35, 4, 39, -83, 53, 16, 93, -47, -21, -53, -91, 98, -45, -95, -59, 58, 35, 76, -10, -76, 40, -57, -41, 17, -90, -75, 48, -74, -87, 73, 57, 41, 85, 85, -21, 23, 3, 42, 42, 10, 82, -2, 12, -65, 79, 51, -96, -15, -84, 53, 74, -100, 10, -18, 62, -31, 97, 52, -36, -1, 2, -33, 67, 22, -16, 29, -74, 5, -68, -62, 45, 81, -10, -44, -41, -34, -35, -19, 27, 32, -23, -49, 64, -5, 45, -30, -45, -39, -56, 12, -53, 40, -98, 90, 98, 72, 11, -41, 23, -39, -92, 1, -69, -16, 53, 72, -53, -72, -97, 52, 19, -78, 80, -69, -27, 30, 62, 80, 99, 93, -43, 47, -79, 92, -28, -49, 11, -54, 59, 5, 40, 60, 94, -64, -61, 55, 40, -93, -3, -44, 19, 59, 54, 43, -90, 90, 42, 68, -58, 35, -80, -15, -85, -35, 47, -86, -62, -75, -57, -37, 58, 43, -1, -2, -31, -100, -22, 26, 63, 89, -58, 55, -34, -40, 64, -4, -15, 18, -26, 27, -83, 7, 36, -78, -9, 41, 93, -50, -77, 32, 81, 52, -48, 81, 98, 100, 21, 53, -13, 26, -33, 20, -1, -34, 43, 67, 30, -9, -22, 36, -12, 45, 62, 29, 57, 55, 71, -66, 80, 50, -90, 58, 80, -83, -57, 78, -60, -31, -34, -10, 30, -73, -67, -46, 32, 18, 65, 66, -97, -40, -44, 77, 40, 19, 20, -13, 30, 26, 35, 9, -82, -36, 6, 9, -22, 28, -8, -14, 79, 86, -38, -16, 87, 20, 66, -16, -88, -13, 34, 50, -67, -7, 43, -18, -91, 64, -56, 99, -54, -42, 52, -83, -87, -28, -85, -46, -64, -13, 99, 60, 60, 68, 68, -18, -25, 86, 67, 12, 37, -45, 97, 98, -25, 86, -79, 99, 25, 80, 37, 97, 72, -39, 98, -82, 55, 87, -80, -66, 41, -69, -60, -96, -68, 26, -9, 23, -46, 73, -94, 90, 9, -29, 21, -51, -10, -63, -7, -44, 81, -52, 17, 88, -68, -89, -74, -32, 82, -56, -100, 32, -74, -17, -37, -89, 45, 34, -91, 10, -85, -83, 64, 24, -70, 23, 28, 58, -5, -48, 13, -28, 12, 23, 65, -81, 67, -96, -80, 92, 19, 86, 24, -79, -69, 14, 23, -19, -40, -9, -24, 69, 89, -13, -98, -11, 84, 75, -78, 48, 71, 11, -25, 51, 24, 13, -15, 78, 94, -46, 98, -24, -33, 68, -41, 37, -35, 29, -47, -53, 13, -32, -7, -58, -26, 96, -50, 81, 53, 56, 2, -56, -53, 20, 5, -40, 85, -31, -56, -93, 26, -99, -78, 73, -69, -24, -29, -37, 22, 99, -91, -17, -2, -27, -92, 22, 1, 46, -3, -10, -75, 64, 30, -87, -53, 46, 34, 55, -62, -78, 96, -81, -27, -32, -27, -88, 66, 44, 70, -86, -70, 2, 47, 75, 70, -6, 92, 78, 99, -18, -74, 47, 63, 28, 75, -34, -63, 83, 17, -84, 42, 88, -3, -78, -69, 75, 99, -69, -79, 42, 62, -90, 50, -74, -45, 12, 52, -44, -65, -1, 55, 56, -59, 91, -45, -83, 14, 9, 68, -36, -13, -53, 30, 42, 2, 100, 80, -24, -95, -67, 13, 79, -18, 81, 50, 27, -21, 21, 1, 50, 23, 11, -17, 29, -17, 70, -16, 48, 23, 51, -96, -18, 25, 95, 10, -98, 19, 18, -51, -8, 29, -85, -39, 57, -81, -41, -76, -38, -7, 49, -80, 70, -17, -69, 28, 61, -30, 51, -68, 54, 3, -31, 60, -52, 98, 66, -74, -73, 61, 25, -71, -46, -41, -7, 90, -100, -10, -11, -5, 96, 100, 95, -91, -43, 81, 57, 13, -45, 59, 34, -28, -17, -23, 46, 3, -14, -20, 98, 93, 12, -24, 24, 99, 91, 71, 47, -81, -36, -42, 48, -64, 11, -28, -52, -99, 100, 69, -91, -96, -73, -2, -55, -100, 87, 26, 73, -100, -48, -67, -33, 57, 74, -38, 89, 2, -44, 24, -94, 68, -37, 55, 95, 51, -18, 30, -27, -98, -23, 39, 37, 78, 62, -20, -28, -53, 37, 93, -13, 22, -84, -25, 39, 71, -60, -67, -100, -8, -54, 31, 95, -43, -37, -13, 21, 62, -47, 58, 80, -93, 67, 41, -11, -46, 63, -56, -8, -94, -84, 96, 30, -35, 41, -83, 73, -45, -54, 66, -68, 23, -42, -14, 38, 73, -65, 58, -42, 56, 36, 73, 100, -26, 48, 15, 76, -62, -60, -69, 41, -27, 26, -85, -8, 3, -90, -5, -18, 66, 71, -68, 75, 2, -8, 64, 55, 56, 57, 75, -10, -95, -16, -92, -89, -77, 3, -49, -73, -34, 41, -3, -94, 86, 14, 34, 19, -18, -83, -31, 83, 42, 66, 77, -93, 32, -16, 79, -44, 93, 46, -91, 85, -27, 22, 37, 75, -5, 67, 97, -87, -12]
check_list = [-100, -100, -100, -100, -100, -100, -100, -100,  -99, -100, -99, -99, -98, -98, -98, -98, -97, -97, -96, -96, -96, -96, -96, -96, -95, -95, -95, -95, -95, -95, -94, -94, -94, -94, -94, -93, -93, -93, -93, -93, -93, -93, -93, -92, -92, -92, -92, -91, -91, -91, -91, -91, -91, -91, -91, -90, -90, -90, -90, -90, -89, -89, -89, -89, -88, -88, -88, -88, -88, -87, -87, -87, -87, -87, -86, -86, -85, -85, -85, -85, -85, -85, -84, -84, -84, -84, -84, -83, -83, -83, -83, -83, -83, -83, -83, -82, -82, -81, -81, -81, -81, -81, -80, -80, -80, -80, -79, -79, -79, -79, -79, -78, -78, -78, -78, -78, -78, -78, -77, -77, -77, -76, -76, -75, -75, -75, -75, -75, -74, -74, -74, -74, -74, -74, -74, -74, -74, -73, -73, -73, -73, -73, -73, -72, -71, -71, -70, -70, -69, -69, -69, -69, -69, -69, -69, -69, -69, -68, -68, -68, -68, -68, -68, -68, -67, -67, -67, -67, -67, -67, -67, -67, -66, -66, -66, -65, -65, -65, -64, -64, -64, -64, -63, -63, -62, -62, -62, -62, -62, -61, -61, -60, -60, -60, -60, -60, -59, -59, -59, -58, -58, -58, -58, -58, -57, -57, -57, -57, -56, -56, -56, -56, -56, -56, -56, -55, -55, -55, -55, -54, -54, -54, -54, -53, -53, -53, -53, -53, -53, -53, -53, -53, -53, -52, -52, -52, -51, -51, -51, -51, -50, -50, -49, -49, -49, -48, -48, -48, -48, -48, -47, -47, -47, -47, -47, -46, -46, -46, -46, -46, -46, -46, -46, -45, -45, -45, -45, -45, -45, -45, -45, -44, -44, -44, -44, -44, -44, -44, -44, -43, -43, -43, -42, -42, -42, -42, -41, -41, -41, -41, -41, -41, -41, -40, -40, -40, -40, -39, -39, -39, -39, -39, -38, -38, -38, -37, -37, -37, -37, -37, -37, -36, -36, -36, -36, -35, -35, -35, -35, -35, -35, -34, -34, -34, -34, -34, -34, -34, -34, -33, -33, -33, -33, -32, -32, -32, -32, -31, -31, -31, -31, -31, -31, -31, -30, -30, -30, -30, -29, -29, -29, -28, -28, -28, -28, -28, -28, -27, -27, -27, -27, -27, -27, -27, -26, -26, -26, -26, -25, -25, -25, -25, -25, -24, -24, -24, -24, -24, -24, -24, -23, -23, -23, -23, -22, -22, -22, -22, -22, -22, -21, -21, -21, -21, -20, -20, -19, -19, -18, -18, -18, -18, -18, -18, -18, -18, -18, -18, -18, -17, -17, -17, -17, -17, -17, -16, -16, -16, -16, -16, -16, -16, -15, -15, -15, -15, -14, -14, -14, -14, -13, -13, -13, -13, -13, -13, -13, -13, -13, -12, -12, -12, -11, -11, -11, -10, -10, -10, -10, -10, -10, -10, -10, -9, -9, -9, -9, -8, -8, -8, -8, -8, -8, -7, -7, -7, -7, -7, -6, -5, -5, -5, -5, -5, -5, -4, -3, -3, -3, -3, -3, -3, -2, -2, -2, -2, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 16, 16, 16, 16, 16, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 33, 33, 34, 34, 34, 34, 34, 34, 34, 35, 35, 35, 36, 36, 36, 37, 37, 37, 37, 37, 37, 38, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 44, 44, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 49, 49, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53, 54, 54, 55, 55, 55, 55, 55, 55, 55, 55, 55, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 61, 61, 61, 62, 62, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 64, 65, 65, 65, 66, 66, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 68, 68, 68, 69, 69, 70, 70, 70, 70, 71, 71, 71, 71, 71, 71, 72, 72, 72, 72, 72, 73, 73, 73, 73, 73, 73, 73, 73, 74, 74, 75, 75, 75, 75, 75, 75, 75, 75, 75, 76, 76, 76, 76, 77, 77, 77, 77, 78, 78, 78, 78, 79, 79, 79, 79, 79, 80, 80, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 81, 81, 81, 81, 82, 82, 83, 83, 83, 83, 83, 84, 84, 85, 85, 85, 85, 85, 86, 86, 86, 86, 86, 86, 87, 87, 87, 88, 88, 88, 89, 89, 89, 89, 90, 90, 90, 90, 91, 91, 91, 91, 91, 92, 92, 92, 93, 93, 93, 93, 93, 93, 93, 94, 94, 94, 94, 94, 95, 95, 95, 95, 95, 95, 95, 96, 96, 96, 96, 96, 96, 96, 97, 97, 97, 97, 97, 97, 98, 98, 98, 98, 98, 98, 98, 98, 99, 99, 99, 99, 99, 99, 99, 99, 99, 100, 100, 100, 100, 100]
print(timeit.timeit("bubble_sort(orig_list[:])", globals=globals(), number=50))  # 6.097
print(timeit.timeit("bubble_sort(check_list[:])", globals=globals(), number=50))  # 3.294

"""
проверить формулу
"""
