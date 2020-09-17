"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие нескольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class QueueClass:
    def __init__(self):
        self.elems = []

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.basic = QueueClass()
        self.revision = QueueClass()
        self.ready = QueueClass()

    def to_basic(self, el):
        self.basic.to_queue(el)

    def to_revision(self):
        el = self.basic.from_queue()
        self.revision.to_queue(el)

    def from_revision(self):
        el = self.revision.from_queue()
        self.basic.to_queue(el)

    def to_ready(self):
        el = self.basic.from_queue()
        self.ready.to_queue(el)


if __name__ == '__main__':
    my_board = TaskBoard()
    my_board.to_basic('Task1')
    my_board.to_basic('Task2')
    my_board.to_basic('Task3')
    my_board.to_basic('Task4')
    my_board.to_basic('Task5')
    print(my_board.basic)
    my_board.to_revision()
    my_board.to_revision()
    my_board.from_revision()
    my_board.to_ready()
    my_board.to_ready()
    print(my_board.basic)
    print(my_board.revision)
    print(my_board.ready)
