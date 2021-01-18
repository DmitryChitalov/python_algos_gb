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
        self.elems_2 = []
        self.max_size = 5
        self.counter = 1

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if len(self.elems) < self.max_size:
            self.elems.append(el)
            print(f'Добавлен элемент "{el}" в стек 1')
        else:
            self.elems_2.append(el)
            print(f'Стек 1 наполнен. Добавлен элемент {el} в стек 2.')

    def pop_out(self, stack_num=None):
        if not stack_num:
            return self.elems.pop()
        else:
            return self.elems_2.pop()

    def get_val(self, stack_num=None):
        if not stack_num:
            return self.elems[len(self.elems) - 1]
        else:
            return self.elems[len(self.elems_2) - 1]

    def stack_size(self, stack_num=None):
        if not stack_num:
            return len(self.elems)
        else:
            return len(self.elems_2)


SC_OBJ = StackClass()

print(SC_OBJ.is_empty())  # -> стек пустой

# наполняем стек
SC_OBJ.push_in(1)
SC_OBJ.push_in(2)
SC_OBJ.push_in(3)
SC_OBJ.push_in(4)
SC_OBJ.push_in(5)
print(SC_OBJ.stack_size())
SC_OBJ.push_in(6)
print(SC_OBJ.stack_size(1))
SC_OBJ.push_in(7)
SC_OBJ.push_in(8)
SC_OBJ.push_in(9)

print(SC_OBJ.stack_size())
print(SC_OBJ.stack_size(1))
