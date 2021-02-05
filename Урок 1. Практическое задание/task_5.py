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
для реализации этой структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class StackClass:

    def __init__(self, max_stacks, max_in_stack):
        self.plates = []
        for i in range(max_stacks):
            self.plates.append([])  # заранее создаём списки в списке
        self.stack = 0
        self.max_in_stack = max_in_stack

    def is_empty(self):
        return self.plates == []

    def push_in(self, el):
        try:
            if len(self.plates[self.stack]) == self.max_in_stack:
                self.stack += 1  # переходим между стэками по необходимости
            self.plates[self.stack].append(el)
        except IndexError:
            print('Закончилось место под стопки')
            self.stack -= 1

    def pop_out(self):
        try:
            if len(self.plates[self.stack]) == 0:
                self.stack -= 1  # переходим между стэками по необходимости
            return self.plates[self.stack].pop()
        except IndexError:
            print('Закончились тарелки')
            self.stack = 0

    def get_val(self):
        if len(self.plates[self.stack]) == 0:
            self.stack -= 1  # Если до этого удалили последний элемент из стека и не перешли на предыдущий
        return self.plates[self.stack][len(self.plates[self.stack]) - 1]

    def stack_size(self):
        if len(self.plates[self.stack]) == 0:
            self.stack -= 1  # переходим между стэками по необходимости
        return len(self.plates[self.stack])

    def get_stack(self):
        if len(self.plates[self.stack]) == 0:
            self.stack -= 1  # переходим между стэками по необходимости
        return self.plates[self.stack]

    def get_stacks(self):
        if len(self.plates[self.stack]) == 0:
            self.stack -= 1  # переходим между стэками по необходимости
        return self.plates


plates_stacks = StackClass(3, 10)   # первое число - максимальное количество стопок, второе - максимальное количество
                                    # тарелок в стопке

for i in range(31):
    plates_stacks.push_in(f'plate{i + 1}')

print(plates_stacks.stack_size())
print(plates_stacks.get_val())
print(plates_stacks.get_stack())
print(plates_stacks.get_stacks())

for i in range(3):
    plates_stacks.pop_out()

print(plates_stacks.stack_size())
print(plates_stacks.get_val())
print(plates_stacks.get_stack())
print(plates_stacks.get_stacks())
