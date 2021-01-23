
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
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def to_queue(self, item):
        self.elements.insert(0, item)

    def from_queue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)


class TaskBoard:
    def __init__(self):
        self.cur_queue = QueueClass()  # Базоваяя очередь
        self.revision_queue = QueueClass()  # очередь на доработку
        self.log = []  # Список решенных задач

    def resolve_task(self):

        task = self.cur_queue.from_queue()
        self.log.append(task)

    def to_revision_task(self):

        task = self.cur_queue.from_queue()
        self.revision_queue.to_queue(task)

    def to_current_queue(self, item):

        self.cur_queue.to_queue(item)

    def from_revision(self):

        task = self.revision_queue.from_queue()
        self.cur_queue.to_queue(task)

    def current_task(self):

        return self.cur_queue.elements[len(self.cur_queue.elements) - 1]

    def current_revision(self):

        return self.revision_queue.elements[len(self.revision_queue.elements) - 1]


if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.to_current_queue("Task1")
    task_board.to_current_queue("Task2")
    task_board.to_current_queue("Task3")
    print(task_board.cur_queue.elements)
    print(task_board.current_task())
    task_board.to_revision_task()
    task_board.resolve_task()
    task_board.from_revision()
    print(task_board.cur_queue.elements)
    print(task_board.current_task())
    print(task_board.log)
