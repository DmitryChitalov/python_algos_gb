"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""

from collections import deque

def pal_checker(string):
    dc_obj = deque(c for c in string if c != ' ')

    still_equal = True

    while len(dc_obj) > 1 and still_equal:
        first = dc_obj.popleft()
        last = dc_obj.pop()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))