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
        self.done_task = []
        self.hard_task = []

    def is_empty(self):
        return self.elems == [], self.done_task == [], self.hard_task == []

    def insert_to_queue(self, item):
        self.elems.insert(0, item)

    def del_from_queue(self):
        return self.elems.pop()

    def del_from_queue_done(self):
        return self.done_task.pop()

    def del_from_queue_hard(self):
        return self.hard_task.pop()

    def size(self):
        return len(self.elems), len(self.done_task), len(self.hard_task)

    def to_hard(self):
        self.hard_task.insert(0, self.elems.pop())

    def to_done(self):
        self.done_task.insert(0, self.elems.pop())

    def all_queue(self):
        return self.elems, self.done_task, self.hard_task

if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty())  # -> True, True, True. Очередь пустая

    # помещаем объекты в очередь
    qc_obj.insert_to_queue('my_obj')
    qc_obj.insert_to_queue(4)
    qc_obj.insert_to_queue(True)

    print(qc_obj.is_empty())  # -> False, True, True. Очередь не пустая, сложные и выполненые задачи пусты

    print(qc_obj.size())  # -> (3, 0, 0)

    print(qc_obj.del_from_queue())  # -> my_obj

    print(qc_obj.size())        # -> (2, 0, 0)
    print(qc_obj.all_queue())   # -> ([True, 4], [], [])
    qc_obj.to_hard()            # -> Перемещяем задачу в сложные
    print(qc_obj.size())        # -> (1, 0, 1)
    print(qc_obj.all_queue())   # -> ([True], [], [4])

    qc_obj.del_from_queue_hard()  # -> Удаляем из сложной
    print(qc_obj.all_queue())  # -> ([True], [], [])