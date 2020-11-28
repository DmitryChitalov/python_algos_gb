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
from memory_profiler import profile


class Matrix:
    def __init__(self, list_lists):
        self._list_lists = list_lists

    def __str__(self):
        str_list = ''
        for el in self._list_lists:
            for el_2 in el:
                str_list += f'{el_2}  '
            str_list += '\n'
        return str_list[:-1]

    def __add__(self, other):
        sum_mat = []
        x = 0
        while x < len(self._list_lists):
            sum_mat.append([])
            y = 0
            while y < len(self._list_lists[x]):
                sum_el = self._list_lists[x][y] + other._list_lists[x][y]
                sum_mat[x].append(sum_el)
                y += 1
            x += 1
        return Matrix(sum_mat)


@profile
def sum_string():
    sum_user = 0
    flag = True
    while flag:
        string = ' '.join([str(el) for el in range(10000)])
        list_string = string.split()
        list_string.append('&')
        for el in list_string:
            if flag:
                if el != '&':
                    sum_user += int(el)
                else:
                    flag = False
    else:
        return sum_user


@profile
def sum_matrix():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    matrix_a = Matrix(a)
    matrix_b = Matrix(b)
    print(matrix_a + matrix_b)


print(sum_string())
sum_matrix()
'''
Для этого задания взял из основ несколько заданий
'''
