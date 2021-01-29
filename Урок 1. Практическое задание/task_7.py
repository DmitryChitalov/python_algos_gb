"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""


class DequeClass:

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, el):
        self.elems.append(el)

    def remove_from_front(self):
        return self.elems.pop()

    def add_to_rear(self, el):
        self.elems.insert(0, el)

    def remove_from_rear(self):
        return self.elems.pop(0)

    def get_front_val(self):
        return self.elems[-1]

    def get_rear_val(self):
        return self.elems[0]

    def print_deque(self):
        print(self.elems)

    def remove_spaces(self):
        for el in self.elems:
            if el == ' ':
                self.elems.remove(el)

    def size(self):
        return len(self.elems)