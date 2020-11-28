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

"""
OS: MacOS 10.13.6
PYTHON: 3.8
"""

from numpy import array
from mymodules import measurer
from pympler import asizeof

"""
Задача 1. Реализуем наполнение списка и считаем сумму всех элементов этого словаря.
"""


class SomeList:
    def __init__(self):
        self.some_list = []

    @measurer
    def list_generator(self, m):
        self.some_list = [i for i in range(m)]
        return self.some_list

    @measurer
    def sum_elem_list(self):
        result = 0
        for v in self.some_list:
            result += v
        return print(f'Сумма значений словаря = {result}')


list_1 = SomeList()
print(f'------ ЗАДАЧА 1 ------')
print(f'-- БАЗОВОЕ решение --')
list_1.list_generator(1000000)
list_1.sum_elem_list()
print()


class SomeListTwo:
    def __init__(self):
        self.some_list = []

    @measurer
    def list_generator(self, m):
        self.some_list = array([i for i in range(m)])
        return self.some_list

    @measurer
    def sum_elem_list(self):
        result = sum(self.some_list)
        return print(f'Сумма элементов списка = {result}')


list_2 = SomeListTwo()
print(f'-- ОПТИМИЗИРОВАННОЕ решение --')
list_2.list_generator(1000000)
list_2.sum_elem_list()
print()
print()
print()

"""
РЕЗУЛЬТАТ:

------ ЗАДАЧА 1 ------
-- БАЗОВОЕ решение --
Выполнение заняло 0.1705 сек и 31.14 Miб
Сумма значений словаря = 499999500000
Выполнение заняло 0.17136 сек и 7.371 Miб

-- ОПТИМИЗИРОВАННОЕ решение --
Выполнение заняло 0.28208 сек и 11.51 Miб
Сумма элементов списка = 499999500000
Выполнение заняло 0.35438 сек и 0.003906 Miб

ВЫВОД:
 
В оптимизированном решении было примененно array из NumPy, а также встроенная фуркция sum. Оптимизированное 
решение получилось уменьшить прилично по потреблению памяти, но по времени оно заняло
примерно в два раза больше времени... Как получить оптимизацию по времени и памяти, пока не дошло.
Вариант решения должен выбираться исходя из задачи, если важна скорость, то оптимизируем скорость работы,
если важно потребление памяти, то соответственно оптимизируем потребление памяти.
"""

"""
Задача 2. Приведен код ниже, позволяет сохранить в массиве индексы четных элементов другого массива.
"""


class ArrOperations:
    def __init__(self):
        self.lst = []
        self.new_lst = []

    @measurer
    def arr_generator(self, n):
        self.lst = [el for el in range(n)]
        return self.lst

    @measurer
    def arr_algo(self):
        for el in range(len(self.lst)):
            if self.lst[el] % 2 == 0:
                self.new_lst.append(el)
        return self.new_lst


print(f'------ ЗАДАЧА 2 ------')
print(f'-- БАЗОВОЕ решение --')
item_1 = ArrOperations()
item_1.arr_generator(100000)
item_1.arr_algo()
print(asizeof.asizeof(item_1))
print()


class ArrOperationsTwo:
    def __init__(self):
        self.lst = []
        self.new_lst = []

    @measurer
    def arr_generator_two(self, n):
        self.lst = array([el for el in range(n)])
        return self.lst

    @measurer
    def arr_algo_two(self):
        self.new_lst = self.lst[::2]
        return self.new_lst


print(f'-- ОПТИМИЗИРОВАННОЕ решение --')
item_2 = ArrOperationsTwo()
item_2.arr_generator_two(100000)
item_2.arr_algo_two()
print(asizeof.asizeof(item_2))

"""
РЕЗУЛЬТАТ:

------ ЗАДАЧА 2 ------
-- БАЗОВОЕ решение --
Выполнение заняло 0.10919 сек и 0.3125 Miб
Выполнение заняло 0.12604 сек и 1.398 Miб
6027072

-- ОПТИМИЗИРОВАННОЕ решение --
Выполнение заняло 0.12417 сек и 0.9766 Miб
Выполнение заняло 0.10261 сек и 0.0 Miб
800472

ВЫВОД: 

В оптимизированном решение был применен array из NumPy, а так же в методе arr_algo_two срез вместо перебора.
Что мы в итоге получили по этой задаче:
- по времени: время выполнения примерно одинаково
- по потреблению памяти: при формировании массива, даже больше тратится чем в БАЗОВОМ решении, а при формировании 
второго массива ОПТИМИЗИРОВАННОЕ выйграло
- но если мы посмотрим на итоговый размер экземпляров, то увидим, что ОПТИМИЗИРОВАННЫЙ экземпляр занимает минимум
в 6 раз меньше места.
Поэтому я выбираю ОПТИМИЗИРОВАННОЕ решение!
"""
