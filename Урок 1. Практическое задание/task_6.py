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

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()


def processing(tasks, revision, completed):
    """ Забирает из очереди задач от самой старой к новой, и распределяет по
    очередям, в зависимости от степени доработки документа"""
    for i in range(len(tasks.elems) - 1, -1, -1):
        if tasks.elems[i]:
            completed.to_queue(tasks.from_queue())
        else:
            revision.to_queue(tasks.from_queue())


def revision_process(revision, completed):
    """Просматривает очередь задач на доработке,
    если задача была доработана, отправляет её к выполненным,
    иначе добавляет снова к задачам"""
    for i in range(len(revision.elems) - 1, -1, -1):
        if revision.elems[i]:
            completed.to_queue(revision.from_queue())
        else:
            tasks.to_queue(revision.from_queue())


revision = QueueClass()
completed = QueueClass()
tasks = QueueClass()
tasks.elems = [x % 2 == 0 for x in range(30)]  # создаем массив для обработки
processing(tasks, revision, completed)  # обработка
print(tasks.elems, completed.elems, revision.elems, sep='\n')
for i in range(1, 10, 2):  # допустим некоторые задачи были доработаны
    revision.elems[i] = True
revision_process(revision, completed)  # отправим доработанные к выполненным
print(revision.elems, completed.elems, sep='\n')
