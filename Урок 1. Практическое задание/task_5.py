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


class PlateStack:
    def __init__(self, max_count):
        self.elems = [[]]
        self.max_count = max_count

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self):
        if len(self.elems[-1]) == self.max_count:
            print('Стопка заполнена, приготовьте новую')
        else:
            self.elems[-1].append('plate')

    def add_stack(self):
        if len(self.elems[-1]) != self.max_count:
            print('Предыдущая стопка не заполнена')
        else:
            self.elems.append([])

    def pop_out(self):
        try:
            self.elems[-1].pop()
        except IndexError:
            print('Стопка пуста')

    def del_stack(self):
        if self.elems[-1] == []:
            self.elems.pop()
        else:
            print('Стопка не пуста')

    def stacks_quantity(self):
        return len(self.elems)

    def last_stack_size(self):
        return len(self.elems[-1])


plates = PlateStack(5)
plates.push_in()
plates.push_in()
plates.push_in()
plates.push_in()
plates.push_in()
plates.push_in()
print(plates)
print(plates.stacks_quantity())
plates.add_stack()
plates.add_stack()
plates.push_in()
plates.push_in()
plates.push_in()
print(plates)
plates.pop_out()
print(plates)
plates.pop_out()
print(plates)
plates.pop_out()
print(plates)
print(plates.stacks_quantity())
plates.pop_out()
print(plates)
plates.del_stack()
print(plates)
plates.del_stack()
print(plates)
plates.del_stack()
print(plates)
plates.del_stack()
print(plates)
plates.del_stack()
plates.pop_out()
print(plates)
plates.add_stack()
print(plates)
plates.push_in()
print(plates)
print(plates.last_stack_size())
