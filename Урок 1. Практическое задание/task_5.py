"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class Teller:
    def __init__(self, teller_size):
        self.teller_size = teller_size
        self.elems = []

    def __str__(self):
        return str(self.elems)

    def stack_clear(self):
        return self.elems == [[]]

    def insert_teller(self, plate):
        plate_count = 0
        try:
            if len(self.elems[-1]) == self.teller_size:
                self.elems.append([])
            for elem in self.elems:
                if len(elem) < self.teller_size:
                    self.elems[plate_count].append(plate)
                else:
                    plate_count += 1
                    continue
        except IndexError:
            self.elems.append([])
            self.elems[plate_count].append(plate)

    def stack_count(self):
        return len(self.elems)

x = Teller(3)

x.insert_teller('plate')
x.insert_teller('plate2')
x.insert_teller('plate3')
x.insert_teller('plate4')
x.insert_teller('plate5')
print(x)
print('Кол-во стоек: ' + str(x.stack_count()))