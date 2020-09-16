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
        self.elems_sq = []


    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def send_to_second_Queue(self):
        self.elems_sq.insert(0, self.from_queue())

    def sq_is_empty(self):
        return self.elems_sq == []

    def sq_to_queue(self, item):
        self.elems_sq.insert(0, item)

    def sq_from_queue(self):
        return self.elems_sq.pop()

    def sq_size(self):
        return len(self.elems_sq)


c = QueueClass()
c.to_queue(123)
c.send_to_second_Queue()
c.sq_to_queue('hello')
print(c.sq_is_empty())
print(c.sq_size())
print(c.sq_from_queue())
print(c.sq_size())
print(c.sq_from_queue())
print(c.sq_is_empty())

