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


class PlateStack:
    def __init__(self, size_value):
        self.el = [[]]
        self.size_value = size_value

    def empty(self):
        return self.el == [[]]

    def push(self, el):
        if len(self.el[len(self.el) - 1]) < self.size_value:
            self.el[len(self.el) - 1].append(el)
        else:
            self.el.append([])
            self.el[len(self.el) - 1].append(el)

    def pop(self):
        res = self.el[len(self.el) - 1].pop()
        if len(self.el[len(self.el) - 1]) == 0:
            self.el.pop()
        return res

    def get_value(self):
        return self.el[len(self.el) - 1][len(self.el[len(self.el) - 1]) - 1]

    def size_of_stack(self):
        el_sum = 0
        for el in self.el:
            el_sum += len(el)
        return el_sum

    def __str__(self):
        return str(self.el)


if __name__ == '__main__':
    plate = PlateStack(4)
    plate.push('Plate one')
    plate.push('Plate two')
    plate.push('Plate three')
    print(plate)
    print(plate.pop())
    print(plate.get_value())
    print(plate.size_of_stack())
