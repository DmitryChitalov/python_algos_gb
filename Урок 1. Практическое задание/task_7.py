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
    string = string.replace(' ', '')  # удаляем пробелы
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


true_polynomial_word = "топот"
true_polynomial_sentence = "молоко делили ледоколом"
false_polynomial_word = "топот!!!"
false_polynomial_sentence = "молоко делили ледоколом!!!"

print(f'"{true_polynomial_word}" это полином? {pal_checker(true_polynomial_word)}')
print(f'"{true_polynomial_sentence}" это полином? {pal_checker(true_polynomial_sentence)}')
print(f'"{false_polynomial_word}" это полином? {pal_checker(false_polynomial_word)}')
print(f'"{false_polynomial_sentence}" это полином? {pal_checker(false_polynomial_sentence)}')
