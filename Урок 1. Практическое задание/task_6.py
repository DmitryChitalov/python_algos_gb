"""
Задание 6.
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


class TaskBoard:
    def __init__(self):
        self.all_tasks = QueueClass()
        self.rework_tasks = QueueClass()
        self.completed_tasks = list()

    def add_task(self, task):
        return self.all_tasks.to_queue(task)

    def pop_task_and_complete(self):
        if self.all_tasks.size() != 0:
            task = self.all_tasks.from_queue()
            self.completed_tasks.append(task)

    def pop_task_from_rework_and_complete(self):
        if self.rework_tasks.size() != 0:
            task = self.rework_tasks.from_queue()
            self.completed_tasks.append(task)

    def pop_task_and_add_to_rework(self):
        task = self.all_tasks.from_queue()
        return self.rework_tasks.to_queue(task)


task_board = TaskBoard()


def print_task_board_info(task_board, message=''):
    print(message + ':')
    print('all tasks:', end=' ')
    print(*task_board.all_tasks.elems)
    print('rework tasks:', end=' ')
    print(*task_board.rework_tasks.elems)
    print('completed tasks tasks:', end=' ')
    print(*task_board.completed_tasks)


task_board.add_task('task1')
task_board.add_task('task2')
task_board.add_task('task3')
task_board.add_task('task4')
task_board.add_task('task5')
print_task_board_info(task_board, 'initial state')
task_board.pop_task_and_complete()
task_board.pop_task_and_complete()
print_task_board_info(task_board, 'after pop 2 tasks and complete')
task_board.pop_task_and_add_to_rework()
task_board.pop_task_and_add_to_rework()
print_task_board_info(task_board, 'after pop 2 tasks and add to rework')
task_board.pop_task_from_rework_and_complete()
task_board.pop_task_from_rework_and_complete()
print_task_board_info(task_board, 'after pop 2 tasks and add to rework')
