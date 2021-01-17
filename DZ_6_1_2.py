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
def func_gen():
    a = [randint(1, 100) for _ in range(300000)]
    res_even = [a[i] for i in range(1, len(a)) if a[i] % 2 == 0]
    res_odd = [a[i] for i in range(1, len(a)) if a[i] % 2 == 1]
    del a
    return res_even, res_odd


@profile
def func_app():
    b = [randint(1, 100) for _ in range(300000)]
    i = 0
    list_even = []
    list_odd = []
    while i < len(b):
        if b[i] % 2 == 0:
            list_even.append(b[i])
        else:
            list_odd.append(b[i])
        i += 1
    del b
    return list_even, list_odd


elapsed_func_gen = (timeit.timeit("func_gen()",
                                  setup="from __main__ import func_gen",
                                  number=1))
elapsed_func_app = (timeit.timeit("func_app()",
                                  setup="from __main__ import func_app",
                                  number=1))
print(elapsed_func_gen)
print(elapsed_func_app)

# В этом примере надо вычислить кол-во четных и нечетных чисел и поместить их в отдельный список
# У генератора кол-во вхождений практически 2 раза меньше соответственно и быстрее
