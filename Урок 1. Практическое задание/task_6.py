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

########################################################################################################################


class Tasks:
    def __init__(self):
        self.tasks = []
        self.done = []
        self.revision = []

    def is_empty(self):
        return self.tasks == [], self.done == [], self.revision == []

    def to_queue(self, task):
        self.tasks.insert(0, task)

    def done_tasks(self):
        task = self.tasks.pop()
        self.done.append(task)

    def revision_queue(self):
        task = self.tasks.pop()
        self.revision.append(task)

    def size(self):
        return len(self.tasks), len(self.done), len(self.revision)


t = Tasks()
for i in range(1, 12):
    t.to_queue(i)

t.done_tasks()
t.done_tasks()
t.revision_queue()
print(t.size())

