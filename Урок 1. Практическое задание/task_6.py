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
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def to_queue(self, el):
        self.elements.insert(0, el)

    def from_queue(self):
        return  self.elements.pop()


class Tasks:
    def __init__(self):
        # Базовая очередь
        self.base_q = Queue()
        # Очередь на доработку
        self.revision_q = Queue()
        # Список решенных задач
        self.done = []

    def close_task(self):
        # Задача выполнена - закрываем и сохраняем в списке закрытых
        t = self.base_q.from_queue()
        self.done.append(t)

    def to_revision(self):
        # Отправляем задачу на доработку
        t = self.base_q.from_queue()
        self.revision_q.to_queue(t)

    def from_revision(self):
        # Задача доработана, возвращаем в рабочую очередь
        t = self.revision_q.from_queue()
        self.base_q.to_queue(t)

    def to_work(self, task):
        # Берем задачу в работу
        self.base_q.to_queue(task)

    def curr_task(self):
        # Текущая задача
        return self.base_q.elements[-1]
#        return self.base_q.elements[len(self.base_q.elements) - 1]

    def curr_revision(self):
        # Задача в дораработке
        return self.revision_q.elements[-1]


board = Tasks()
board.to_work('Задача 1')
board.to_work('Задача 2')
board.to_work('Задача 3')
board.to_work('Задача 4')

print('Текущая задача ' + board.curr_task())
board.to_revision()
print('Текущая задача ' + board.curr_task())
print('Задача на доработке ' + board.curr_revision())
board.to_revision()
print('Текущая задача ' + board.curr_task())
print('Задача на доработке ' + board.curr_revision())
board.close_task()
print('Текущая задача ' + board.curr_task())
print('Задача на доработке ' + board.curr_revision())
board.from_revision()
print('Текущая задача ' + board.curr_task())
print('Задача на доработке ' + board.curr_revision())

