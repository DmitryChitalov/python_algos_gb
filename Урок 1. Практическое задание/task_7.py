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
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_to_front(self, element):
        self.items.append(element)

    def add_to_rare(self, element):
        self.items.insert(0, element)

    def remove_from_front(self):
        return self.items.pop()

    def remove_from_rear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)