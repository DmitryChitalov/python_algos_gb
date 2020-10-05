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


class TaskBoard:
    def __init__(self):
        self.base_queue = QueueClass()
        self.revision_queue = QueueClass()
        self.solved_list = []

    def to_queue(self, item):
        self.base_queue.to_queue(item)

    def task_solved(self):
        self.solved_list.append(self.base_queue.from_queue())

    def to_revise(self):
        self.revision_queue.to_queue(self.base_queue.from_queue())

    def task_revised(self):
        self.solved_list.append(self.revision_queue.from_queue())


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


task_board = TaskBoard()

task_board.to_queue("Сделать гб")
task_board.to_queue("Купить еды")
task_board.to_queue("Сходить на работу")
task_board.to_queue("Подготовиться к универу")
task_board.to_queue("Позвонить родителям")

task_board.task_solved()
task_board.task_solved()
task_board.to_revise()
task_board.task_solved()
task_board.task_solved()
task_board.task_revised()
