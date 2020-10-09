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
    """Класс описывающий очередь"""

    def __init__(self):
        self.elements = []

    def is_empty(self):
        """Возвращает пустую очередь"""
        return self.elements == []

    def to_queue(self, item):
        """Вставляет задачу в очередь"""
        self.elements.insert(0, item)

    def from_queue(self):
        """Извлекает задачу из очереди"""
        return self.elements.pop()

    def size(self):
        """Возвращает длину очереди"""
        return len(self.elements)


class TaskBoard:
    def __init__(self):
        self.to_do_queue = QueueClass()  # Базовая очередь
        self.to_fix_queue = QueueClass()  # Очередь на доработку
        self.completed_queue = []  # Решенные

    def complete_task(self):
        """Закрывает задачу и добавляет в решенные"""
        task = self.to_do_queue.from_queue()
        self.completed_queue.append(task)

    def to_to_fix_queue(self):
        """Отправляет задачу на доработку"""
        task = self.to_do_queue.from_queue()
        self.to_fix_queue.to_queue(task)

    def to_to_do_queue(self, item):
        """Добавляет задачу в основной список"""
        self.to_do_queue.to_queue(item)

    def from_to_fix_queue(self):
        """Переносит задачу из доработки в текущую очередь"""
        task = self.to_fix_queue.from_queue()
        self.to_do_queue.to_queue(task)

    def current_to_do_task(self):
        """Текущая задача"""
        return self.to_do_queue.elements[len(self.to_do_queue.elements) - 1]

    def current_to_fix_task(self):
        """Задача на доработке"""
        return self.to_fix_queue.elements[len(self.to_fix_queue.elements) - 1]


if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.to_to_do_queue("Task_1")
    task_board.to_to_do_queue("Task_2")
    task_board.to_to_do_queue("Task_3")
    task_board.to_to_do_queue("Task_4")
    task_board.to_to_do_queue("Task_5")
    task_board.complete_task()
    task_board.complete_task()
    task_board.to_to_fix_queue()
    print(f'Основная очередь:\n{task_board.to_do_queue.size()}')
    print(f'Очередь на доработку:\n{task_board.to_fix_queue.size()}')
    print(f'Решенные:\n{task_board.completed_queue}')
