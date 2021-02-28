"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import random
import timeit


def bubble_sort_not_optimized(lst: list):
    for global_pass_index in range(1, len(lst)):
        for local_pass_index in range(len(lst) - global_pass_index):
            if lst[local_pass_index] < lst[local_pass_index + 1]:
                lst[local_pass_index], lst[local_pass_index + 1] = lst[local_pass_index + 1], lst[local_pass_index]
    return lst


def bubble_sort_optimized(lst: list):
    is_all_sorted = True
    for global_pass_index in range(1, len(lst)):
        for local_pass_index in range(len(lst) - global_pass_index):
            if lst[local_pass_index] < lst[local_pass_index + 1]:
                lst[local_pass_index], lst[local_pass_index + 1] = lst[local_pass_index + 1], lst[local_pass_index]
                if is_all_sorted:
                    is_all_sorted = False
        if is_all_sorted:  # значит уже всё отсортировано
            break
    return lst


list1 = [random.randint(-100, 100) for _ in range(1000)]
print(bubble_sort_not_optimized(list1.copy()))
print(bubble_sort_optimized(list1.copy()))


def test_time():
    print('list1.copy():',
          timeit.repeat("list1.copy()", globals=globals(), number=20, repeat=5))
    print('not_optimized:',
          timeit.repeat("bubble_sort_not_optimized(list1.copy())", globals=globals(), number=20, repeat=5))
    print('optimized:', timeit.repeat("bubble_sort_optimized(list1.copy())", globals=globals(), number=20, repeat=5))


test_time()
# not_optimized: [3.1908901000000003, 3.1159356999999996, 3.0828675000000008, 3.0988305, 3.249768500000002]
# optimized: [3.1646758000000013, 3.1735179000000002, 3.1759834, 3.0898353000000007, 3.1289866999999987]
'''
Вывод: на плохо отсортированных массивах оптимизация не заметна
'''

bubble_sort_optimized(list1)
test_time()
'''
Вывод: на отсортированных массивах оптимизация очень сильно заметна!
not_optimized: [1.5732861, 1.4530762, 1.4095705, 1.4813889000000007, 1.4542365999999998]
optimized: [0.0027989000000001596, 0.0028034999999997368, 0.0028034999999997368, 0.002803600000000017, 
            0.002963500000000785]
'''

list1[len(list1) - 1] = min(list1) - 1
list1[len(list1) - 2] = min(list1) - 2
test_time()
'''
list1.copy(): [8.609999999997786e-05, 8.189999999996811e-05, 8.149999999995661e-05, 8.149999999995661e-05, 
8.130000000006188e-05]
not_optimized: [1.6151873, 1.7183247000000001, 2.1346521000000003, 1.8589674, 1.6130014]
optimized: [1.5070309999999996, 1.5835235, 1.5767375000000001, 1.6152051000000007, 1.740965300000001]
'''
bubble_sort_optimized(list1)
list1[0] -= 1
list1[1] = list1[0] + 1
test_time()
'''
list1.copy(): [8.569999999963329e-05, 8.150000000028967e-05, 8.19000000014114e-05, 8.169999999907418e-05, 
8.229999999898041e-05]
not_optimized: [1.4977375999999971, 1.5109492000000024, 1.500036399999999, 1.504519000000002, 1.7172155999999994]
optimized: [1.8067917999999992, 1.850519600000002, 1.6995086000000015, 1.6663841999999995, 1.4794926999999944]
'''
