"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие нескольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""


class QueueClass:
    new_tasks_index = 0
    inwork_tasks_index = 1
    rework_tasks_index = 2
    finished_tasks_index = 3

    def __init__(self):
        self.elems = [[], [], [], []]

    def is_empty(self):
        return self.elems == [[], [], [], []]

    def is_empty_inner(self, index):
        return self.elems[index] == []

    def size(self):
        return len(self.elems)

    def size_inner(self, index):
        return len(self.elems[index])

    def new_task(self, item):
        self.elems[self.new_tasks_index].insert(0, item)

    def get_task_in_work(self):
        item = self.elems[self.new_tasks_index].pop()
        self.elems[self.inwork_tasks_index].insert(0, item)

    def finish_task(self):
        item = self.elems[self.inwork_tasks_index].pop()
        self.elems[self.finished_tasks_index].insert(0, item)

    def rework_task(self):
        item = self.elems[self.finished_tasks_index].pop()
        self.elems[self.rework_tasks_index].insert(0, item)


if __name__ == '__main__':
    qc_obj = QueueClass()
    print('is empty =>>>', qc_obj.is_empty())  # -> True. Очередь пустая

    # помещаем объекты в очередь
    qc_obj.new_task('first task')
    qc_obj.new_task('second_task')
    qc_obj.new_task('third task')

    print('is empty =>>>', qc_obj.is_empty_inner(qc_obj.new_tasks_index))  # -> False. Очередь пустая

    print('queue size =>>>', qc_obj.size())  # -> 4

    print('new tasks queue size =>>>', qc_obj.size_inner(qc_obj.new_tasks_index))  # -> 3

    qc_obj.get_task_in_work()
    print('new tasks queue size =>>>', qc_obj.size_inner(qc_obj.new_tasks_index))  # -> 2
    print('inwork tasks queue size =>>>', qc_obj.size_inner(qc_obj.inwork_tasks_index))  # -> 1

    qc_obj.get_task_in_work()
    qc_obj.finish_task()
    print('inwork tasks =>>>', qc_obj.elems[qc_obj.inwork_tasks_index])
    print('finished tasks =>>>', qc_obj.elems[qc_obj.finished_tasks_index])

    qc_obj.rework_task()
    print('queue =>>>', qc_obj.elems)
