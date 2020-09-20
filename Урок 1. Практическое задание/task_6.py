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


class BoardClass:
    def __init__(self):
        self.main_tasks = []
        self.resolved_tasks = []
        self.remake_tasks = []

    def add_main_task(self, task):
        self.main_tasks.insert(0, task)

    def current_task(self):
        return self.main_tasks[len(self.main_tasks) - 1]

    def main_task_is_resolved(self):
        self.resolved_tasks.insert(0, self.main_tasks.pop())

    def show_resolved_tasks(self):
        print(self.resolved_tasks)

    def main_task_to_remake(self):
        self.remake_tasks.insert(0, self.main_tasks.pop())

    def show_tasks_to_remake(self):
        print(self.remake_tasks)

    def current_remake_task(self):
        return self.remake_tasks[len(self.remake_tasks) - 1]

    def remake_to_resolved(self):
        self.resolved_tasks.insert(0, self.remake_tasks.pop())


if __name__ == '__main__':
    board_1 = BoardClass()
    board_1.add_main_task(1)
    board_1.add_main_task(2)
    board_1.add_main_task(3)
    board_1.add_main_task(4)
    print(board_1.main_tasks)
    print(board_1.current_task())
    board_1.main_task_is_resolved()
    print(board_1.main_tasks)
    board_1.show_resolved_tasks()
    print(board_1.current_task())
    board_1.main_task_to_remake()
    board_1.show_tasks_to_remake()
    board_1.remake_to_resolved()
    board_1.show_resolved_tasks()


