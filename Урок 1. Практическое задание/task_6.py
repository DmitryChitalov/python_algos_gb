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

"""Три доски. Добавлять задание можно только в доску Base. Из доски Base можно
первый добавленный элемент переместить или в доску revision, или в доску finished
Из доски revision можно переместить в доску finished первый добавленный элемент"""
class DeskQueue:
    def __init__(self):
        self.base = []
        self.revision = []
        self.finished = []

    def add_task(self, task):
        self.base.append(task)

    def to_revision(self):
        self.revision.append(self.base.pop(0))

    def to_finished(self):
        self.finished.append(self.base.pop(0))

    def from_revision_to_finished(self):
        self.finished.append(self.revision.pop(0))

    def show_task(self):
        print(self.base)

    def show_revision(self):
        print(self.revision)

    def show_finished(self):
        print(self.finished)


desk = DeskQueue()

desk.add_task('1')
desk.add_task('2')
desk.add_task('3')
desk.add_task('4')
desk.add_task('5')
desk.add_task('6')
desk.add_task('7')
desk.add_task('8')
desk.add_task('9')
desk.add_task('10')
desk.to_revision()
desk.to_revision()
desk.to_revision()
desk.show_task()
desk.show_revision()
desk.from_revision_to_finished()
desk.from_revision_to_finished()
desk.show_revision()
desk.show_finished()
desk.to_finished()
desk.to_finished()
desk.show_finished()
desk.show_task()