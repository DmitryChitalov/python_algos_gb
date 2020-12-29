"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""


class Deck:
    def __init__(self, s):
        self.orig_s = s
        self.lst = [x for x in s.lower() if x.isalpha()]

    def push_to_start(self, elem):
        self.lst.insert(0, elem)

    def push_to_end(self, elem):
        self.lst.append(elem)

    def pop_from_start(self):
        return self.lst.pop(0)

    def pop_from_end(self):
        return self.lst.pop(-1)

    def size(self):
        return len(self.lst)

    def check(self):
        while self.size() > 1:
            if self.pop_from_end() != self.pop_from_start():
                print(f'"{self.orig_s}" не является палиндромом')
                return
        print(f'"{self.orig_s}" является палиндромом')


test_lst = [' sadfasf lkjh ee   oo ', 'Топота', 'Топот', 'Лёша на полке клопа нашёл', 'А роза упала на лапу Азора',
            'Аргентина манит негра', 'Я иду съ мечемъ судия', 'Я — арка края', 'О, лета тело!']
for st in test_lst:
    d = Deck(st)
    d.check()
