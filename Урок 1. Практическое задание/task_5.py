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


class StackPlates():
    def __init__(self, max_size):
        self.max_size = max_size
        self.stacks = []
        self.elems = []

    def __str__(self):
        return str(self.stacks + [self.elems])

    def is_empty(self):
        return self.stacks == []

    def push_in(self, el):
        self.elems.append(el)
        if len(self.elems) == self.max_size:
            self.stacks.append(self.elems)
            self.elems = []

    def pop_out(self):
        if len(self.elems) != 0:
            return self.elems.pop()
        else:
            self.elems = self.stacks.pop()
            return self.elems.pop()

    def get_val(self): #последняя тарелка в последней стопке
        if len(self.elems) !=0:
            return self.elems[len(self.elems) - 1]
        else:
            return self.stacks[len(self.elems) - 1][self.max_size-1]

    def stacks_number(self): #количество стопок
        if len(self.elems) == 0:
            return len(self.stacks)
        else:
            return (len(self.stacks)+1)

    def stack_size(self):
        return (len(self.elems)+len(self.stacks)*max_plates)



if __name__ == "__main__":

    max_plates = int(input('Введите количество тарелок в стопке:'))
    n = int(input('Введите общее количество тарелок:'))
    stack_plates = StackPlates(max_plates)
    print(stack_plates.is_empty())
    for i in range(n):
        stack_plates.push_in(('plate_'+ str(i)))
    print(stack_plates.is_empty())
    print(stack_plates)
    print(stack_plates.get_val())
    print(stack_plates.stack_size())
    print((stack_plates.stacks_number()))
    stack_plates.pop_out()
    stack_plates.pop_out()
    stack_plates.pop_out()
    print(stack_plates)
    print(stack_plates.get_val())
    print(stack_plates.stack_size())