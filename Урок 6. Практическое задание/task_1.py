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
import itertools
from random import randint

from memory_profiler import profile


class Data:
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]


class Teacher:
    def __init__(self):
        self.work = 0

    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)


@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    c = [3] * (2 * (5 ** 7) * 5)
    d = [4] * ((2 * 5) ** 7 * 5)
    del b
    del d
    return a


@profile
def XOR_cipher(string, key):
    answer = []
    key = itertools.cycle(key)  # Повторяем ключ, чтобы зашифровать всю строку

    for s, k in zip(string, key):
        answer.append(chr(ord(s) ^ ord(k)))

    return ''.join(answer)


@profile
def bubble_sort():
    N = 10
    a = []
    for i in range(N):
        a.append(randint(1, 99))
    print(a)

    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print(a)


@profile
def oop_test():
    lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
    marIvanna = Teacher()
    ivanVasilch = Teacher()
    vasy = Pupil()
    marIvanna.teach(vasy)
    ivanVasilch.teach("Math", vasy, vasy)
    del marIvanna


if __name__ == '__main__':
    my_func()
    """Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    49     13.1 MiB     13.1 MiB           1   @profile
    50                                         def my_func():
    51     20.7 MiB      7.6 MiB           1       a = [1] * (10 ** 6)
    52    173.3 MiB    152.6 MiB           1       b = [2] * (2 * 10 ** 7)
    53    179.2 MiB      6.0 MiB           1       c = [3] * (2 * (5 ** 7) * 5)
    54    560.7 MiB    381.5 MiB           1       d = [4] * ((2 * 5) ** 7 * 5)
    55    408.1 MiB   -152.6 MiB           1       del b
    56     26.6 MiB   -381.5 MiB           1       del d
    57     26.6 MiB      0.0 MiB           1       return a
"""
    print("- " * 50)
    XOR_cipher("test-test-test", "5")
    """Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    60     26.7 MiB     26.7 MiB           1   @profile
    61                                         def XOR_cipher(string, key):
    62     26.7 MiB      0.0 MiB           1       answer = []
    63     26.7 MiB      0.0 MiB           1       key = itertools.cycle(key)  # Повторяем ключ, чтобы зашифровать всю строку
    64                                         
    65     26.7 MiB      0.0 MiB          15       for s, k in zip(string, key):
    66     26.7 MiB      0.0 MiB          14           answer.append(chr(ord(s) ^ ord(k)))
    67                                         
    68     26.7 MiB      0.0 MiB           1       return ''.join(answer)
"""
    print("- " * 50)
    bubble_sort()
    """
    Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    71     26.7 MiB     26.7 MiB           1   @profile
    72                                         def bubble_sort():
    73     26.7 MiB      0.0 MiB           1       N = 10
    74     26.7 MiB      0.0 MiB           1       a = []
    75     26.7 MiB      0.0 MiB          11       for i in range(N):
    76     26.7 MiB      0.0 MiB          10           a.append(randint(1, 99))
    77     26.7 MiB      0.0 MiB           1       print(a)
    78                                         
    79     26.7 MiB      0.0 MiB          10       for i in range(N - 1):
    80     26.7 MiB      0.0 MiB          54           for j in range(N - i - 1):
    81     26.7 MiB      0.0 MiB          45               if a[j] > a[j + 1]:
    82     26.7 MiB      0.0 MiB          18                   a[j], a[j + 1] = a[j + 1], a[j]
    83                                         
    84     26.7 MiB      0.0 MiB           1       print(a)

    """
    print("- " * 50)
    oop_test()
"""Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    87     26.7 MiB     26.7 MiB           1   @profile
    88                                         def oop_test():
    89     26.7 MiB      0.0 MiB           1       lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
    90     26.7 MiB      0.0 MiB           1       marIvanna = Teacher()
    91     26.7 MiB      0.0 MiB           1       ivanVasilch = Teacher()
    92     26.7 MiB      0.0 MiB           1       vasy = Pupil()
    93     26.7 MiB      0.0 MiB           1       marIvanna.teach(vasy)
    94     26.7 MiB      0.0 MiB           1       ivanVasilch.teach("Math", vasy, vasy)
    95     26.7 MiB      0.0 MiB           1       del marIvanna
"""
print("- " * 60)
"""
    python3.7 (x64) 
    ---------------
    
    Возможно, я выбрал не очень показательные примеры. То что я вижу: увеличение использования памяти 
    заметно только при работе с листом (я думаю что и со справочником будет тоже самое)
    
    В случае, если инициализация была выполнена разово, то память уже не течет (это можно видеть на сортировке и
    на кодировании)
    
    В случае работы с циклами - 
    растет количество вхождений "Occurences" - что может говорить о замедлении по времени выполнения.
    
    А вот при работе с классами (ооп), для меня немного странно: при создании экземпляра объекта - память не растет(!)
    Почему? Видимо что-то не правильно сделал.

"""
