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
        self.base_q = QueueClass()
        self.revision_q = QueueClass()
        self.complited_list = []

    def complited_tasks(self):
        """
    добавляем задачу из базовой очереди 
    в список решенных задач
    """
        self.complited_list.append(self.base_q.from_queue())

    def revision_tasks(self):
        """
    добавляем из базовой очереди задачу в 
    очередь на доработку
    """
        self.revision_q.to_queue(self.base_q.from_queue())

    def revised_tasks(self):
        """
    возращаем доработанные задачи в базовую
    очередь
    """
        self.base_q.to_queue(self.revision_q.from_queue())

    def base_task(self):
        """
    возращает решаемую задачу
    """
        try:
            return self.base_q.elems[len(self.base_q.elems) - 1]
        except IndexError:
            return self.base_q.elems


if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.base_q.to_queue('task_1')
    task_board.base_q.to_queue('task_2')
    task_board.base_q.to_queue('task_3')
    print(task_board.base_q.elems)
    print(task_board.base_task())
    task_board.revision_tasks()
    task_board.revision_tasks()
    task_board.complited_tasks()
    print(task_board.revision_q.elems)
    print(task_board.base_q.elems)
    print(task_board.complited_list)
    task_board.revised_tasks()
    task_board.complited_tasks()
    print(task_board.base_task())
    print(task_board.revision_q.elems)
    print(task_board.base_q.elems)
    print(task_board.complited_list)