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

from random import randint, sample
from timeit import timeit
import memory_profiler


def list_min_1(lst):
    min_num = lst[0]
    for i, el in enumerate(lst):
        for j in range(i + 1, len(lst)):
            num = list_min_2([lst[i], lst[j]])
            if num < min_num:
                min_num = num
    return min_num


def list_min_2(lst):
    min_num = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_num:
            min_num = lst[i]
    return min_num


def very_top(info_dict):
    """
    Это вспомогательная функция определения одного максимального элемента для функции top_v1
    T(n) = n*log(n) + 1*n
    """
    max_profit = max(info_dict.values())                # O(n*log(n))
    for el in info_dict:                                # O(n)
        if info_dict.get(el) == max_profit:             # O(1)
            return el


def top_v1(info_dict):
    """
    T(n) = 1 + n + 3*(n*log(n) + 1*n + 1 + 1) = 3*n*log(n) + 4n + 7
    """
    top3 = []                                           # O(1)
    info_dict_copy = info_dict.copy()                   # O(n)
    for i in range(3):                                  # O(3)
        cur_top = very_top(info_dict_copy)              # T(n) = n*log(n) + 1*n
        top3.append(cur_top)                            # O(1)
        info_dict_copy.pop(cur_top)                     # O(1)
    return top3


def top_v2(info_dict):
    """
    T(n) = 1 + n + n * (n*log(n) + n + 2) + 1 = 2 + n + n^2*log(n) + n^2 + 2n + 1 = (1+log(n))*n^2 + 3n + 3
    """
    min_profit_company = ''                             # O(1)
    info_dict_copy = info_dict.copy()                   # O(n)
    while len(info_dict_copy) > 3:                      # O(n)
        min_profit = min(info_dict_copy.values())       # O(n*log(n))
        for el in info_dict_copy:                       # O(n)
            if info_dict_copy.get(el) == min_profit:    # O(1)
                min_profit_company = el                 # O(1)
        info_dict_copy.pop(min_profit_company)          # O(1)
    return list(info_dict_copy.keys())


def main():

    m1 = memory_profiler.memory_usage()
    list_example = [randint(1, 9) for _ in range(5000)]
    print(list_min_1(list_example))

    m2 = memory_profiler.memory_usage()
    m_diff_1 = m2[0] - m1[0]

    m1 = memory_profiler.memory_usage()
    list_example_2 = [randint(1, 9) for _ in range(5000)]
    print(list_min_2(list_example_2))

    m2 = memory_profiler.memory_usage()
    m_diff_2 = m2[0] - m1[0]

    print(f'Вычисление минимума потребовало {m_diff_1} MiB в первом варианте и {m_diff_2} MiB во втором варианте')

    m1 = memory_profiler.memory_usage()
    print(top_v1(information_storage))
    m2 = memory_profiler.memory_usage()
    m_diff_1 = m2[0] - m1[0]

    m1 = memory_profiler.memory_usage()
    print(top_v2(information_storage))
    m2 = memory_profiler.memory_usage()
    m_diff_1 = m2[0] - m1[0]

    print(f'Вычисление топа потребовало {m_diff_1} MiB в первом варианте и {m_diff_2} MiB во втором варианте')


information_storage = {'MAIL.RU': 18690, 'Yandex': 12830, 'МТС': 54240, 'АФК Система': 65686, 'МГТС': 39730,
              'Наука-Связь': 0.27, 'Ростелеком': 14780, 'Таттелеком': 810.09, 'Центральный Телеграф': 2090}


main()

"""
1
1
Вычисление минимума потребовало 0.0 MiB в первом варианте и 0.0 MiB во втором варианте
['АФК Система', 'МТС', 'МГТС']
['МТС', 'АФК Система', 'МГТС']
Вычисление топа потребовало 0.0 MiB в первом варианте и 0.0 MiB во втором варианте

Те скрипты, которые мы делали, расходуют минимум памяти, поэтому профайлер почти всегда выдаёт ноли, лишь в отдельных
случаях какие-то цифры после запятой. Можно с этой целью в первых двух функциях (строки 82 и 89 увеличить range(),
но они тогда выполняются о-очень долго.
То есть можно сказать что все пока что написанные скрипты эффективно используют память.

Версия python 3.8.3
ОС 64-разрядная
"""
