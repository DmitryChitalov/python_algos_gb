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


class StackCup:
    def __init__(self):
        self.max_elems = 3
        self.current_stack = 0
        self.elems = []
        self.elems.append([])

    def is_empty(self):
        return self.elems[0] == []

    def push_in(self, el):
        if len(self.elems[self.current_stack]) < self.max_elems:
            self.elems[self.current_stack].append(el)
        else:
            self.current_stack += 1
            self.elems.append([])
            self.elems[self.current_stack].append(el)

    def pop_out(self):
        el = self.elems[self.current_stack].pop()
        if self.elems[self.current_stack] == [] and self.current_stack != 0:
            self.current_stack -= 1
            self.elems.pop()
        return el

    def get_val(self):
        return self.elems[self.current_stack][len(self.elems[self.current_stack]) - 1]

    def stack_size(self):
        length = 0
        for el in self.elems:
            length += len(el)
        return length


if __name__ == '__main__':
    SC_OBJ = StackCup()
    print(SC_OBJ.is_empty())
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    print(SC_OBJ.is_empty())
    SC_OBJ.push_in(5.5)
    print(SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(SC_OBJ.elems)
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.pop_out()
    print(SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(SC_OBJ.elems)
    SC_OBJ.pop_out()
    print(SC_OBJ.elems)
    SC_OBJ.pop_out()
