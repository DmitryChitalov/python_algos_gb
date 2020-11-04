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

"""К имеющемуся коду добавил 2 списка: выполненные и сложные задачи.
А также методы, которые перемещают задачи из основной очереди в одну из двух.
Методы size и is_empty показывают размер и пустая ли очередь всех очередей
Еще один метод показывает содержимое всех очерей"""


class QueueClass:
    def __init__(self):
        self.queue = []
        self.done_task = []
        self.hard_task = []

    def is_empty(self):
        return self.queue == [], self.done_task == [], self.hard_task == []

    def to_queue(self, item):
        self.queue.insert(0, item)

    def from_queue(self):
        return self.queue.pop()

    def to_done(self):
        self.done_task.insert(0, self.queue.pop())

    def to_hard(self):
        self.hard_task.insert(0, self.queue.pop())

    def size(self):
        return len(self.queue), len(self.done_task), len(self.hard_task)

    def all_queue(self):
        return self.queue, self.done_task, self.hard_task


if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty())

    qc_obj.to_queue('my_obj')
    qc_obj.to_queue(4)
    qc_obj.to_queue(True)

    print(qc_obj.is_empty())

    print(qc_obj.size())

    print(qc_obj.from_queue())
    print(qc_obj.all_queue())
    qc_obj.to_hard()

    print(qc_obj.size())

    print(qc_obj.all_queue())
    print(qc_obj.is_empty())
