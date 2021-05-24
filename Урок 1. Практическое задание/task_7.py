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


# палиндром

def pal_checker(string):
    deq_object = DequeClass()

    for letter in string:
        if letter != " ":
            deq_object.add_to_rear(letter)

    still_equal = True

    while deq_object.size() > 1 and still_equal:
        first = deq_object.remove_from_front()
        last = deq_object.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))
