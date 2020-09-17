"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации этой структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class StackPlates:
    def __init__(self, max):
        self.elems = [[]]
        self.max = max

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def to_stack(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.max:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def from_stack(self):
        el = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return el

    def size(self):
        el_sum = 0
        for i in self.elems:
            el_sum += len(i)
        return el_sum


if __name__ == '__main__':
    my_plates = StackPlates(4)
    my_plates.to_stack('Plate1')
    my_plates.to_stack('Plate2')
    my_plates.to_stack('Plate3')
    my_plates.to_stack('Plate4')
    my_plates.to_stack('Plate5')
    my_plates.to_stack('Plate6')
    my_plates.to_stack('Plate7')
    print(my_plates)
    print(my_plates.size())
    my_plates.from_stack()
    my_plates.from_stack()
    print(my_plates)
    print(my_plates.size())

