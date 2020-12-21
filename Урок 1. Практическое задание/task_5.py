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


class StacksClass:
    def __init__(self):
        self.stacks = {}

    def is_empty(self):
        return self.stacks == {}

    def push_in(self, el):
        last_stack = self.find_last()
        if self.is_empty():
            self.stacks.update({"1": [el]})
        elif self.is_full():
            self.stacks.update({str(int(last_stack)+1): [el]})
        elif not self.is_empty() and not self.is_full():
            self.stacks[last_stack].append(el)

    def is_full(self):
        return self.stack_size() >= 10

    def show_struct(self):
        for items in self.stacks.items():
            print("{} : {}".format(*items[0], items[1]))

    def find_last(self):
        if not self.is_empty():
            return max(self.stacks.keys())

    def pop_out(self):
        if not self.is_empty():
            if self.stack_size() == 0:
                self.stacks.pop(self.find_last())
            return self.stacks[self.find_last()].pop()

    def get_val(self):
        if not self.is_empty():
            return self.stacks[self.find_last()][self.stack_size() - 1]

    def stack_size(self):
        if not self.is_empty():
            return len(self.stacks[self.find_last()])


"""
Тестирование поведения 
"""
SC_OBJ = StacksClass()
for i in range(50):
    SC_OBJ.push_in(i)
SC_OBJ.show_struct()
for i in range(11):
    SC_OBJ.pop_out()
print(SC_OBJ.pop_out())
print(SC_OBJ.get_val())
for i in range(12):
    SC_OBJ.push_in(i)
SC_OBJ.show_struct()
print(SC_OBJ.get_val())

