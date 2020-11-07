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

    def __init__(self, base_list, rework_list):
        self.base_queue = base_list
        self.rework_queue = rework_list

    def queue_len(self, queue_name):
        return len(self.base_queue) if queue_name == 'base' else len(self.rework_queue)

    def add_task(self, task_name, queue_name):
        self.base_queue.append(task_name) if queue_name == 'base' else \
            self.rework_queue.append(task_name)

    def take_task(self, queue_name):
        return self.base_queue.pop(0) if queue_name == 'base' else \
            self.rework_queue.pop(0)

    def clear_queue(self, queue_name):
        self.base_queue.clear() if queue_name == 'base' else \
            self.rework_queue.clear()


queue = Queue(['task1_link', 'task2_link', 'tsk3_link'], ['task4_link', 'task5_link'])
queue.add_task('task6_link', 'base')
print(queue.queue_len('base'))
print(queue.queue_len('rework'))
print(queue.take_task('rework'))
print(queue.queue_len('rework'))
queue.clear_queue('rework')
print(queue.queue_len('rework'))


