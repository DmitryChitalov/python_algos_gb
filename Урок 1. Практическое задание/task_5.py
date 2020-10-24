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


class StackClass():

    def __init__(self):
        self.elems = [[]]
        self.active = 0  # активный стек

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[self.active]) == 5:  # В один стек входит пять тарелок
            self.elems.append([])
            self.active += 1
            self.elems[self.active].append(el)
        else:
            self.elems[self.active].append(el)

    def pop_out(self):
        return self.elems[self.active].pop()

    def get_val(self):
        return self.elems[self.active][len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def stack_el_size(self):
        return len(self.elems[self.active])


plate = StackClass()

plate.push_in('1 plate')
plate.push_in('2 plate')
plate.push_in('3 plate')
plate.push_in('4 plate')
plate.push_in('5 plate')
plate.push_in('6 plate')
plate.push_in('7 plate')
plate.push_in('8 plate')

print(plate.elems)

plate.pop_out()

print(plate.elems)

plate.push_in('9 plate')
plate.push_in('10 plate')

print(plate.elems)

plate.push_in('11 plate')
plate.push_in('12 plate')

print(plate.elems)
print(f'Всего тарелок в {plate.active + 1}-й стопке: {plate.stack_el_size()}')
print(f'Всего стопок: {plate.stack_size()}')
