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


class Queue:
    def __init__(self):
        self.el = []

    def is_empty(self):
        return self.el == []

    def add_to_queue(self, item):
        self.el.insert(0, item)

    def delete_from_queue(self):
        return self.el.pop()

    def size(self):
        return len(self.el)

    def show_cur_on_queue(self):
        try:
            a = self.el[len(self.el)-1]
        except IndexError:
            a = []
        return (a)


class Tasks:
    def __init__(self):
        self.task_queue = Queue()
        self.checks = Queue()
        self.completed = []

    def add_to_task(self, task):
        self.task_queue.add_to_queue(task)

    def show_task(self):
        return (self.task_queue.show_cur_on_queue())

    def complete_task(self):
        task = self.task_queue.delete_from_queue()
        self.completed.append(task)

    def add_to_checks(self):
        task = self.task_queue.delete_from_queue()
        self.checks.add_to_queue(task)

    def show_checks(self):
        return (self.checks.show_cur_on_queue())

    def return_from_checks(self):
        task = self.checks.delete_from_queue()
        self.task_queue.add_to_queue(task)

board=Tasks()

board.add_to_task('test1')
board.add_to_task('test2')
print(board.task_queue.el)
print(board.show_task())
board.add_to_checks()
print(board.task_queue.el)
print(board.show_task())
board.complete_task()
print(board.task_queue.el)
print(board.show_task())
board.return_from_checks()
print(board.task_queue.el)
print(board.show_task())
print(board.completed)