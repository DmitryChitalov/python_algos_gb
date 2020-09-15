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
        self.polindrom = []     
    def is_empty(self):
        return self.polindrom == []     

    def add_to_front(self, el):
        self.polindrom.append(el)

    def add_to_rear(self, el):
        self.polindrom.insert(0, el)

    def remove_from_front(self):
        return self.polindrom.pop()

    def remove_from_rear(self):
        return self.polindrom.pop(0)

    def size(self):
        return len(self.polindrom)


def polind(string):
    dc_obj = DequeClass()

    for el in string.replace(' ', ''):
        dc_obj.add_to_rear(el)

    word = True

    while dc_obj.size() > 1 and wordl:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            word = False

    return word