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
class Stack:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, elem):
        self.elems.append(elem)

    def pop_out(self):
        return self.elems.pop()

    def peek(self):
        return self.elems[len(self.elems)-1]

    def size(self):
        return len(self.elems)

    def __str__(self):
        return self.elems


if __name__=='__main__':

    def stacks_plates(num_p, max_p):
        stack_obj = Stack()
        stacks = []
        for p in range(num_p):
            if stack_obj.size() >= max_p:
                stacks.append(stack_obj)
                stack_obj = Stack()
            stack_obj.push_in(p)
        stacks.append(stack_obj)
        return stacks


s = stacks_plates(250, 10)
print(len(s))









