"""
Задание 6.
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


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class DashBoard:
    def __init__(self):
        self.base = QueueClass()
        self.done = QueueClass()
        self.undone = QueueClass()

    def to_queue(self, item):
        self.base.to_queue(item)

    def to_done_queue(self):
        self.done.to_queue(self.base.from_queue())

    def to_undone_queue(self):
        self.undone.to_queue(self.base.from_queue())

    def to_base(self):
        self.base.to_queue(self.undone.from_queue())

    def size(self):
        return len(self.base.elems)

    def print_base(self):
        return print(self.base.elems)

    def print_done(self):
        return print(self.done.elems)

    def print_undone(self):
        return print(self.undone.elems)


if __name__ == '__main__':
    dash = DashBoard()
    dash.to_queue(1)
    dash.to_queue(2)
    dash.to_queue(3)
    dash.to_queue(4)
    print(dash.size())
    dash.print_base()
    dash.to_done_queue()
    dash.print_base()
    dash.print_done()
    dash.print_undone()
    dash.to_undone_queue()
    dash.print_base()
    dash.print_done()
    dash.print_undone()
    dash.to_base()
    dash.print_base()
    dash.print_done()
    dash.print_undone()