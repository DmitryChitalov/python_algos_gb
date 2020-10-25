"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""


class Deque_Class:

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.is_empty == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def deque_size(self):
        return len(self.elems)


if __name__ == '__main__':
    def pal_check(string: str) -> bool:

        new_string = string.replace(' ', '')
        dc_obj = Deque_Class()

        for el in new_string:
            dc_obj.add_to_rear(el)

        still_equal = True

        while dc_obj.deque_size() > 1 and still_equal:
            first = dc_obj.remove_from_rear()
            second = dc_obj.remove_from_front()
            if first != second:
                still_equal = False

        return still_equal

    print(pal_check('молоко делили ледоколом'))
