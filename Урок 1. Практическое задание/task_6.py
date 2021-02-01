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


class TaskTracker:
    def __init__(self):
        self.assigned_tasks = QueueClass()
        self.completed_tasks = QueueClass()
        self.postponed_tasks = QueueClass()

    def solve_cur_task(self):
        if not self.assigned_tasks.is_empty():
            task = self.assigned_tasks.from_queue()
            self.completed_tasks.to_queue(task)
        else:
            print('Everything is already done!')

    def postpone_cur_task(self):
        if not self.assigned_tasks.is_empty():
            task = self.assigned_tasks.from_queue()
            self.postponed_tasks.to_queue(task)
        else:
            print('Nothing to postpone!')

    def regain_top_postponed_task(self):
        if not self.postponed_tasks.is_empty():
            task = self.postponed_tasks.from_queue()
            self.assigned_tasks.to_queue(task)
        else:
            print('No postponed tasks')

    def assign_task(self, task):
        self.assigned_tasks.to_queue(task)

    def current_task(self):
        if self.assigned_tasks.is_empty():
            print('Everything is already done!')
        else:
            return self.assigned_tasks.elems[-1]

    def top_postponed_task(self):
        if self.postponed_tasks.is_empty():
            print('No postponed tasks')
        else:
            return self.postponed_tasks.elems[-1]


tt = TaskTracker()
tt.assign_task('Homework')
tt.assign_task('Feature development')
print(tt.current_task())
tt.postpone_cur_task()
print(tt.current_task())
print(tt.top_postponed_task())
tt.solve_cur_task()
tt.solve_cur_task()
tt.regain_top_postponed_task()
print(tt.current_task())
print(tt.top_postponed_task())