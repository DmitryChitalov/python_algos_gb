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
        self.base_queue = QueueClass()
        self.revision_queue = QueueClass()

    def is_empty(self):
        return self.base_queue.is_empty() and self.revision_queue.is_empty()

    def size(self):
        return self.base_queue.size() + self.revision_queue.size()

    def to_queue(self, item):
        self.base_queue.to_queue(item)

    def from_queue(self):
        return self.base_queue.from_queue()

    def to_revision(self, item):
        self.revision_queue.to_queue(item)

    def from_revision(self):
        return self.revision_queue.from_queue()



qc_obj = TaskBoard()
print(qc_obj.is_empty())  # -> True. Очередь пустая

# помещаем объекты в очередь
qc_obj.to_queue('my_obj')
qc_obj.to_queue(4)
qc_obj.to_queue(True)

print(qc_obj.is_empty())  # -> False. Очередь пустая

print(qc_obj.size())  # -> 3

print(qc_obj.from_queue())  # -> my_obj

print(qc_obj.size())  # -> 2

task = qc_obj.from_queue()
qc_obj.to_revision(task)

print(qc_obj.size()) # -> 2

print(qc_obj.from_revision()) # -> 4

print(qc_obj.size()) # -> 2