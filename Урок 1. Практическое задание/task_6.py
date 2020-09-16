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


class TaskBoard:
    def __init__(self):
        self.main_queue = QueueClass()  # основная очередь
        self.reworking_queue = QueueClass()  # очередь на доработку
        self.completed_list = []  # список решённых задач

    def to_main_queue(self, item):
        self.main_queue.to_queue(item)

    def current_main_task(self):
        return self.main_queue.elems[len(self.main_queue.elems) - 1]

    def to_reworking_task(self):
        task = self.main_queue.from_queue()
        self.reworking_queue.to_queue(task)

    def from_reworking(self):
        task = self.reworking_queue.from_queue()
        self.main_queue.to_queue(task)

    def current_reworking_task(self):
        return self.reworking_queue.elems[len(self.reworking_queue.elems) - 1]

    def to_completed_list(self):
        task = self.main_queue.from_queue()
        self.completed_list.append(task)

    def completed_list(self):
        return self.completed_list


if __name__ == '__main__':
    task_board = TaskBoard()
    print(task_board.main_queue.elems)  # -> []. Очередь пустая

    # наполняем очередь задачами
    task_board.to_main_queue('Task1')
    task_board.to_main_queue('Task2')
    task_board.to_main_queue('Task3')
    task_board.to_main_queue('Task4')
    print(task_board.main_queue.elems)  # -> ['Task4', 'Task3', 'Task2', 'Task1']

    # текущая задача
    print(task_board.current_main_task())  # -> Task1

    # отправляем текущую задачу на доработку
    task_board.to_reworking_task()
    print(task_board.main_queue.elems)  # -> ['Task4', 'Task3', 'Task2']
    print(task_board.reworking_queue.elems)  # -> ['Task1']

    # текущая здача готова
    task_board.to_completed_list()
    print(task_board.completed_list)  # -> ['Task2']
    print(task_board.main_queue.elems)  # -> ['Task4', 'Task3']

    # возвращаем доработанную задачу в основной список
    task_board.from_reworking()
    print(task_board.main_queue.elems)  # -> ['Task1', 'Task4', 'Task3']
    print(task_board.reworking_queue.elems)  # -> []
