"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

дПримечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Селать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import timeit
from memory_profiler import profile
from random import randint


@profile
def built_in():
    rand_list = [str(randint(1, 10)) for _ in range(100000)]
    return rand_list[::-1]


@profile
def reverse():
    rand_list = [str(randint(1, 10)) for _ in range(100000)]
    rand_list.reverse()
    return rand_list


@profile
def cycle():
    rand_list = [str(randint(1, 10)) for _ in range(100000)]
    new_items = []
    for i in range(len(rand_list), 0, -1):
        new_items.append(rand_list[i - 1])
    del rand_list
    return new_items


elapsed_built_in = (timeit.timeit("built_in()",
                                  setup="from __main__ import built_in",
                                  number=1))
elapsed_reverse = (timeit.timeit("reverse()",
                                 setup="from __main__ import reverse",
                                 number=1))
elapsed_cycle = (timeit.timeit("cycle()",
                               setup="from __main__ import cycle",
                               number=1))

print(elapsed_built_in)
print(elapsed_reverse)
print(elapsed_cycle)

# Reverse работает чуть чуть быстрее, и занимает чуть чуть меньше памяти, но это возможно погрешность profile
# Что касается цикла, то естественно он медленнее встроенных функций и занимает больше памяти.
