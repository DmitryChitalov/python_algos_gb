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
import random

@profile
def summ_er():
    print("Calculation started")
    size = random.randint(500000, 750000)
    print(size)
    test_line1 = [random.random() for i in range(size)]
    test_line2 = [random.randint(10, 100) for i in range(size)]
    test_line3 = [random.randint(10, 500) for i in range(size)]
    tline = [test_line1, test_line2, test_line3]
    result = 0
    for step in tline:
        for itr in step:
            result += itr
    print(f'Summ: {result}')

summ_er()

# Calculation started
# 596111
# Summ: 185055894.99877942
# Filename: /home/mrwindmark/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/task_1.py

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     19     17.5 MiB     17.5 MiB           1   @profile
#     20                                         def summ_er():
#     21     17.5 MiB      0.0 MiB           1       print("Calculation started")
#     22     17.5 MiB      0.0 MiB           1       size = random.randint(500000, 750000)
#     23     17.5 MiB      0.0 MiB           1       print(size)
#     24     40.5 MiB     23.0 MiB      596114       test_line1 = [random.random() for i in range(size)]
#     25     45.2 MiB      4.7 MiB      596114       test_line2 = [random.randint(10, 100) for i in range(size)]
#     26     59.0 MiB     13.7 MiB      596114       test_line3 = [random.randint(10, 500) for i in range(size)]
#     27     59.0 MiB      0.0 MiB           1       tline = [test_line1, test_line2, test_line3]
#     28     59.0 MiB      0.0 MiB           1       result = 0
#     29     59.0 MiB      0.0 MiB           4       for step in tline:
#     30     59.0 MiB      0.0 MiB     1788336           for itr in step:
#     31     59.0 MiB      0.0 MiB     1788333               result += itr
#     32     59.0 MiB      0.0 MiB           1       print(f'Summ: {result}')

"""
Анализ данного кода показывает:
- числа с плавающей запятой потребляют не меньше памяти, чем int значения
- размер переменной зависит от размера каждой переменной, а не числа элементов
- интерпретатор автоматически делает ссылки на объекты для оперирования и таким образом экономит ресурсы системы
- Очистку памяти лучше делать для объектов, хранящихся внутри функций и не использующихся в дальнейшем, т.к.
не ясно когда именно будет произведено автоматическое освобождение памяти
"""