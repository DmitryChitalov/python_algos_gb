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
import timeit
from memory_profiler import profile
import memory_profiler
from random import randint
from pympler import asizeof


def test_func(func):
    def wrapper():
        t1 = timeit.default_timer()
        m1 = memory_profiler.memory_usage()
        result = func()
        t2 = timeit.default_timer()
        m2 = memory_profiler.memory_usage()
        print(f'Время выполненя функции {func.__name__}: {t2 - t1}, использовано памяти: {m2[0] - m1[0]} MiB')
        return result
    return wrapper


@test_func
def find_min():  # Функциия до оптимизации
    lst = [i + randint(1, 1000) for i in range(100000)]
    min_el = lst[0]
    for i in range(len(lst) - 1):
        if min_el > lst[i]:
            min_el = lst[i]
    return f'Минимальное число: {min_el}'


@test_func
def find_min2():  # Функция после оптимизации
    lst = (i + randint(1, 1000) for i in range(100000))
    min_el = 1001
    for el in lst:
        if min_el > el:
            min_el = el
    del lst
    return f'Минимальное число: {min_el}'


print(find_min())
print(find_min2())


"""
Результаты анализа функции find_min() - до оптимизации
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     15.9 MiB     15.9 MiB           1   @profile
    29                                         def find_min():  # Поиск минимального значения списка
    30     18.6 MiB      2.7 MiB      100003       lst = [i + randint(1, 1000) for i in range(100000)]
    31     18.6 MiB      0.0 MiB           1       min_el = lst[0]
    32     18.6 MiB      0.0 MiB      100000       for i in range(len(lst) - 1):
    33     18.6 MiB      0.0 MiB       99999           if min_el > lst[i]:
    34     18.6 MiB      0.0 MiB           2               min_el = lst[i]
    35     18.6 MiB      0.0 MiB           1       return min_el


Python 3.8,  Windows x64   
результаты анализа памяти, показывают повышенный расход при формировании списка случайных чисел. 
Для оптимизации использованя памяти, предлагается заменить формирование списка с испольования генератора.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     15.9 MiB     15.9 MiB           1   @profile
    43                                         def find_min2():  # Поиск минимального значения списка
    44     15.9 MiB  -5768.1 MiB      200003       lst = (i + randint(1, 1000) for i in range(100000))
    45     15.9 MiB      0.0 MiB           1       min_el = 1001
    46     15.9 MiB  -2884.1 MiB      100001       for el in lst:
    47     15.9 MiB  -2884.0 MiB      100000           if min_el > el:
    48     15.9 MiB      0.0 MiB           4               min_el = el
    49     15.9 MiB     -0.0 MiB           1       del lst
    50     15.9 MiB      0.0 MiB           1       return f'Минимальное число: {min_el}'
    
Результаты после оптимизации кода, показывает сокращении использования памяти в случае использования генератора 
Вывод с применением созданного декоратора:
    Время выполненя функции find_min: 0.21875, использовано памяти: 0.0703125 MiB
    Минимальное число: 38
    Время выполненя функции find_min2: 0.203125, использовано памяти: 0.0 MiB
    Минимальное число: 12    
"""


class PilePlates:
    __slots__ = ('size', 'el', 'elems')

    def __init__(self, size):
        self.elems = [[]]
        self.size = size

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        count = len(self.elems) - 1
        if len(self.elems[count]) < self.size:
            self.elems[count].append(el)
        else:
            self.elems.append([])
            self.elems[count + 1].append(el)

    def pop_out(self):
        count = len(self.elems) - 1
        last_el = self.elems[count].pop()
        if len(self.elems[count]) == 0:
            self.elems.pop()
        return last_el

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


first = PilePlates(7)
print(f'Размер обьекта класса {PilePlates.__name__} составляет {asizeof.asizeof(first)}')
"""
Размер обьекта класса PilePlates составляет 232. Измеряем размер используемой памяти, обьектом.
Размер обьекта можно уменьшить за счет использования Слотов. 
Добавим следующую запись в наш класс: __slots__ = ('size', 'el', 'elems') - это позволит изменить способ 
хранения атрибутов с dict на tuple, что позволяет использовать меньше памяти
Размер обьекта класса PilePlates составляет 112
"""