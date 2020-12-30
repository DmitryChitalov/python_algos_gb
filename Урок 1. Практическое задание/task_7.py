"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""

# Ну, я пыталась..((
# Сделала три варианта, первый работает не правильно, вторые 2 совсем не работают, покажу хотя бы это..

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

    def get_first(self):
        return self.elems[0]

    def get_last(self):
        return self.elems[-1]


def pal_checker(string):
    dc_obj = DequeClass()

    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        """Вариант 1"""
        # if dc_obj.get_first() == ' ':
        #     dc_obj.remove_from_front()
        # if dc_obj.get_last() == ' ':
        #     dc_obj.remove_from_rear()
        # first = dc_obj.remove_from_front()
        # last = dc_obj.remove_from_rear()
        """Вариант 2"""
        # first = ' '
        # last = ' '
        # while first == ' ':
        #     first = dc_obj.remove_from_front()
        # while last == ' ':
        #     last = dc_obj.remove_from_rear()
        """Вариант 3"""
        first = dc_obj.remove_from_front()
        if first == ' ':
            first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if last == ' ':
            last = dc_obj.remove_from_rear()

        if first != last:
            still_equal = False

    return still_equal


print(pal_checker('топот'))
print(pal_checker('леша на полке клопа нашел'))
print(pal_checker("но невидим архангел мороз узором лег на храм и дивен он"))
