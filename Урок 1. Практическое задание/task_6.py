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

    def to_queue(self, el):
        self.elems.insert(0, el)

    def from_queue(self, el):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

class TaskBoard:
    def __init__(self):
     self.curr_queue = QueueClass()
     self.revis_queue = QueueClass()
     self.log = []

    def done_task(self):
        task=self.curr_queue.from_queue()
        self.log.append(task)

    def to_revise_task(self):
        task = self.curr_queue.from_queue()
        self.log.append(task)

    def to_curr_queue(self, el):
        self.curr_queue.to_queue(el)

    def from_revision(self):
        task = self.revis_queue.from_queue()
        self.curr_queue.to_queue(task)

    def curr_task(self):
        return self.curr_queue.elems[len(self.curr_queue.elems)-1]

    def revise_task(self):
        return self.revis_queue.elems[len(self.revis_queue.elems)-1]