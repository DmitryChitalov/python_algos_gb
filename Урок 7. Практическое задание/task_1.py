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
import timeit

'''
Резултат замеров:
2.651500000000473e-05
2.0527999999991886e-05

Если раскоментировать print он уже не даст таких результатов так-как после первой сортировки все последующии уже будут 
отсартированны.
Результат с раскоментированным print:
3.207299999999358e-05
1.9671999999998357e-05

Ввывод:
Умный пузырёк умнее=) Так-как он делает лишних итераций. Отсортировав список он выходит из цикла, и не тратит время 
на дополнительные итерации.
'''

l = [random.randint(-100, 100) for i in  range(10)]


def bubble_sort_fool(lst):
    n = 1
    while n < len(lst):
        for k in range(len(lst) - n):
            if lst[k] < lst[k+1]:
                lst[k], lst[k+1] = lst[k+1], lst[k]
        n += 1
    return lst


def bubble_sort_smart(lst):
    n = 1
    change_counter = 1
    while n < len(lst):
        for j in range(len(lst) - n):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                change_counter += 1
                if change_counter == j:
                    break
        n += 1
    return lst


print(f'До сортировки - {l}')
print(f'После сортировки - {bubble_sort_fool(l)}')

lst_obj = [random.randint(-100, 100) for _ in range(10)]

print(f'До сортировки - {lst_obj}')
print(f'После сортировки - {bubble_sort_smart(lst_obj)}')


print(timeit.timeit('bubble_sort_fool(l[:])', setup='from __main__ import bubble_sort_fool, l', number=1))

print(timeit.timeit('bubble_sort_smart(lst_obj[:])', setup='from __main__ import bubble_sort_smart, lst_obj', number=1))
