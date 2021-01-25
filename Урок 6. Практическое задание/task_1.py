"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import random
import timeit
import memory_profiler


def performance_dec(func):
    def wrapper(*args):
        start = timeit.default_timer()
        m_1 = memory_profiler.memory_usage()
        func(*args)
        m_2 = memory_profiler.memory_usage()
        end = timeit.default_timer()
        print(f'Время выполнения {func} - {end - start} секунд, использованная память {m_2[0] - m_1[0]} Mib')

    return wrapper


@performance_dec
def summ_list_1():
    lst_obj = [random.randint(0, 100) for _ in range(10000)]
    total_summ = 0
    for el in lst_obj:
        total_summ = total_summ + el
    return total_summ


@performance_dec
def summ_list_2():
    lst_obj = [random.randint(0, 100) for _ in range(10000)]
    return sum(lst_obj)


@performance_dec
def number_repeat_1():
    array = [random.randint(0, 100) for _ in range(10000)]
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@performance_dec
def number_repeat_2():
    array = [random.randint(0, 100) for _ in range(10000)]
    array_count = [array.count(el) for el in array]
    max_count = max(array_count)
    max_count_elem = array[array_count.index(max_count)]
    return f'Чаще всего встречается число {max_count_elem}, ' \
           f'оно появилось в массиве {max_count} раз(а)'


summ_list_1()
summ_list_2()

number_repeat_1()
number_repeat_2()

# Функция summ_list_2 быстрее summ_list_1 за счет использования встроенной функции sum(),
# при этом у обоих не наблюдается инкремента по памяти. Имеет место только оптимизация по времени.

# Функция number_repeat_1 имеет инкремент по памяти в 0.125 Mib и большее время относительно number_repeat_2, которая
# оптимизирована за счет генераторного выражения.

# Время выполнения <function summ_list_1 at 0x0152CE80> - 0.23940430000000001 секунд, использованная память 0.0 Mib
# Время выполнения <function summ_list_2 at 0x0152CF58> - 0.21701939999999997 секунд, использованная память 0.0 Mib
# Время выполнения <function number_repeat_1 at 0x038508E0> - 2.7446499 секунд, использованная память 0.125 Mib
# Время выполнения <function number_repeat_2 at 0x03850A48> - 2.7066743000000004 секунд, использованная память 0.0 Mib
