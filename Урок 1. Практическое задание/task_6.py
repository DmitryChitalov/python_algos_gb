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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def put_in_queue(self, elem):
        self.elems.insert(0, elem)

    def remove_from_queue(self):
        return self.elems.pop()

    def size_queue(self):
        return len(self.elems)

    def __str__(self):
        for elem in self.elems:
            print(elem)
        print('\n')

    def __repr__(self):
        return str(self.elems)


class TaskBoard:

    def __init__(self):
        self.tasks = Queue() # очередь задач на выполнение
        self.tasks_for_verification = Queue() # очередь задач на проверку
        self.tasks_for_revision = Queue() # очередь задач на доработку
        self.completed_tasks = Queue() # завершённые задачи

    def add_current_task(self, task):
        self.tasks.put_in_queue(task)

    def from_tasks_to_verification(self):
        task = self.tasks.remove_from_queue()
        self.tasks_for_verification.put_in_queue(task)

    def from_verification_to_revision(self):
        task = self.tasks_for_verification.remove_from_queue()
        self.tasks_for_revision.put_in_queue(task)

    def from_verification_to_completed(self):
        task = self.tasks_for_verification.remove_from_queue()
        self.completed_tasks.put_in_queue(task)

    def from_revision_to_verification(self):
        task = self.tasks_for_revision.remove_from_queue()
        self.tasks_for_verification.put_in_queue(task)

    def from_revision_to_completed(self):
        task = self.tasks_for_revision.remove_from_queue()
        self.completed_tasks.put_in_queue(task)

    def show_current_tasks(self):
        self.tasks.__str__()

    def get_count_current_tasks(self):
        return self.tasks.size_queue()

    def get_completed_tasks(self):
        return self.completed_tasks.__repr__()

    def get_count_completed_tasks(self):
        return self.completed_tasks.size_queue()


if __name__ == '__main__':
    test_board = TaskBoard()
    test_board.add_current_task('Проснуться')
    test_board.add_current_task('Умыться')
    test_board.add_current_task('Почистить зубы')
    test_board.add_current_task('Позавтракать')
    test_board.show_current_tasks()
    test_board.from_tasks_to_verification()
    test_board.from_tasks_to_verification()
    test_board.from_tasks_to_verification()
    test_board.show_current_tasks()
    print(test_board.get_count_current_tasks())
    test_board.from_verification_to_completed()
    test_board.from_verification_to_revision()
    test_board.from_verification_to_revision()
    test_board.from_revision_to_completed()
    test_board.from_revision_to_completed()
    test_board.show_current_tasks()
    print(test_board.get_completed_tasks())









