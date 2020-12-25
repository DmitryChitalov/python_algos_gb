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

import random


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def get_line(self):
        line = ''
        line += '\t'.join([str(el) for el in self.elems])
        return line

    def __str__(self):
        return self.get_line()


class StackOfPlates(StackClass):

    __plates_in_stack = 10

    @property
    def plates_in_stack(self):
        return self.__plates_in_stack

    def push_in(self, list_of_plates):
        if self.is_empty() and len(list_of_plates) > 0:
            self.elems.append(StackClass())
        for plate in list_of_plates:
            if self.get_val().stack_size() < self.plates_in_stack:
                self.get_val().push_in(plate)
            else:
                new_stack = StackClass()
                new_stack.push_in(plate)
                self.elems.append(new_stack)

    def total_plates(self):
        return (self.stack_size() - 1) * self.plates_in_stack + self.get_val().stack_size()

    def pop_out(self):
        self.take_plates(1)

    def take_plates(self, number):
        if number > self.total_plates():
            raise Exception('Столько тарелок нет!')
        lst_plates = []
        for i in range(number):
            if self.get_val().stack_size() == 0:
                self.elems.pop()
            lst_plates.append(self.get_val().pop_out())
        return lst_plates

    def get_line(self):
        s = ''
        s += '\n'.join([stk.get_line() for stk in self.elems])
        return s


st = StackOfPlates()

lst = [i for i in range(random.randint(10, 30))]
print(f'Добавляем тарелки: {lst}')
st.push_in(lst)
print(st)

num = random.randint(1, 20)
st.take_plates(num)
print(f'Удалили {num} тарелок:')
print(st)

lst = [i for i in range(random.randint(5, 15))]
print(f'Добавляем тарелки: {lst}')
st.push_in(lst)
print(st)

num = random.randint(1, 10)
st.take_plates(num)
print(f'Удалили {num} тарелок:')
print(st)
