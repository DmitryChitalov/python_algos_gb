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

from timeit import timeit
import random


def buble_funk(arr_obj):
    n = 1
    while n < len(arr_obj):
        for i in range(len(arr_obj)-n):
            if arr_obj[i] < arr_obj[i+1]:
                arr_obj[i], arr_obj[i+1] = arr_obj[i+1], arr_obj[i]
        n += 1
    return arr_obj


def bubble_funck_mod(arr_obj):
    n = 1
    flag_breakpoint = 0
    while n < len(arr_obj):
        for i in range(len(arr_obj)-n):
            if arr_obj[i] < arr_obj[i+1]:
                arr_obj[i], arr_obj[i+1] = arr_obj[i+1], arr_obj[i]
                flag_breakpoint = 1
        if flag_breakpoint == 0:
            break
        n += 1
    return arr_obj


if __name__ == '__main__':
    arr_obj_original_one = [random.randint(-100, 100) for _ in range(10)]
    arr_obj_original_two = [random.randint(-100, 100) for _ in range(10)]
    print(f'Оригинальный список: {arr_obj_original_one}')
    print(f'Результат сортировки функции buble_funk: \
{buble_funk(arr_obj_original_one)}\n')
    print(f'Оригинальный список: {arr_obj_original_two}')
    print(f'Результат сортировки функции buble_funk: \
{bubble_funck_mod(arr_obj_original_two)}')

    print('\nСкрипт профилировки buble_funk:')
    print(
        timeit(
            "buble_funk(arr_obj_original_one)",
            setup="from __main__ import buble_funk, arr_obj_original_one",
            number=100))
    print('\nСкрипт профилировки bubble_funck_mod:')
    print(
        timeit(
            "bubble_funck_mod(arr_obj_original_two)",
            setup="from __main__ import bubble_funck_mod, arr_obj_original_two",
            number=100))

"""
В качестве вывода ->
Оригинальный список: [100, -87, 35, -90, -5, 70, -91, 51, 64, 23]
Результат сортировки функции buble_funk:[100, 70, 64, 51, 35, 23, -5, -87, -90, -91]

Оригинальный список: [-69, -18, 51, 36, -27, 15, 83, -72, 55, 13]
Результат сортировки функции buble_funk: [83, 55, 51, 36, 15, 13, -18, -27, -69, -72]

Скрипт профилировки buble_funk:
0.0015046409998831223

Скрипт профилировки bubble_funck_mod:
0.00025248899964935845
________________________________________________________

Наблюдается незначительное оптимизация,
с учетом установки флага + маленькие вх. данные.
Вопрос => нужна-ли она при реальной работе?
Попробуем увеличить входящие данные до 1000:
Опишу только проф-ку:

Скрипт профилировки buble_funk:
4.778609343000426

Скрипт профилировки bubble_funck_mod:
0.016413667000051646

В данном случае очевидно, что флаг значительно сокращает время,
делая вариант сортировки "пузырьком" ->
конкурирующим с вариантами,
которые также были обозначены на уроке
"""
