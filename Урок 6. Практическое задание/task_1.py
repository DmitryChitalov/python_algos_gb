"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from memory_profiler import profile
from timeit import timeit

from random import randint
from collections import Counter


# Результат замера времени выполнения при размере входного массива 1000000
# Время: 0.40545047500000003
#
# Результат профилирования:
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     45  17.29688 MiB  17.29688 MiB   @profile(precision=5)
#     46                             def most_common(array):
#     47  17.29688 MiB   0.00000 MiB       el = {}
#     48  17.34375 MiB   0.01562 MiB       for it in array:
#     49  17.34375 MiB   0.02344 MiB           el[it] = el.get(it, 0) + 1
#     50
#     51  17.24609 MiB   0.00000 MiB       res = 0
#     52  17.24609 MiB   0.00000 MiB       max_qty = 0
#     53  17.24609 MiB   0.00000 MiB       for key, val in el.items():
#     54  17.24609 MiB   0.00000 MiB           if max_qty < val:
#     55  17.24609 MiB   0.00000 MiB               max_qty = val
#     56  17.24609 MiB   0.00000 MiB               res = key
#     57
#     58  17.24609 MiB   0.00000 MiB       return res
# Итого затрачено: 0.04 MiB
#
@profile(precision=5)
def most_common(array):
    el = {}
    for it in array:
        el[it] = el.get(it, 0) + 1

    res = 0
    max_qty = 0
    for key, val in el.items():
        if max_qty < val:
            max_qty = val
            res = key

    return res


# Результат замера времени выполнения при размере входного массива 1000000
# Время: 0.151676139
#
# Результат профилирования:
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     39  13.85547 MiB  13.85547 MiB   @profile(precision=5)
#     40                             def most_common_fast(array):
#     41  13.85938 MiB   0.00391 MiB       return Counter(array).most_common(1)[0][0]
# Итого затрачено: 0.04 MiB
#
@profile(precision=5)
def most_common_fast(array):
    return Counter(array).most_common(1)[0][0]


# Вывод: оба алгоритма имеют сопоставимые затраты по памяти.
# По аремени выполнения встроенная структура данных имеет не значительное преимущество.
#
if __name__ == '__main__':
    rand_array = [randint(1, 10) for _ in range(0, 1000000)]

    print(f'Чаще всего встречается {most_common(rand_array)}')
    print(f'Чаще всего встречается {most_common_fast(rand_array)}')

    # print(
    #     timeit('most_common(rand_array)',
    #            'from __main__ import most_common, rand_array',
    #            number=100) / 100
    # )
    #
    # print(
    #     timeit('most_common_fast(rand_array)',
    #            'from __main__ import most_common_fast, rand_array',
    #            number=100) / 100
    # )
