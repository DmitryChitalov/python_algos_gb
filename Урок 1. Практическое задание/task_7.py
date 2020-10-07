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


def pal_checker(string, fix=False):
    dc_obj = DequeClass()

    # Удаление из строки пробелов, и перевод в нижний регистр
    if fix:
        string = string.replace(' ', '').lower()
    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


def fine_pal_checker(string, fix=False):
    print(f"\nСтрока{' (пофиксинная)' if fix else ''}: {string}\nЯвляется ли полиндромом? {pal_checker(string, fix)}", end="\n\n")


######################################
fine_pal_checker('топот')
fine_pal_checker('Топот')
fine_pal_checker('Топот', True)
fine_pal_checker('молоко делили ледоколом')
fine_pal_checker('Молоко делили ледоколом', True)
fine_pal_checker('молоко делили литрами')
