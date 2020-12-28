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

    def __init__(self, name):
        self.elements = []
        self.__queue_name = name

    @property
    def name(self):
        return self.__queue_name

    def is_empty(self):
        return self.elements == []

    def to_queue(self, item):
        self.elements.insert(0, item)

    def from_queue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)


class TaskBoard:
    def __init__(self):
        self.queues = {'todo': QueueClass('ToDo'), 'in_work': QueueClass('InWork'), 'done': QueueClass('Done')}

    def add_task_todo(self, task):
        self.queues['todo'].to_queue(task)

    def start_new_task(self):
        self.queues['in_work'].to_queue(self.queues['todo'].from_queue())

    def show_task_inwork(self):
        return self.queues['in_work'].elements[self.queues['in_work'].size() - 1]

    def show_next_task_todo(self):
        return self.queues['todo'].elements[self.queues['todo'].size() - 1]

    def finish_task(self):
        self.queues['done'].to_queue(self.queues['in_work'].from_queue())


tb = TaskBoard()
tb.add_task_todo('task1')
tb.add_task_todo('task2')
tb.add_task_todo('task3')
print(f'Следующая задача в списке: {tb.show_next_task_todo()}')
tb.start_new_task()
tb.start_new_task()
tb.add_task_todo('task4')
print(f'Следующая задача в списке: {tb.show_next_task_todo()}')
print(f'Текущая задача в работе: {tb.show_task_inwork()}')
tb.finish_task()
print(f'Текущая задача в работе: {tb.show_task_inwork()}')

