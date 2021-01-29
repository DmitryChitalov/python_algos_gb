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
        self.doing = []
        self.done = []
        self.bugs = []

    def is_empty(self, queue):
        return queue == []

    def to_queue(self, el):
        self.doing.append(el)

    def from_queue(self, from_queue, to_queue):
        if len(from_queue) > 0:
            val = from_queue.pop(0)
            to_queue.append(val)
        else:
            print('В извлекаемой очереди нет задач.')
            val = None
        return val

    def size(self, queue):
        return len(queue)