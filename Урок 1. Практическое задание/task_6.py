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


class TaskBoard:
    def __init__(self):
        self.base = []
        self.revision = []
        self.solved = []

    def is_empty(self):
        return self.base == self.revision == []

    def to_base_queue(self, item):
        self.base.insert(0, item)

    def from_base_queue(self):
        self.solved.insert(0, self.base.pop())

    def to_revision_queue(self):
        self.revision.insert(0, self.base.pop())

    def from_revision_queue(self):
        self.solved.insert(0, self.revision.pop())

    def show_tasks(self):
        print(self.base, self.revision)

    def size(self):
        return len(self.base), len(self.revision), len(self.solved)


if __name__ == '__main__':
    SC_OBJ = TaskBoard()
    print(SC_OBJ.is_empty())
    SC_OBJ.to_base_queue('task 1. Do something')
    SC_OBJ.to_base_queue('task 2. Do something else')
    SC_OBJ.from_base_queue()
    SC_OBJ.to_revision_queue()
    SC_OBJ.from_revision_queue()
    print(SC_OBJ.size())
    SC_OBJ.to_base_queue('task 1. Do something')
    SC_OBJ.to_base_queue('task 2. Do something else')
    SC_OBJ.to_base_queue('task 3. Do nothing')
    SC_OBJ.to_revision_queue()
    print(SC_OBJ.size())
    SC_OBJ.show_tasks()
    print(SC_OBJ.is_empty())
