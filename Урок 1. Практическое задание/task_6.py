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


class TaskBoard(object):
    def __init__(self):
        self.base_queue = QueueClass()
        self.revision_queue = QueueClass()
        self.completed_task = []

    def complete_task(self):
        """Закрыть задачу и отправить в список завершенных"""
        task = self.base_queue.from_queue()
        self.completed_task.append(task)

    def to_revision(self):
        """Отправить задачу на доработку"""
        task = self.base_queue.from_queue()
        self.revision_queue.to_queue(task)

    def add_cur_task(self, task):
        """Добавить  в текущие задачи"""
        self.base_queue.to_queue(task)

    def from_revision(self):
        """Вернуть задачу из доработки в текущие задачи"""
        task = self.revision_queue.from_queue()
        self.base_queue.to_queue(task)

    def cur_task(self):
        return self.base_queue.elems[len(self.base_queue.elems) - 1]

    def cur_revision(self):
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]


if __name__ == "__main__":
    task_board = TaskBoard()
    task_board.add_cur_task("Task1")
    task_board.add_cur_task("Task2")
    task_board.add_cur_task("Task3")

    print(task_board.cur_task())

    task_board.to_revision()
    task_board.to_revision()
    print(task_board.cur_revision())

    task_board.from_revision()
