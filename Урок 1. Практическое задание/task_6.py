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
        self.main = []
        self.resolved = []
        self.unresolved = []

    def is_main_empty(self):
        return self.main == []

    def to_main_queue(self, task):
        self.main.insert(0, task)

    def to_resolve(self):
        self.resolved.append(self.main.pop())
        self.resolved.sort()

    def to_rework(self):
        self.unresolved.insert(0, self.main.pop())

    def reworked(self):
        self.resolved.append(self.unresolved.pop())

    def main_size(self):
        return len(self.main)

    def show_tasks(self):
        return f' !!!main: {self.main}\n resolved: {self.resolved}\n unresolved: {self.unresolved}'


tasks = TaskBoard()

for i in range(10):
    tasks.to_main_queue(f'task {i+1}')

print(tasks.show_tasks())

tasks.to_resolve()
tasks.to_resolve()
tasks.to_resolve()

print(tasks.show_tasks())

tasks.to_rework()

print(tasks.show_tasks())

tasks.reworked()

print(tasks.show_tasks())
