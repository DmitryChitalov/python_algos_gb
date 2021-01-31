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

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

class Kanban:
    def __init__(self):
        self.base_tasks = QueueClass()
        self.other_tasks = QueueClass()
        self.closed_tasks = []

    def add_task(self, task):
        self.base_tasks.to_queue(task)

    def close_task(self):
        task = self.base_tasks.from_queue()
        self.closed_tasks.append(task)
        return task

    def rework_task(self):
        task = self.base_tasks.from_queue()
        self.other_tasks.to_queue(task)

    def count_task(self):
        return self.base_tasks.size(), self.other_tasks.size(), len(self.closed_tasks)


ExObj = Kanban()

while 1 == 1:
    x, y, z = ExObj.count_task()
    print(f'Сейчас у нас в базовой очереди: {x} задач, на доработку: {y} задач и {z} задач уже выполнено!')
    opt = input(f'Если хотите добавить задачу - нажмите 1, отметить как решенную - 2, перевести в доработку - 3: ')
    if len(opt) == 0:
        break
    if opt == "1":
        ExObj.add_task(input('Введите задачу:   '))
    elif opt == "2":
        ExObj.close_task()
    elif opt == "3":
        ExObj.rework_task()
    else:
        print('Неверная команда!')
