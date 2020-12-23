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


class TaskBoard:
    def __init__(self):
        self.current_queue = QueueClass()
        self.rework_queue = QueueClass()
        self.completed = []

    def to_current(self, t):
        self.current_queue.to_queue(t)

    def current_task(self):
        return self.current_queue.elems[len(self.current_queue.elems) - 1]

    def to_completed(self):
        t = self.current_queue.from_queue()
        self.completed.append(t)

    def to_rework(self):
        t = self.current_queue.from_queue()
        self.rework_queue.to_queue(t)

    def rework_task(self):
        return self.rework_queue.elems[len(self.rework_queue.elems) - 1]

    def from_rework(self):
        t = self.rework_queue.from_queue()
        self.current_queue.to_queue(t)


task = TaskBoard()
task.to_current("Wake up")
task.to_current("Stand up")
task.to_current("Make up")
print("First: " + task.current_task())
task.to_completed()
print("Second: " + task.current_task())
task.to_rework()
print("Rework: " + task.rework_task())
print("Third: " + task.current_task())
print(task.current_queue.elems)
task.from_rework()
print(task.rework_queue.elems)
print(task.current_queue.elems)
task.to_completed()
print(task.current_queue.elems)