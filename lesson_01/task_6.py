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


class TasksDesk:
    def __init__(self):
        self.base_queue = []
        self.revision_queue = []
        self.complete_queue = []

    def __str__(self):
        return f'Список текущих задач: {self.base_queue}\n' \
               f'Список задач на доработке: {self.revision_queue}\n' \
               f'Список выполненных задач: {self.complete_queue}\n'

    def add_to_base(self, task):
        self.base_queue.insert(0, task)

    def replace_to_revision(self):
        if self.base_queue:
            self.revision_queue.insert(0, self.base_queue.pop())

    def replace_to_complete(self):
        if self.base_queue:
            self.complete_queue.insert(0, self.base_queue.pop())

    def replace_to_base(self):
        if self.revision_queue:
            self.base_queue.insert(0, self.revision_queue.pop())

    def solve_task(self, status):
        self.replace_to_complete() if status == 1 else self.replace_to_revision()

    def size(self):
        return len(self.base_queue), len(self.complete_queue), len(self.revision_queue)


if __name__ == '__main__':

    from random import randint

    # Заполним очередь текущих задач:
    task_desk = TasksDesk()
    for number in range(1, 10):
        task_desk.add_to_base(f'Задание {number:02}')
    print(task_desk)

    # Примем случайное решение по каждой задаче и отправим задачи в решённые или на доработку:
    for _ in range(10):
        task_desk.solve_task(randint(0, 1))
    print(task_desk)

    # Вернём доработанные задачи в очередь текущих задач:
    for _ in range(task_desk.size()[2]):
        task_desk.replace_to_base()
    print(task_desk)

    # Теперь снова примем решение по задачам (пусть они выполнены):
    for _ in range(task_desk.size()[0]):
        task_desk.solve_task(1)
    print(task_desk)
