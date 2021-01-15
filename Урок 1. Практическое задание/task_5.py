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
        self.elems = [[]]

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < 5:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
            self.elems[len(self.elems) - 1].pop()
        else:
            self.elems[len(self.elems) - 1].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


SC_OBJ = StackClass()

SC_OBJ.push_in(1)
SC_OBJ.push_in(2)
SC_OBJ.push_in(3)
SC_OBJ.push_in(4)
SC_OBJ.push_in(5)
SC_OBJ.push_in(6)
SC_OBJ.push_in(7)

print(SC_OBJ)

SC_OBJ.pop_out()
SC_OBJ.pop_out()
SC_OBJ.pop_out()

print(SC_OBJ)
