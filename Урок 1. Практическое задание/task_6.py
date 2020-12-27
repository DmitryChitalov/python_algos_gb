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

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class Board:
    def __init__(self):
        self.tasks = {
            'initial': QueueClass(),
            'resolving': QueueClass(),
            'solved': QueueClass(),
        }

    def __str__(self):
        my_str = ''
        for key, value in self.tasks.items():
            my_str += str(key) + ':' + str(value) + '\n'
        return my_str

    def to_board(self, queue, el):
        self.tasks[queue].to_queue(el)

    def to_solved(self):
        self.tasks['solved'].to_queue(self.tasks['initial'].from_queue())

    def to_resolving(self):  # Здесь можно отдавать в порядке общей очереди задачи на доработку,
        # что не совсем эффективно, но соответствует условиям задачи
        self.tasks['resolving'].to_queue(self.tasks['solved'].from_queue())


if __name__ == '__main__':
    qc_obj = Board()

    qc_obj.to_board('initial', 'task1')
    qc_obj.to_board('initial', 'task2')
    qc_obj.to_board('initial', 'task2')
    print(qc_obj)
    qc_obj.to_solved()
    print(qc_obj)
    qc_obj.to_board('initial', 'task3')
    qc_obj.to_board('initial', 'task4')
    qc_obj.to_board('initial', 'task5')
    print(qc_obj)
    qc_obj.to_solved()
    qc_obj.to_solved()
    print(qc_obj)
    qc_obj.to_resolving()
    print(qc_obj)
    qc_obj.to_resolving()
    print(qc_obj)
    qc_obj.to_board('initial', 'task6')
    qc_obj.to_board('initial', 'task7')
    qc_obj.to_board('initial', 'task8')
    print(qc_obj)


