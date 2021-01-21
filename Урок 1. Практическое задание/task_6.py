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


class TaskDesc:
    def __init__(self):
        self.first = []
        self.second = []

    def is_empty(self):
        return self.first == self.second == []

    def to_first_queue(self, item):
        self.first.insert(0, item)

    def from_first_queue(self):
        return self.first.pop()

    def to_second_queue(self):
        self.second.insert(0, self.first.pop())

    def from_second_queue(self):
        return self.second.pop()

    def size(self):
        return len(self.first), len(self.second)


if __name__ == '__main__':
    qc_obj = TaskDesc()
    print(qc_obj.is_empty())  # True.
    qc_obj.to_first_queue('my_obj')
    qc_obj.to_first_queue(4)
    print(qc_obj.size())  # (2, 0)
    qc_obj.to_first_queue(True)
    print(qc_obj.is_empty())  # False
    print(qc_obj.size())  # (3, 0)
    qc_obj.to_second_queue()  #
    print(qc_obj.size())  # (2, 1)
    print(qc_obj.from_second_queue())  # my_obj
    print(qc_obj.from_first_queue())  # 4
    print(qc_obj.size())
