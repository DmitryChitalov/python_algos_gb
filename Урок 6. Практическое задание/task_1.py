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


import copy
from memory_profiler import profile
from sys import getrefcount


#  Найти сумму элементов следующего ряда чисел: 1  -0,5  0,25  -0,125  0,0625  ...
#  Количество элементов(n) вводится с клавиатуры

length = 900

#  До


@profile
def for_in(length_val):
    elem = 1
    amount = 0
    for i in range(length_val):
        amount += elem
        elem = -elem / 2
    print(f'Сумма последовательности из {length_val} элементов равна {amount}')


for_in(length)

#  После


@profile
def recursion(length):
    def sum_series_numbers(n, elem=1):
        if n <= 0:
            return 0
        return elem + sum_series_numbers(n-1, -elem / 2)
    print(
        f'Сумма последовательности из {length} элементов равна: '
        f'{sum_series_numbers(length)}'
    )


recursion(length)
"""


def recur_method(i, numb, n_count, common_sum):
    #  Рекурсия
    if i == n_count:
        print(f"Количество элементов - {n_count}, их сумма - {common_sum}")
    elif i < n_count:
        return recur_method(i + 1, numb / 2 * -1, n_count, common_sum + numb)


try:
    N_COUNT = int(input("Введите количество элементов: "))
    recur_method(0, 1, N_COUNT, 0)
except ValueError:
    print("Вы вместо числа ввели строку. Исправьте ошибку")
"""
