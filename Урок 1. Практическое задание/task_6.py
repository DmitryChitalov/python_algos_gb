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

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

class QueueTasksClass:
    def __init__(self):
        self.queue = QueueClass()
        self.completed = QueueClass()
        self.revision = QueueClass()

    def __str__(self):
        result = f'Задачи в очереди {str(self.queue)}\n Решенные задачи {str(self.completed)}\n ' \
                 f'Задачи на доработке {self.revision}'
        return result

    def task(self, item):
        return self.queue.to_queue(item)

    def solution_task(self, done):
        if done:
            item = self.queue.from_queue()
            self.completed.to_queue(item)
        else:
            item = self.queue.from_queue()
            self.revision.to_queue(item)


if __name__ == '__main__':
    qc_obj = QueueTasksClass()

    qc_obj.task('Задача №1')
    qc_obj.task('Задача №2')
    qc_obj.task('Задача №3')
    qc_obj.task('Задача №4')

    print(f'Задачи в очереди {qc_obj.queue}')
    print('*' * 40, '\n')

    qc_obj.solution_task(True)

    print(f'Задачи в очереди {qc_obj.queue}')
    print(f'Решенные задачи {qc_obj.completed}')
    print('*' * 40, '\n')

    qc_obj.solution_task(False)

    print(f'Задачи в очереди {qc_obj.queue}')
    print(f'Решенные задачи {qc_obj.completed}')
    print(f'Задачи на доработке {qc_obj.revision}')
    print('*' * 40, '\n')

