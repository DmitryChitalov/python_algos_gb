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


class StackCl:
    def __init__(self, max_stack_size):
        self.max_stack_size = max_stack_size
        self.full_stack = [[]]

    def is_empty(self):
        return self.full_stack == [[]]

    def push_in(self, el):
        #Предполагаем, что верхний элемент стека находится в конце списка
        if len(self.full_stack[-1]) <= self.max_stack_size:
            self.full_stack[-1].append(el)
        else:
            self.full_stack.append([el])

    def pop_out(self):
        if len(self.full_stack[-1]) == 1:
            del_var = self.full_stack.pop()
            if not self.full_stack:
                self.full_stack = [[]]
            return del_var
        else:
            return self.full_stack[-1].pop()

    def get_val(self):
        return self.full_stack[-1][-1]

    def size(self):
        num_of_stacks = len(self.full_stack)
        return num_of_stacks

    def __repr__(self):
        return self.full_stack

stack = StackCl(2)
stack.push_in(1)
stack.push_in(8)
stack.push_in(10)
stack.push_in(20)

print(stack.get_val())
print(stack.size())
stack.push_in(8)
print(stack.size())
stack.pop_out()
print(stack.size())
print(stack.full_stack)
