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


def bubble_sort_flag(lst_obj):
    sorted_flag = True
    while sorted_flag:
        sorted_flag = False
        for i in range(len(lst_obj)-1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                sorted_flag = True
    return lst_obj


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10000)]
print(f"исходный список - {orig_list}")
print(f"отсортированный список - {bubble_sort_flag(orig_list)}")
sorted_list = bubble_sort_flag(orig_list)
# замеры неотсортированного списка - 0.005
print('Время выполнения сортировки с флагом не сортированного списка - ', end='')
print(timeit.timeit("bubble_sort_flag(orig_list)", setup="from __main__ import bubble_sort_flag, orig_list", number=1))
# замеры отсортированного списка - 0.0076
print('Время выполнения сортировки с флагом сортированного списка - ', end='')
print(timeit.timeit("bubble_sort_flag(sorted_list)",
                    setup="from __main__ import bubble_sort_flag, sorted_list", number=1))

orig_list = [random.randint(-100, 100) for _ in range(10000)]
print(f"исходный список - {orig_list}")
print(f"отсортированный список - {bubble_sort(orig_list)}")
sorted_list = bubble_sort(orig_list)
# замеры неотсортированного списка - 5.45
print(f'Время выполнения сортировки без флага - '
      f'{timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1)}')

# замеры отсортированного списка - 5.51
print(f'Время выполнения сортировки без флага - '
      f'{timeit.timeit("bubble_sort(sorted_list)", setup="from __main__ import bubble_sort, sorted_list", number=1)}')

"""
Добавление флага существенно снижает время сортировки, это обусловлено тем, что если нет флага, то функция перебирает
весь список, не зависимо от того, отсортирован уже список или нет. С флагом, функция прекращает свою работу, если список
уже отсортирован. При этом если в функции передавать отсортированный список, то функция с флагом при этом работает еще
быстрее, но не значительно, потому что один проход по списку как минимум всегда есть. А функция без флага при этом не 
начинает работать быстрее, потому что она так же перебирает весь список.
"""