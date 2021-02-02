"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import memory_profiler
from timeit import default_timer


def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        res_time = default_timer() - start_time
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff, res_time

    return wrapper


@decor
def list_append(n):
    new_list = []
    for i in range(n):
        new_list.append(i)
    return new_list


@decor
def dict_append(n):
    new_dict = {}
    for i in range(n):
        new_dict[i] = i
    return new_dict


if __name__ == '__main__':
    res, mem_diff, res_time = list_append(10000)
    print(f"Выполнение заняло {mem_diff} Mib")
    print(f"Выполнение заняло {res_time} sec")
    res1, mem_diff1, res_time1 = dict_append(10000)
    print(f"Выполнение заняло {mem_diff1} Mib")
    print(f"Выполнение заняло {res_time1} sec")

'''
Для списка:
Выполнение заняло 0.125 Mib
Выполнение заняло 0.1007515 sec
Для словаря:
Выполнение заняло 0.41796875 Mib
Выполнение заняло 0.10079670000000002 sec
Как здесь видно, использование словаря связано с дополнительными накладными расходами на поддержание хеша,
поэтому наполнение словаря и списка так отличается по памяти. Если памяти не хватает, то возможно стоит посмотреть
на использование списка. 
'''
