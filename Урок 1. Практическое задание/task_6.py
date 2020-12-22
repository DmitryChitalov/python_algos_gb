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
from queue import QueueClass


class Trello():
    def __init__(self):
        self.to_do = QueueClass()
        self.ready_4qa = QueueClass()
        self.done_tasks = QueueClass()

    def add_task(self, task):
        self.to_do.to_queue(task)  # добавили новую задачу в беклог
        return print(f'Задача "{task}"  добавлена, {self.to_do.size()} в работе')

    def move_to_qa(self):
        task = self.to_do.from_queue()  # взяли готовую задачку
        self.ready_4qa.to_queue(task)  # отдали собственно на тестирование
        return print(f'Задача "{task}" передана на тестирование, {self.ready_4qa.size()} в тестировании')

    def move_to_done(self):
        task = self.ready_4qa.from_queue()   # взяли проверенную задачку
        self.done_tasks.to_queue(task)   # перенесли в готовые
        return print(f'Задача "{task}" проверена, {self.done_tasks.size()} готово')

    def revert_to_dev(self):
        task = self.ready_4qa.from_queue()  # взяли плохо работающию задачку
        self.to_do.to_queue(task)  # вернули в туду
        return print(f'Задача "{task}" возвращена на доработку, {self.to_do.size()} в работе')


if __name__ == '__main__':
    my_board = Trello()
    my_board.add_task('сделать задание 6')
    my_board.add_task('task')
    my_board.add_task('refactoring')
    my_board.add_task('code review')
    my_board.add_task('backlog grooming')
    # заполнили to_do
    my_board.move_to_qa()
    my_board.move_to_qa()
    my_board.move_to_done()
    my_board.revert_to_dev()
    my_board.move_to_qa()
    my_board.move_to_done()

    # вроде работает
