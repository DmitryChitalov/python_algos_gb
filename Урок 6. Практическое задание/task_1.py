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
from collections import deque
from distutils.util import get_platform

print(f'Используемая OC - {get_platform()}')

@profile()
def func(N):
    list = [random.randint(1, 100000) for _ in range(N)]
    deque_1 = deque([random.randint(1, 100000) for _ in range(N)])
    for el in range(1, len(list)):
        list[el] = list[el]*random.randint(0, 2)
    total = sum(list)
    for el in range(1, len(deque_1)):
        deque_1[el] = deque_1[el]*random.randint(0, 2)
    total_2 = sum(deque_1)
    maximum = max(total, total_2)
    del list
    del deque_1
    return maximum


N = 100000

if __name__ == '__main__':
    func(N)


'''

Python 3.8 
OC macosx-10.9-x86_64

Для запуска программы было выделено 13.3 MiB
Для создания списка list выделено еще 6.4 MiB
Для изменения значений элементов по очереди в списке list выделено еще 3.8 MiB
Удаление ссылки на список и дек командой del осовбодили память до 11.8 MiB


 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     13.3 MiB     13.3 MiB           1   @profile()
    36                                         def func(N):
    37     19.6 MiB      6.4 MiB      100003       list = [random.randint(1, 100000) for _ in range(N)]
    38     21.2 MiB -517356.8 MiB      100003       deque_1 = deque([random.randint(1, 100000) for _ in range(N)])
    39     16.7 MiB     -8.3 MiB      100000       for el in range(1, len(list)):
    40     16.7 MiB      3.8 MiB       99999           list[el] = list[el]*random.randint(0, 2)
    41     16.7 MiB      0.0 MiB           1       total = sum(list)
    42     16.7 MiB      0.0 MiB      100000       for el in range(1, len(deque_1)):
    43     16.7 MiB      0.0 MiB       99999           deque_1[el] = deque_1[el]*random.randint(0, 2)
    44     16.7 MiB      0.0 MiB           1       total_2 = sum(deque_1)
    45     16.7 MiB      0.0 MiB           1       maximum = max(total, total_2)
    46     16.4 MiB     -0.3 MiB           1       del list
    47     11.8 MiB     -4.6 MiB           1       del deque_1
    48     11.8 MiB      0.0 MiB           1       return maximum

'''
