"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""

t = 'а роза упала на лапу азора'
t2 = 'молоко делили ледоколом'

# t = t.split()
# t = ''.join(t)
# print(len(t))
# t1 = t[:len(t)-1]
# t2 = t[-len(t)+1:]
# t2 = t2[::-1]
# print(t1 == t2)

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

def pal_checker(string):
    dc_obj = DequeClass()
    string_without_spaces = string.replace(' ', '')
    for el in string_without_spaces:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker('топот'))
print(pal_checker(t))
print(pal_checker(t2))