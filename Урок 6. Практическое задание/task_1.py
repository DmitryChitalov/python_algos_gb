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

# В примере испоьзована оптимизация класса через __slots__. В теории должно меньше заанимать места, но
# по факту показывает одни знаения. Возможно это связано с малым колличеством объектов.
from memory_profiler import profile


class MyClass:
    def __init__(self, my_matrix):
        self.matrix = my_matrix
        self.matrix_2 = []

    def __str__(self):
        return str(self.matrix)

    def __add__(self, other):
        i = 0
        for el in self.matrix:
            i_2 = 0
            numbers = []
            for el_2 in el:
                i_3 = 0
                numbers_2 = []
                for el_3 in el_2:
                    el_4 = el_3 + other.matrix[i][i_2][i_3]
                    numbers_2.append(el_4)
                    i_3 += 1
                numbers.append(numbers_2)
                i_2 += 1
            self.matrix_2.append(numbers)
            i += 1
        return self.matrix_2


matrix = [
    [
        [31, 22],
        [37, 43],
        [51, 86],
    ],
    [
        [3, 5, 32],
        [2, 4, 6],
        [-1, 64, -8],
    ],
    [
        [3, 5, 8, 3],
        [8, 3, 7, 1],
    ]
]

matrix_2 = [
    [
        [31, 22],
        [37, 43],
        [51, 86],
    ],
    [
        [3, 5, 32],
        [2, 4, 6],
        [-1, 64, -8],
    ],
    [
        [3, 5, 8, 3],
        [8, 3, 7, 1],
    ]
]


@profile
def my_func():
    a = MyClass(matrix)
    print(a)
    b = MyClass(matrix_2)
    print(a + b)


my_func()


# Вариант №2
class MyClass2:

    __slots__ = ('matrix', 'matrix_2')

    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_2 = []

    def __str__(self):
        return str(self.matrix)

    def __add__(self, other):
        i = 0
        for el in self.matrix:
            i_2 = 0
            numbers = []
            for el_2 in el:
                i_3 = 0
                numbers_2 = []
                for el_3 in el_2:
                    el_4 = el_3 + other.matrix[i][i_2][i_3]
                    numbers_2.append(el_4)
                    i_3 += 1
                numbers.append(numbers_2)
                i_2 += 1
            self.matrix_2.append(numbers)
            i += 1
        return self.matrix_2


matrix_3 = [
    [
        [31, 22],
        [37, 43],
        [51, 86],
    ],
    [
        [3, 5, 32],
        [2, 4, 6],
        [-1, 64, -8],
    ],
    [
        [3, 5, 8, 3],
        [8, 3, 7, 1],
    ]
]

matrix_4 = [
    [
        [31, 22],
        [37, 43],
        [51, 86],
    ],
    [
        [3, 5, 32],
        [2, 4, 6],
        [-1, 64, -8],
    ],
    [
        [3, 5, 8, 3],
        [8, 3, 7, 1],
    ]
]


@profile
def my_func_2():
    a = MyClass2(matrix_3)
    print(a)
    b = MyClass2(matrix_4)
    print(a + b)


my_func_2()
