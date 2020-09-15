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


def tasks(tasks_list: list, n: int) -> QueueClass:
    task_queue = QueueClass()       # общая очередь
    unresolved_task = QueueClass()  # очередь нерешенных задач
    is_solved_task = QueueClass()   # очередь решенных задач
    for itm in tasks_list:
        task_queue.to_queue(itm)
    if task_queue.size() > n:
        num = n
    else:
        num = task_queue.size()
    for i in range(num):
        task = task_queue.from_queue()
        if task[1] == 'is_solved':
            is_solved_task.to_queue(task)
        elif task[1] == 'unresolved':
            unresolved_task.to_queue(task)
        else:
            print(task, 'решения нет')
    return unresolved_task, is_solved_task


tasks([["Вася", 'is_solved'], ["Петя", 'unresolved'], ["Света", 'is_solved'], ["Жанна", 'unresolved'],
             ["Катя", 'unresolved'], ["Лена", 'is_solved']], 7)
