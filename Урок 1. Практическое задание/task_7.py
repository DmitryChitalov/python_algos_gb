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

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


def is_palindrom(string):
    __deque = DequeClass()
    new_string = string.strip().lower()
    for el in new_string:
        if el.isalpha():
            __deque.add_to_rear(el)

    while __deque.size() > 1:
        first = __deque.remove_from_front()
        last = __deque.remove_from_rear()
        if first != last:
            return False
    return True

print(is_palindrom('Там холм лохмат'))
print(is_palindrom('Уверена я, а не реву'))