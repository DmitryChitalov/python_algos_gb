# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.

from pympler import asizeof
from timeit import timeit


class Matrix:

    def __init__(self, matrix: list):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def __str__(self):
        result = []
        for elem in self.matrix:
            result.append(f'{" ".join([str(number) for number in elem])}')

        return '\n'.join(result)

    def __add__(self, other):
        if not self.rows == other.rows or not self.columns == other.columns:
            raise ValueError('Невозможно сложить матрицы, имеющие разную разрядность')
        else:
            result = []
            for idx_row in range(self.rows):
                result.append([self.matrix[idx_row][idx_col] + other.matrix[idx_row][idx_col]
                               for idx_col in range(self.columns)])

            return Matrix(result)


class MatrixRefactor:

    __slots__ = ['matrix', 'rows', 'columns']

    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def __str__(self):
        result = (f'{" ".join(map(str, elem))}' for elem in self.matrix)
        return '\n'.join(result)

    def __add__(self, other):
        if not self.rows == other.rows or not self.columns == other.columns:
            raise ValueError('Невозможно сложить матрицы, имеющие разную разрядность')
        else:
            result = [[self.matrix[idx_row][idx_col] + other.matrix[idx_row][idx_col]
                       for idx_col in range(self.columns)]
                      for idx_row in range(self.rows)]
            return MatrixRefactor(result)


test_lst_1 = [list(range(5)) for _ in range(5)]
test_lst_2 = [list(range(5, 10)) for _ in range(5)]


a = Matrix(test_lst_1)
print(f'\nПамять, занимаемая объектом: {asizeof.asizeof(a)}')
# Память, занимаемая объектом: 1104


b = MatrixRefactor(test_lst_2)
print(f'Память, занимаемая объектом: {asizeof.asizeof(b)}')
# Память, занимаемая объектом: 816

print('\nПеревод объекта в строковое представление:')
print(timeit('str(a)', globals=globals()))  # 4.4430457
print(timeit('str(b)', globals=globals()))  # 4.357287599999999

print('\nСложение объектов:')
print(timeit('a + a', globals=globals(), number=10000))  # 0.043921900000000846
print(timeit('b + b', globals=globals(), number=10000))  # 0.0423966999999994

# Для анализа памяти, занимаемой объектами класса использовалась функция asizeof,
# а для сравнения скорости выполнения операций с объектами - timeit.
# Замеры показывают, что в результате рефакторинга удалось несколько снизить затраты по памяти.
# Скорость выполнения операций снизилась несущественно, но всё же и здесь имеется небольщой прогресс.
# Для оптимизации по памяти была использована директива __slots__. Метод класса __str__ был переписан с использованием
# генератора и функции map, а метод __add__ - c использованием спискового включения.
# Теперь код стал меньше по объёму, методы класса работают чуть быстрее, а экземпляры класса занимают меньше памяти.
