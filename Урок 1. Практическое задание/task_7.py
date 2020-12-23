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
        self.all_el = []

    def add_begin(self, el):
        self.all_el.append(el)

    def add_end(self, el):
        self.all_el.insert(0, el)

    def remove_begin(self):
        return self.all_el.pop()

    def remove_end(self):
        return self.all_el.pop(0)

    def size(self):
        return len(self.all_el)


# функция очистки от пробелов
def make_clean_string(our_string):
    our_object = DequeClass()
    new_string = our_string.replace(' ', '').lower()

    for el in new_string:
        our_object.add_end(el)

    equal = True

    while our_object.size() > 1 and equal:
        first = our_object.remove_begin()
        last = our_object.remove_end()
        if first != last:
            equal = False

    return equal


print(make_clean_string('РвАл ДеД ЛаВр'))
print(make_clean_string('не палиндром'))