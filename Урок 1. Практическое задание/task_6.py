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

from collections import deque

class TaskQueue:
    def __init__(self):
        self.base = deque()
        self.rework = deque()
        self.solved = []
    
    def add(self, task):
        self.base.append(task)
    
    def accept(self):
        task = self.base.popleft()
        self.solved.append(task)

    def reject(self):
        task = self.base.popleft()
        self.rework.append(task)
    
    def revise(self):
        task = self.rework.popleft()
        self.base.append(task)

    # Поскольку мы пишем (и строим графики) слева направо,
    # приходится обращать порядок элементов, чтобы вход в очередь
    # был слева, а выход справа
    def __repr__(self):
        return f"""Base:{
            list(reversed(self.base))
        }, Work:{
            list(reversed(self.rework))
        }, Solved:{
            self.solved
        }"""

tq = TaskQueue()

tq.add('A')
tq.add('B')
tq.add('C')
print(tq)
tq.accept()
print(tq)
tq.reject()
print(tq)
tq.revise()
print(tq)
tq.add('D')
print(tq)
tq.reject()
print(tq)
tq.accept()
print(tq)