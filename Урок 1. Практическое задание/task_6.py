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


class TaskBoardQueue:
    def __init__(self):
        self.base = []
        self.complete = []
        self.rework = []

    def push_to_base(self, elem):
        self.base.insert(0, elem)

    def pop_from_base(self):
        return self.base.pop(-1)

    def push_to_complete(self, elem):
        self.complete.insert(0, elem)

    def pop_from_complete(self):
        return self.complete.pop(-1)

    def push_to_rework(self, elem):
        self.rework.insert(0, elem)

    def pop_from_rework(self):
        return self.rework.pop(-1)

    def len_base(self):
        return len(self.base)

    def len_complete(self):
        return len(self.complete)

    def len_rework(self):
        return len(self.rework)

    def show_base(self):
        print('base: ', end='')
        print(', '.join(self.base))

    def show_complete(self):
        print('complete: ', end='')
        print(', '.join(self.complete))

    def show_rework(self):
        print('rework: ', end='')
        print(', '.join(self.rework))


board = TaskBoardQueue()
board.push_to_base('task1')
board.push_to_base('task2')
board.push_to_base('task3')
board.show_base()
board.show_complete()
board.show_rework()
board.push_to_complete(board.pop_from_base())
board.show_base()
board.show_complete()
board.show_rework()
board.push_to_rework(board.pop_from_base())
board.show_base()
board.show_complete()
board.show_rework()
board.push_to_rework(board.pop_from_complete())
board.show_base()
board.show_complete()
board.show_rework()
