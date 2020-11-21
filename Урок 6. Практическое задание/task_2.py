"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""


"""Мой вариант оптимизации памяти - применение мемоизации
Как видно из таблиц @profiler на рекурсии Фибоначчи числа 20:
без мемоизации число повторений Occurences - вычисления числа 10945 и 21892 раз 
А с применением мемоизации 19 и 22 соответвенно.
И хотя на данном примере Increment по памяти не увеличавается, в других задачах он может расти геометрически
Третий вариант представлен циклом for и имеет такое же количество 19 и 20

Вывод: благодаря мемоизации мы можем получить крассивое и аккуратное решение, а т.к. в коде мы можем применять 
 ее многократно к различным рекурсивным функциям - это помимо памяти будет экономить время и уменьшит кол-во строк
 
 Второй вариант касается генератора - вместо list использовать yield - в итоге @profile вообще никакой таблицы не 
 выводит (видимо я что-то неправильно замерил), но я так же использовал данные из этого генератора и объем памяти
 не увеличивался. 
 
 Вывод: генератор стоит использовать максимально во всех случаях, где это возможно, т.к. он не создает массив, а
  выдает слудующее значение по запросу."""

import memory_profiler
from timeit import default_timer
from memory_profiler import profile


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r

    return g


def time_memory(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func(*args)
        finish_time = default_timer()
        m2 = memory_profiler.memory_usage()
        time_diff = finish_time - start_time
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {time_diff} сек and {mem_diff} Mib")
        return res

    return wrapper


@profile
# @time_memory
def wrap(n):
    def f(n):
        if n < 2:
            return n
        return f(n - 1) + f(n - 2)

    return f(n)


wrap(20)


@profile
# @time_memory
def wrap(n):
    @memorize
    def f(n):
        if n < 2:
            return n
        return f(n - 1) + f(n - 2)

    return f(n)


wrap(20)


@profile
def f(n):
    if n < 2:
        return n
    pp = 0
    p = 1
    for i in range(n - 1):
        pp, p = p, pp + p
    return p


f(20)


@profile
# @time_memory
def simple_list():
    lst = list(range(1000000))
    return lst


simple_list()


@time_memory
def generator():
    for num in (range(1000000)):
        yield num


generator()
