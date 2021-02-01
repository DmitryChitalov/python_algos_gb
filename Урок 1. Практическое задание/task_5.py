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


class PlateStacks:
    def __init__(self, size_limit):
        if size_limit <= 0:
            raise ValueError('size_limit should be greater than zero')
        self.stacks = []
        self.size_limit = size_limit

    def add_new_stack(self):
        new_stack = []
        self.stacks.append(new_stack)
        return new_stack

    def get_cur_stack(self):
        return None if self.is_empty() else self.stacks[-1]

    def is_empty(self):
        return self.stacks == []

    def push_in(self, plate):
        cur_stack = self.get_cur_stack()
        if not cur_stack:
            cur_stack = self.add_new_stack()
        elif len(cur_stack) == self.size_limit:
            cur_stack = self.add_new_stack()

        cur_stack.append(plate)

    def pop_out(self):
        cur_stack = self.get_cur_stack()
        if not cur_stack:
            print('Nothing to pop')
            return

        top_plate = cur_stack.pop()
        if not cur_stack:
            self.stacks.remove(cur_stack)
        return top_plate

    def get_val(self):
        cur_stack = self.get_cur_stack()
        if not cur_stack:
            print('No plates in stacks')
            return
        else:
            return cur_stack[-1]

    def stack_size(self):
        if self.is_empty():
            return 0
        else:
            return (len(self.stacks) - 1) * self.size_limit + len(self.get_cur_stack())


ps = PlateStacks(2)
ps.pop_out()
print(ps.get_val())
print(ps.stack_size())
ps.push_in('Plate1')
ps.push_in('Plate2')
ps.push_in('Plate3')
print(ps.get_val())
print(ps.stack_size())
ps.push_in('Plate4')
ps.pop_out()
ps.pop_out()
ps.pop_out()
ps.pop_out()
print(ps.get_val())
print(ps.stack_size())
