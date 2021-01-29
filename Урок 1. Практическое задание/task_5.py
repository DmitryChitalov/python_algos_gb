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


class StackClass:

    def __init__(self):
        self.elems = []
        self.stack = []
        self.stack.append(self.elems)

    def is_empty(self):
        return self.stack == [[]]

    def push_in(self, el):
        if len(self.elems) < 6:
            self.elems.append(el)
        else:
            self.elems = [el]
            self.stack.append(self.elems)

    def pop_out(self):
        if self.is_empty():
            res = 'Стэк уже пустой'
        elif self.elems != []:
            res = self.elems.pop()
        else:
            self.stack.pop()
            self.elems = self.stack[-1]
            res = self.elems.pop()
        return res

    def get_val(self):
        if self.is_empty():
            res = 'Стэк пустой'
        elif self.elems != []:
            res = self.elems[-1]
        else:
            res = self.stack[-2][-1]
        return res

    def stack_size(self):
        res = []
        for l in self.stack:
            res += l
        return len(res)



