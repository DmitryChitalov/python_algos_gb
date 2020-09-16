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

class WorkClass:
    def __init__(self):
        self.comm = QueueClass()
        self.unsolved = QueueClass()
        self.done_lst = []

    def done(self):
        lab = self.comm.from_queue()
        self.done_lst.append(lab)

    def not_done(self):
        lab = self.comm.from_queue()
        self.unsolved.to_queue(lab)

    def to_common_queue(self, item):
        self.comm.to_queue(item)

    def from_unsolved(self):
        lab = self.unsolved.from_queue()
        self.comm.to_queue(lab)

if __name__ == '__main__':
    que = WorkClass()
    que.to_common_queue('bla')
    que.to_common_queue(11)
    que.to_common_queue(82)
    que.to_common_queue('abc')
    print(que.comm.elems)
    que.done()
    print(que.done_lst)
    que.not_done()
    print(que.unsolved.elems)
    print(que.comm.elems)
    que.from_unsolved()
    print(que.unsolved.elems)



