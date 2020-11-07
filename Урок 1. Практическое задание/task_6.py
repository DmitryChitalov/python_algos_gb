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
        self.el = []

    def add_queue(self, value):
        self.el.insert(0, value)

    def get_queue(self):
        return self.el.pop()

    def size_queue(self):
        return len(self.el)

    def empty(self):
        return self.el == []


class TaskBoard:
    def __init__(self):
        self.current_queue = QueueClass()
        self.re_work_queue = QueueClass()
        self.done_work = []

    def task_done(self):
        done_tsk = self.current_queue.get_queue()
        self.done_work.append(done_tsk)

    def re_work(self):
        done_tsk = self.current_queue.get_queue()
        self.re_work_queue.add_queue(done_tsk)

    def current_queue(self, value):
        self.current_queue.add_queue(value)


if __name__ == '__main__':
    new_board = TaskBoard()
    new_board.current_queue('Work 1')
    new_board.current_queue('Work 2')
    new_board.current_queue('Work 3')
    new_board.current_queue('Work 4')
    