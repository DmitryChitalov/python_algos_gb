"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""


class DequeClass:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def add_to_front(self, elem):
        self.elements.append(elem)

    def add_to_rear(self, elem):
        self.elements.insert(0, elem)

    def remove_from_front(self):
        return self.elements.pop()

    def remove_from_rear(self):
        return self.elements.pop(0)

    def size(self):
        return len(self.elements)


def pal_checker(string):
    string = ''.join(string.split()).lower()  # доработка, заодно и для случая с буквами в верхнем регистре
    dc_obj = DequeClass()

    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


if __name__ == '__main__':
    print(pal_checker('молоко делили ледоколом'))
    print(pal_checker('А роза упала на лапу Азора'))
    print(pal_checker('топот'))
    print(pal_checker('пароход'))
