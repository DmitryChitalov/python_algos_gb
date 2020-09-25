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
    def __init__(self, max_size):
        self.elem = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elem)

    def is_empty(self):
        return self.elem == [[]]

    def push_in(self, el):
        if len(self.elem[len(self.elem) - 1]) < self.max_size:
            self.elem[len(self.elem) - 1].append(el)
        else:
            self.elem.append([])
            self.elem[len(self.elem) - 1].append(el)

    def pop_out(self):
        result = self.elem[len(self.elem) - 1].pop()
        if len(self.elem[len(self.elem) - 1]) == 0:
            self.elem.pop()
        return result

    def get_val(self):
        return self.elem[len(self.elem) - 1][len(self.elem[len(self.elem) - 1]) - 1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.elem:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.elem)


plates = PlateStack(3)
plates.push_in('Plate1')
plates.push_in('Plate2')
plates.push_in('Plate3')
plates.push_in('Plate4')
plates.push_in('Plate5')
plates.push_in('Plate6')
print(plates)
print(plates.pop_out())
print(plates.get_val())
print(plates.stack_size())
print(plates.stack_count())
print(plates)
