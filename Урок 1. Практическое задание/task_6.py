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
class Queueing:
    def __init__(self):
        self.elements = []

    def is_null(self):
        return self.elements == []

    def to_queue(self, tasks):
        self.elements.insert(0, tasks)

    def from_queue(self):
        return self.elements.pop()

    def sized(self):
        return len(self.elements)


class Board_task:
    def __init__(self):
        self.base_queue = Queueing()
        self.queue_for_revision = Queueing()
        self.list_of_completed = []

    def perform_task(self):
        task = self.base_queue.from_queue()
        self.list_of_completed.append(task)


    def for_revision_task(self):
        task = self.queue_for_revision.from_queue()
        self.queue_for_revision.to_queue(task)

    def add_to_current(self, tasks):
        self.base_queue.to_queue(tasks)

    def from_revision(self):
        task = self.queue_for_revision.from_queue()
        self.base_queue.to_queue(task)

if __name__ == '__main__':
    taskBoard = Board_task()
    taskBoard.add_to_current("Здача1")
    taskBoard.add_to_current("Здача2")
    taskBoard.add_to_current("Здача3")
    taskBoard.add_to_current("Здача4")
    print(taskBoard.base_queue.elements)
    print(taskBoard.from_revision())