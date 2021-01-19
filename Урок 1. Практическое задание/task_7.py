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
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def add_to_back(self, el):
        self.elements.append(el)

    def remove_from_back(self):
        return self.elements.pop()

    def add_to_head(self, el):
        self.elements.insert(0, el)

    def remove_from_head(self):
        return self.elements.pop(0)

    def size(self):
        return len(self.elements)


def check_str(string):
    dc_obj = DequeClass()
    my_string = string.replace(' ', '')

    for el in my_string:
        dc_obj.add_to_back(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_head()
        last = dc_obj.remove_from_back()
        if first != last:
            still_equal = False
    return still_equal


print(check_str("молоко делили ледоколом"))
print(check_str("молоко делил ледоколом"))
