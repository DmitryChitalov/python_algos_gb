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
        self.elems_unsolved = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)
        
    def to_queue_of_unsolved(self):
        self.elems_unsolved.insert(0, self.elems.pop())
        
    def from_queue_of_unsolved(self):
        return self.elems_unsolved.pop()

    def from_queue(self):
        return self.elems.pop()

    def size_queue(self):
        return len(self.elems)
    
    def size_queue_unsolved(self):
        return len(self.elems_unsolved)


if __name__ == '__main__':
    Task = QueueClass()
    
    for i in range(10):
        Task.to_queue(f'task_{i+1}')
        
    print(Task.from_queue())
    Task.to_queue_of_unsolved()
    Task.to_queue_of_unsolved()
    print(Task.from_queue_of_unsolved())
    print(Task.from_queue())
