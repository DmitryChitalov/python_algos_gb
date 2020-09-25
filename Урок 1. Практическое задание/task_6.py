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
class queue:
    def __init__(self):
        self.el = []

    def to_(self, el):
        self.el.insert(0, el)

    def from_(self):
        return self.el.pop()

    def size(self):
        return len(self.el)

    def check(self, el):
        try:
            self.el.index(el)
            return True
        except ValueError:
            return False


class task:
    def __init__(self):
        self.base_works = queue()
        self.upd_works = queue()
        self.tasks = []

    def ready_task(self, task_):
        if self.base_works.check(task_):
            task_ = self.base_works.from_()
            self.tasks.append(task_)
            print(f'The {task_} has done')
        else:
            print(f'No such {task_} has found')

    def add_task(self, task_in):
        self.base_works.to_(task_in)

    def curr_tasks(self):
        return self.base_works.el

    def add_to_upd(self, task_):
        if self.base_works.check(task_):
            task_ = self.base_works.from_()
            self.upd_works.to_(task_)
        else:
            print(f'No such {task_} has found in current tasks')

    def curr_upd(self):
        return self.upd_works.el

    def from_upd_to_curr(self):
        task_ = self.upd_works.from_()
        self.base_works.to_(task_)


if __name__ == '__main__':
    tasks = task()
    tasks.add_task('task_1')
    tasks.add_task('task_2')
    print(f'in progress tasks : {tasks.curr_tasks()}')

    tasks.ready_task("task_3")
    print(f'Ready tasks : {tasks.tasks}')
    print(f'in progress tasks : {tasks.curr_tasks()}')
    tasks.add_to_upd('task_1')
    print(f'Tasks on updates : {tasks.curr_upd()}')
    print(f'in progress tasks : {tasks.curr_tasks()}')
    tasks.from_upd_to_curr()
    print(f'Tasks on updates : {tasks.curr_upd()}')
    print(f'in progress tasks : {tasks.curr_tasks()}')