"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import profile
from memory_profiler import memory_usage
import timeit


def work_with_indexes():
    array = [i for i in range(10000)]
    res = []
    if len(array) == 0:
        return 0
    for i in range(len(array)):
        if i % 2 == 0:
            res.append(array[i])
    return sum(res) * array[-1]


def work_with_indexes_time():
    array = [i for i in range(10000)]
    res = []
    if len(array) == 0:
        return 0
    for i in range(len(array)):
        if i % 2 == 0:
            res.append(array[i])
    return sum(res) * array[-1]


def work_with_indexes_2():
    array = [i for i in range(10000)]
    return sum(array[0::2]) * array[-1] if 0 < len(array) else 0


def work_with_indexes_2_time():
    array = [i for i in range(10000)]
    return sum(array[0::2]) * array[-1] if 0 < len(array) else 0


def work_with_indexes_3():
    array = [i for i in range(10000)]
    res = []
    if len(array) == 0:
        return 0
    for i in range(len(array)):
        if i % 2 == 0:
            res.append(array[i])
    yield sum(res) * array[-1]


def work_with_indexes_3_time_check():
    array = [i for i in range(10000)]
    res = []
    if len(array) == 0:
        return 0
    for i in range(len(array)):
        if i % 2 == 0:
            res.append(array[i])
    yield sum(res) * array[-1]


print(timeit.timeit("work_with_indexes_time()", setup="from __main__ import work_with_indexes_time", number=1000))
print(timeit.timeit("work_with_indexes_2_time()", setup="from __main__ import work_with_indexes_2_time", number=1000))
print(timeit.timeit("work_with_indexes_3_time_check()", setup="from __main__ import work_with_indexes_3_time_check",
                    number=1000))

work_with_indexes()
work_with_indexes_2()


def memory_check(func):
    m1 = memory_usage()
    func()
    m2 = memory_usage()
    return print(m2[0] - m1[0])


memory_check(work_with_indexes)
memory_check(work_with_indexes_2)
memory_check(work_with_indexes_3)

# вывод я исп вначале я сравнил 2 варианта решения задачи, один с помозью создания новго списка,
# второй при помощи list coprehansion и среза, результат был очевиден -
# первый вариант  очень сильно отличается по времени( в полтора раза медленне)
# однако этот малоэффектифный код превратился в очень быстрый, как только
# я поменял return на yield, это доказывет что генератор очень эффективен в использовании

