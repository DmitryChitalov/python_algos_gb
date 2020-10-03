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
Общие сведения: 
Python version 3.8.2
Mac OS Sierra 64bit
Так же код запускался на Windows 10x64
Отличия в замерах на разных платформах практически отсутствуют.
"""
from memory_profiler import profile
from collections import defaultdict
from functools import reduce


@profile
def test():
    loc_dict = defaultdict(list)
    num_1 = input('Введите первое значение: ').upper()
    num_2 = input('Введите второе значение: ').upper()
    loc_dict = num_1, num_2
    print(loc_dict)
    hex_int = [int(''.join(i), 16) for i in loc_dict]
    sum_ = sum(hex_int)
    mul = reduce(lambda x, y: x * y, hex_int)
    print(hex(sum_).upper()[2:])
    print(hex(mul).upper()[2:])


test()

"""
Пример 1:
В данном примере видим, что узких мест не наблюдается, выполняемый код потребляет минимальные 
ресурсы памяти.
Filename: C:/Users/AlexT/PycharmProjects/pythonProject2/test_1.py
Line #    Mem usage    Increment   Line Contents
================================================
     5     13.7 MiB     13.7 MiB   @profile
     6                             def test():
     7     13.7 MiB      0.0 MiB       loc_dict = defaultdict(list)
     8     13.7 MiB      0.0 MiB       num_1 = input('Введите первое значение: ').upper()
     9     13.7 MiB      0.0 MiB       num_2 = input('Введите второе значение: ').upper()
    10     13.7 MiB      0.0 MiB       loc_dict = num_1, num_2
    11     13.7 MiB      0.0 MiB       print(loc_dict)
    12     13.7 MiB      0.0 MiB       hex_int = [int(''.join(i), 16) for i in loc_dict]
    13     13.7 MiB      0.0 MiB       sum_ = sum(hex_int)
    14     13.7 MiB      0.0 MiB       mul = reduce(lambda x, y:  x * y, hex_int)
    15     13.7 MiB      0.0 MiB       print(hex(sum_).upper()[2:])
    16     13.7 MiB      0.0 MiB       print(hex(mul).upper()[2:])
"""

from memory_profiler import profile
import hashlib


@profile
def test():
    some_dict = set()
    string_txt = "papapapapapapapapapapapappapapapapapapapapappapapapapapapapapapapap"
    for x in range(len(string_txt)):
        for y in range(x, len(string_txt)):
            string_to_hash = hashlib.sha256(string_txt[x:y+1].encode())
            some_dict.add(string_to_hash.hexdigest())
    print(f'Result: string {string_txt} get {len(some_dict)} the same substrings')


test()
"""
Пример 2:
Повышенное потребление памяти выявлено в 11 строке, при работе с заполнение словаря.
Очевидно, что при заполнении словаря большими объемами данных, 11 строка будет одним из 
узких мест.Использовал циклы в надежде получить ощутимый прирост в потреблении ресурсов.

Line #    Mem usage    Increment   Line Contents
================================================
     4     14.1 MiB     14.1 MiB   @profile
     5                             def test():
     6     14.1 MiB      0.0 MiB       some_dict = set()
     7     14.1 MiB      0.0 MiB       string_txt = "papapapapapapapapapapapapapapapapapapapapapapappapapapapapapapapap"
     8     14.2 MiB      0.0 MiB       for x in range(len(string_txt)):
     9     14.2 MiB      0.0 MiB           for y in range(x, len(string_txt)):
    10     14.2 MiB      0.0 MiB               string_to_hash = hashlib.sha256(string_txt[x:y+1].encode())
    11     14.2 MiB      0.1 MiB               some_dict.add(string_to_hash.hexdigest())
    12     14.2 MiB      0.0 MiB       print(f'Result: string {string_txt} get {len(some_dict)} the same substrings')
"""