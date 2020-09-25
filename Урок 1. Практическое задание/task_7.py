"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""


class Deque:
    def __init__(self):
        self.elem = []

    def is_empty(self):
        return self.elem == []

    def add_to_front(self, elem):
        self.elem.append(elem)

    def remove_from_rear(self):
        return self.elem.pop(0)

    def size(self):
        return len(self.elem)


def pal_checker(string):
    dc_obj = Deque()
    new_string = string.replace(' ', '')
    for el in new_string:
        dc_obj.add_to_front(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_rear()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker('молоко делили ледоколом'))
print(pal_checker('Молоко делили ледоколом'))
