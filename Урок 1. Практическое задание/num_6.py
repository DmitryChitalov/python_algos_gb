"""
Задание 6.
Задание на закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доски задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) обычно, откуда берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После структуры, проверьте ее работу на различных сценариях
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

class TaskBoard():
    def __init__(self):
        self.original_queue = QueueClass()    # общая очередь
        self.raw_queue = QueueClass()     # необработанная очередь
        self.resolved = []      # решенные

    def task_arrival(self, item):       # поступление задачи
        self.original_queue.to_queue(item)


    def moving_to_unprocessed(self):        # переьещение в необработанные
        task = self.original_queue.from_queue()
        self.raw_queue.to_queue(task)

    def moving_to_resolved(self):            # перемещение в решенные и удаление из необраюотанной очереди
        task = self.raw_queue.from_queue()
        self.resolved.append(task)

    def from_raw_to_original(self):          # из необработанных в общую в случае нерешения
        task = self.raw_queue.from_queue()
        self.original_queue.to_queue(task)

    def total_original_queue(self):          # количество общей очереди
        return self.original_queue.size()


    def total_raw_queue(self):        # количество необработанной очереди
        return self.raw_queue.size()

    def total_resolevd(self):
        return self.total_original_queue() - self.total_raw_queue()


if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.task_arrival('task_1')
    task_board.task_arrival('task_2')
    task_board.task_arrival('task_3')
    task_board.task_arrival('task_4')
    print(f'количество общей очереди: {task_board.total_original_queue()}')
    task_board.moving_to_unprocessed()    # перемещение в нерешенные
    print(f'количество нерешенных задач: {task_board.total_raw_queue()}')
    task_board.moving_to_unprocessed()    # перемещение в нерешенные
    print(f'количество нерешенных задач: {task_board.total_raw_queue()}')
    task_board.moving_to_resolved()    # перемещение в решенные
    print(f'количество решенных задач: {task_board.total_resolevd()}')
    print(f'количество нерешенных задач: {task_board.total_raw_queue()}')
    task_board.task_arrival('task_5')
    print(f'количество общей очереди: {task_board.total_original_queue()}')
    task_board.task_arrival('task_6')
    print(f'количество общей очереди: {task_board.total_original_queue()}')
    task_board.moving_to_unprocessed()  # перемещение в нерешенные
    print(f'количество общей очереди: {task_board.total_original_queue()}')
    task_board.moving_to_resolved()  # перемещение в решенные
    print(f'количество решенных задач: {task_board.total_resolevd()}')
    print(f'количество общей очереди: {task_board.total_original_queue()}')
    print(f'количество нерешенных задач: {task_board.total_raw_queue()}')
