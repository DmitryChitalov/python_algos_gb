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

"""К имеющемуся коду добавил ограничение высоты стопки тарелок и добавление новых списков - стопок
Добавил методы для просмотра общего количества стопок и просмотра всех стопок"""


class StackClass:
    def __init__(self):
        self.stack = 0
        self.elems = [[]]

    def is_empty(self):
        return self.elems[self.stack] == []

    def push_in(self, el):
        if len(self.elems[self.stack]) < 2:  # указываем высоты стопки тарелок
            self.elems[self.stack].append(el)
        else:
            self.stack += 1
            self.elems.append([])
            self.elems[self.stack].append(el)

    def pop_out(self):
        return self.elems[self.stack].pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems[self.stack])

    def stack_quantity(self):
        return len(self.elems)

    def view_stacks(self):
        return self.elems


SC_OBJ = StackClass()
print(SC_OBJ.is_empty())  # -> стек пустой
SC_OBJ.push_in(10)
SC_OBJ.push_in('code')
SC_OBJ.push_in(False)
SC_OBJ.push_in(5.5)
print(SC_OBJ.get_val())
print(SC_OBJ.stack_size())
print(SC_OBJ.is_empty())
SC_OBJ.push_in(4.4)
print(SC_OBJ.pop_out())
print(SC_OBJ.stack_size())
SC_OBJ.push_in(True)
SC_OBJ.push_in(45)
print(SC_OBJ.stack_size())
print(SC_OBJ.stack_quantity())
print(SC_OBJ.view_stacks())
