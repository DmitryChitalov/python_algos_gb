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

import random
import copy
import timeit

#  функция bubble sort без доработки


def bubble_sort(input_list):
    input_list = copy.copy(input_list)
    for numb in range(len(input_list)-1, 0, -1):
        for i in range(numb):
            if input_list[i] < input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
    return input_list


#  функция bubble sort послe доработки


def bubble_sort_modified(input_list):
    input_list = copy.copy(input_list)
    for numb in range(len(input_list)-1, 0, -1):
        replacements = False
        for i in range(numb):
            if input_list[i] < input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                replacements = True  # здесь добавляем флаг наличия замен при очередном проходе
        if not replacements:
            return input_list  # ранний возврат отсортированного списка при отсутсвии замен при проходе
    return input_list


user_list = random.sample(range(-100, 100), 25)
print(f'изначальный список:                             {user_list}')
print()

sorted_list_1 = bubble_sort(user_list)
print(f'отсортированный по убыванию список (функция 1): {sorted_list_1}')
print(timeit.timeit("bubble_sort(user_list)", setup="from __main__ import bubble_sort, user_list", number=10000))

sorted_list_2 = bubble_sort_modified(user_list)
print(f'отсортированный по убыванию список (функция 2): {sorted_list_2}')
print(timeit.timeit("bubble_sort_modified(user_list)", setup="from __main__ import bubble_sort_modified, user_list",
                    number=10000))

'''
Результат теста по времени:
bubble_sort:          0.7866039
bubble_sort_modified: 0.5492596

Вторая функция выполняется обычно быстрее. Разница по скорости зависит от того, 
насколько случайно сгенерированный список изначально близок к отсортированному варианту. 
Чем изначальный список более упорядочен по убыванию, тем больше разрыв по времени.
'''