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

from numpy import array
from pympler import asizeof


class Matrix:
    __slots__ = array(['data'])

    def __init__(self, data):
        self.data = data

    def __str__(self):
        temp_str = '\n'
        for row in self.data:
            temp_str += '\t'.join([str(itm) for itm in row]) + '\n'
        return temp_str

    def __add__(self, other):
        if (len(self.data) is len(other.data)) and (len(self.data[0]) is len(other.data[0])):
            # First connect the two matrices together in tuples
            output_data = [list(zip(self.data[idx], other.data[idx])) for idx, itm in enumerate(self.data)]
            # Then sum each tuple
            output_data = [list(map(sum, row)) for row in output_data]
            return Matrix(output_data)
        TypeError('Matrices should be of the same length!')


# Old init
matrix_a = [[1, 2, 3],
            [5, 8, 1],
            [12, 3, 2]]

matrix_b = [[5, 21, 4],
            [6, 2, 43],
            [11, 12, 8]]

size_a_old = asizeof.asizeof(matrix_a)
size_b_old = asizeof.asizeof(matrix_b)

# New init
matrix_a = array([
    array([1, 2, 3]),
    array([5, 8, 1]),
    array([12, 3, 2])])

matrix_b = array([
    array([5, 21, 4]),
    array([6, 2, 43]),
    array([11, 12, 8])])

size_a_new = asizeof.asizeof(matrix_a)
size_b_new = asizeof.asizeof(matrix_b)

mat_a = Matrix(matrix_a)
mat_b = Matrix(matrix_b)

size_class = asizeof.asizeof(mat_a)

print(f'Matrix A: {mat_a}')
print(f'Matrix B: {mat_b}')

mat_c = mat_a + mat_b

print(f'Matrix C: {mat_c}')

print(f'Размер старого класса составил 392, нового {size_class}, '
      f'старая матрица А {size_a_old}, матрица B {size_b_old} '
      f'новая матрциа А {size_a_new}, матрица B {size_b_new} ')

# Размер старого класса составил 392, нового 216,
# старая матрица А 544, матрица B 640,
# новая матрциа А 168, матрица B 168

"""
По полученным результатам можно сделать вывод, что использование слотов и библиотеки numpy значительно уменьшают 
потребление памяти программой, т.к. для класса используются списки (к тому же из нумпая), а не словари и в кач-ве
матриц записаны не списки списков, а массивы массивов нумпая.

З.Ы. Конечно же в данной задаче в реальности бы просто использовался функционал нумпая по работе с матрицами, но в 
рамках урока задача вполне подходящая, помоему

Python 3.7, Windows 10 x64
"""
