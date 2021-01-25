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


class Trello_board():
    def __init__(self):
        self.todo_list = QueueClass()
        self.remake_list = QueueClass()
        self.done_list = []

    def add_todo_list(self, item):
        self.todo_list.to_queue(item)

    def todo_task(self):
        return self.todo_list.elems[len(self.todo_list.elems) - 1]

    def add_remake_list(self):
        task = self.remake_list.from_queue()
        self.remake_list.to_queue(task)

    def remake_task(self):
        return self.remake_list.elems[len(self.remake_list.elems) - 1]

    def add_done_list(self):
        task = self.todo_list.from_queue()
        self.done_list.append(task)


if __name__ == '__main__':
    trello_board = Trello_board()
    trello_board.add_todo_list('Make task 1')
    trello_board.add_todo_list('Make task 2')
    trello_board.add_todo_list('Make task 3')
    print(trello_board.todo_list.elems)
    print(trello_board.todo_task())
    trello_board.add_remake_list()
    print(trello_board.remake_list.elems)
    print(trello_board.add_remake_list())
    trello_board.add_done_list()
    print(trello_board.add_done_list())
