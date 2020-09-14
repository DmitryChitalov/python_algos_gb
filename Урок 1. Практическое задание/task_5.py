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
    def __init__(self, capacity):
        self.stacks = []
        if capacity < 1:
            raise NameError("Стек больше одного")
        else:
            self.capacity = capacity

    def push(self, item):  # добавить
        if self.stacks == []:
            self.stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)

    def pop(self):  # извлечь
        if self.stacks == []:
            raise NameError('Стек пуст')
        else:
            popped_data = self.stacks[-1][-1]
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                del self.stacks[-1][-1]
        return popped_data

    def popAt(self, index):  # извлечь из
        if self.stacks == []:
            raise NameError('Стек пуст')
        elif index - 1 > len(self.stacks):
            raise NameError('вне стека')
        else:
            popped_data = self.stacks[index - 1][-1]
            if len(self.stacks[index - 1]) == 1:
                del self.stacks[-1]
            elif len(self.stacks) == index:
                del self.stacks[-1][-1]
            else:
                self.stacks[index - 1][-1] = self.stacks[index][0]
                for i in range(index, len(self.stacks)):
                    for j in range(0, len(self.stacks[i]) - 1):
                        self.stacks[i][j] = self.stacks[i][j + 1]
                    if i < len(self.stacks) - 1:
                        self.stacks[i][-1] = self.stacks[i + 1][0]
                del self.stacks[-1][-1]
                if len(self.stacks[-1]) == 0:
                    del self.stacks[-1]
        return popped_data

    def peek(self):
        return self.stacks[len(self.stacks) - 1]

    def size(self):  # размер
        return len(self.stacks)

    def isEmpty(self):
        return self.stacks == []


s = Stack(4)
s.push('зеленая_1')
s.push('зеленая_2')
s.push('зеленая_3')
s.push('зеленая_4')
s.push('зеленая_5')
s.push('зеленая_6')
s.push('зеленая_7')
s.push('белая_1')
s.push('белая_2')
s.push('белая_3')
s.push('белая_4')
s.push('белая_5')
s.push('белая_6')
s.push('белая_7')
s.push('желтая_1')
s.push('красная_1')

print(s.popAt(0))
print(s.popAt(1))
print(s.popAt(2))
print(s.popAt(3))
