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


class Stack:
    MAX_STACK_SIZE = 4

    def __init__(self):
        self.__stacks = []

    def push(self, element):
        if len(self.__stacks) == 0 or len(self.__stacks[-1]) == self.MAX_STACK_SIZE:
            self.__stacks.append([])

        self.__stacks[-1].append(element)

    def pop(self):
        if len(self.__stacks) == 0:
            return None

        element = self.__stacks[-1].pop()

        if len(self.__stacks[-1]) == 0:
            self.__stacks.pop()

        return element

    def stacks_len(self):
        return len(self.__stacks)

    def __len__(self):
        ln = 0
        for stack in self.__stacks:
            ln += len(stack)

        return ln


plates = Stack()

for i in range(0, 14):
    plates.push(i)

print('len:', len(plates))
print('stacks:', plates.stacks_len())

while True:
    plate = plates.pop()
    if plate is None:
        break
    print('plate:', plate, 'len:', len(plates), 'stacks:', plates.stacks_len())
