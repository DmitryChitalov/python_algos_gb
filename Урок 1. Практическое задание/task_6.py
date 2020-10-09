"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


class PlateStack:
    def __init__(self, max_stack_size):
        self.stacks = []
        self.max_stack_size = max_stack_size
        self.current_stack = Stack()
        self.stacks.append(self.current_stack)

    def __len__(self):
        return len(self.stacks)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def push(self, item):
        self.current_stack.push(item)
        if len(self.current_stack) == self.max_stack_size:
            self.current_stack = Stack()
            self.stacks.append(self.current_stack)


if __name__ == '__main__':
    st = PlateStack(3)
    st.push('plate1')
    st.push('plate2')
    st.push('plate3')
    st.push('plate4')
    st.push('plate5')
