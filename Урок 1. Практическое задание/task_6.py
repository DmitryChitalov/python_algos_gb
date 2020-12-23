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
        self.all_el = []

    def in_line(self, item):
        self.all_el.insert(0, item)

    def from_line(self):
        return self.all_el.pop()

    def queue_size(self):
        return len(self.all_el)


class TaskBoardClass:
    def __init__(self):
        self.base_queue = QueueClass()  # базовая
        self.correction_queue = QueueClass()  # для коррекции
        self.complete = []  # завершенные

    def base_task(self, item):
        self.base_queue.in_line(item)  # добавляем

    def correction_task(self):
        task = self.base_queue.from_line()  # забираем
        self.correction_queue.in_line(task)  # переносим

    def complete_task(self):
        task = self.base_queue.from_line()  # забираем
        self.complete.append(task)  # заносим в завершенные

    def from_correct(self):
        task = self.correction_queue.from_line()  # из коррекции забираем
        self.base_queue.in_line(task)  # ставим в текущие

    def current_task(self):
        return self.base_queue.all_el[len(self.base_queue.all_el) - 1]


if __name__ == '__main__':
    task_board = TaskBoardClass()
    task_board.base_task('Один')
    task_board.base_task('Два')
    task_board.base_task('Три')
    print(task_board.base_queue.all_el)
    print(task_board.current_task())
    task_board.correction_task()
    print(task_board.correction_queue.all_el)