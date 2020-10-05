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

from math import ceil

class Mystack:
    def __init__(self, max_stack):
        self.elems = []
        self.max_stack = max_stack

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
            self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        '''возвращает 2 значения: 1) количство стопок 2) количество тарелок в последней стопке'''
        return ceil((len(self.elems) / self.max_stack)), len(self.elems) % self.max_stack

if __name__ == '__main__':

    shelf = Mystack(9)

    print(shelf.is_empty())

    for i in range(1):
        shelf.push_in('Tarelka')

    print(shelf.is_empty())
    print(shelf.get_val())
    print(shelf.stack_size())
