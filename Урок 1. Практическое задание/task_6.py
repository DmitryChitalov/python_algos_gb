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
        self.base = []
        self.reworked = []
        self.completed = []

    def is_empty(self):
        return self.base == []

    def to_queue(self, item):
        self.base.insert(0, item)

    def from_queue(self):
        return self.base.pop()

    def size(self):
        return len(self.base)

    def complete(self):
        self.completed.insert(0, self.base.pop())

    def rework(self):
        self.reworked.insert(0, self.base.pop())


qc_obj = QueueClass()

qc_obj.to_queue('Task_1')
qc_obj.to_queue('Task_2')
qc_obj.to_queue('Task_3')
qc_obj.to_queue('Task_4')

print(qc_obj.size())  # -> 3

qc_obj.complete()
qc_obj.rework()

print(qc_obj.base)
print(qc_obj.completed)
print(qc_obj.reworked)
