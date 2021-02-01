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


class Stack:
    count: int
    items = []

    def __init__(self, count):
        self.count = count

    def __str__(self):
        return str(self.items)

    def push(self, item):
        count_stack = len(self.items)
        if count_stack == 0:
            self.items.append([])
            count_stack = len(self.items)
            self.items[count_stack - 1].append(item)
        else:
            len_stack = len(self.items[count_stack - 1])
            if len_stack == self.count:
                self.items.append([])
            count_stack = len(self.items)
            self.items[count_stack - 1].append(item)

    def pop(self):
        count_stack = len(self.items)
        if count_stack > 0:
            len_stack = len(self.items[count_stack - 1])
            item = self.items[count_stack - 1][len_stack - 1]
            if len_stack == 1:
                del self.items[count_stack - 1]
            else:
                del self.items[count_stack - 1][len_stack - 1]
            return item


stack_1 = Stack(7)
for i in range(16):
    stack_1.push(random.randint(1, 10))
    print(stack_1)

print("-----------------------")

for i in range(20):
    stack_1.pop()
    print(stack_1)

print("-----------------------")

for i in range(16):
    stack_1.push(random.randint(1, 10))
    print(stack_1)
