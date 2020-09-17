"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""
class deque_class:
    def __init__(self):
        self.el = []

    def add_to_rear(self, el):
        self.el.insert(0, el)

    def remove_from_front(self):
        return self.el.pop()

    def remove_from_rear(self):
        return self.el.pop(0)

    def size(self):
        return len(self.el)


def check(string):
    dc_obj = deque_class()
    new_string = ''.join(string.split())  # Убираем все пробелы
    for el in new_string:
        dc_obj.add_to_rear(el)

    eq = True
    while dc_obj.size() > 1 and eq:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            eq = False
    return eq


print(check(' то п от'))