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
import memory_profiler
from timeit import default_timer
from memory_profiler import profile
import sys


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


class Matrix:
    def __init__(self):
        self.list = []
        self.new_list = []

    def __add__(self, matrix_data):
        self.list.append(matrix_data)

    def addition(self):
        if len(self.list) > 1:
            data_1 = self.list[0]
            data_2 = self.list[1]
            for i in range(len(matrix_1)):
                total = [x + y for x, y in zip(data_1[i], data_2[i])]
                self.new_list.append(total)
            return self.new_list

    def __str__(self):
        self.addition()
        if self.new_list:
            print('Сумма матриц: ')
            return '\n'.join(map(str, self.new_list))
        else:
            for q_of_matrix in range(len(self.list)):
                return '\n'.join(map(str, self.list[q_of_matrix]))


matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]


@profile
def matrix():
    matrix = Matrix()
    matrix + matrix_1
    print(matrix)  # если одна матрица - печатаем ее
    matrix + matrix_2
    print(matrix)  # если две матрицы - печатаем сумму матриц


matrix()

del matrix_1
del matrix_2
print(sys.getrefcount('matrix_1'))
print(sys.getrefcount('matrix_2'))

"""Первая задача - сумма матриц из курса основ. 
Как видно из таблицы - она оптимизирована по памяти, хотя тут так же сказывается малое количество данных.
Так же применил del, но получить число 0 или 1 не получилось, видимо ссылки показывают на задачу в другой папке."""

number = 12345678912345678911234645846514


@profile
def wrap(n):
    def recursive_reverse(number):
        if number == 0:
            return str(number % 10)
        return f'{str(number % 10)}{recursive_reverse(number // 10)}'

    return recursive_reverse(n)


wrap(number)


@profile
def reverse_by_join(number):
    reversed_number = [''.join(i for i in str(number)[::-1])]
    return reversed_number


reverse_by_join(number)


@profile
def reverse_by_slice(number):
    reversed_number = str(number)[::-1]
    return reversed_number


reverse_by_slice(number)

"""Второй задачей выбрал разворот числа из курса алгоритмизации.
Опять же в таблицах мы не видим инкремента памяти, но отлично видно большое число Occurences в решении через
 рекурсию и join, а вот решение через срез проходит всего один цикл.
Вариант решения через мемоизацию рассмотрел во второй задаче, поэтому здесь его не рассматриваю, но мемоизация - это
одно из лучших решений. В данном случае лучше только срез.

Вывод по итогам рассмотрерия данных задач сделал о том, что на некоторых малых данных инкремента памяти может и 
 не происходить, в таком случае смотрим на Occurences и время выполнения программы."""
