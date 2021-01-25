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
        func(*args)
        end = timeit.default_timer()
        m = memory_profiler.memory_usage()
        print(f'Время выполнения: {func} {end - start} секунд, использованная память {m[0]} Mib')
    return wrapper


@performance_dec
def min_value_1():
    lst_obj = [random.randint(0, 1000) for _ in range(1000)]
    min_el = lst_obj[0]
    for el in lst_obj:
        for i in lst_obj:
            if el < i and el < min_el:
                min_el = el
    return min_el


@performance_dec
def min_value_2():
    lst_obj_2 = [random.randint(0, 1000) for _ in range(1000)]
    min_el = lst_obj_2[0]
    for el in lst_obj_2:
        if el < min_el:
            min_el = el
    return min_el


@performance_dec
def number_repeat_1():
    array = [random.randint(0, 1000) for _ in range(1000)]
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
    array = [random.randint(0, 1000) for _ in range(1000)]
    array_count = [array.count(el) for el in array]
    max_count = max(array_count)
    max_count_elem = array[array_count.index(max_count)]
    return f'Чаще всего встречается число {max_count_elem}, ' \
           f'оно появилось в массиве {max_count} раз(а)'


min_value_1()
min_value_2()

number_repeat_1()
number_repeat_2()

# Время выполнения: <function min_value_1 at 0x0288CE80> 0.12094400000000005 секунд, использованная память 15.76171875 Mib
# Время выполнения: <function min_value_2 at 0x0288CF58> 0.0040168000000000426 секунд, использованная память 15.78515625 Mib
# Время выполнения: <function number_repeat_1 at 0x02D608E0> 0.057901699999999945 секунд, использованная память 15.78515625 Mib
# Время выполнения: <function number_repeat_2 at 0x02D60A48> 0.05960040000000011 секунд, использованная память 15.78515625 Mib

# Первая функция потребляет меньше памяти, Python 3.8.5, Win 64 bit
