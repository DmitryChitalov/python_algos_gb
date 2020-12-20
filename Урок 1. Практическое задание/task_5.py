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
    def __init__(self, max_size):
        self.items = [[]]
        self.max_size = max_size

    def isEmpty(self):
        return self.items == [[]]

    def push(self, element):
        if len(self.items[len(self.items)-1]) < self.max_size:
            self.items.append(element)
        else:
            self.items.append([])
            self.items[len(self.items)-1].append(element)

    def pop(self):
        result = len(self.items[len(self.items)-1]).pop()
        if len(self.items[len(self.items)-1]) == 0:
            self.items.pop()
        return result

    def __str__(self):
        return str(self.items)

    def get_value(self):
        return self.items[len(self.items) - 1][len(self.items[len(self.items)-1])-1]

    def size(self):
        items_summary = 0
        for stack in self.items:
            items_summary += len(stack)
        return items_summary
    def stack_count(self):
        return len(self.items)