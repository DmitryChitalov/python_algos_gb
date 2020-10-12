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

    def push_in(self, el):
        self.elems.insert(0, el)

    def pop_out(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TasksBoard:

    def __init__(self, task, completed):
        self.cur_queue = QueueClass()
        self.revision_queue = QueueClass()
        self.log = []

    def resolve_task(self):
        task = self.cur_queue.pop_out()
        self.log.append(task)

    def to_revision_task(self):
        task = self.cur_queue.pop_out()
        self.revision_queue.push_in(task)

    def to_current_task(self, el):
        self.cur_queue.push_in(el)

    def from_revision(self):
        task = self.revision_queue.pop_out()
        self.cur_queue.push_in(task)

    def current_task(self):
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]

    def current_revision(self):
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]
