"""
Задание 6.
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

class Kanban:
    # Определяет базу данных как словарь куда будут помещаться задания
    def __init__(self):
        self.board = {
            'Backlog': [],
            'Open': [],
            'Fix': [],
            'Done': [],
        }

    # Добавляет задание в бэклог
    def addTask(self, task):
        self.task = task
        self.board['Backlog'].append(task)

    # Метод который будет использоваться для перемещения заданий между очередями,
    # для определения используется порядковый номер задания в той или иной очереди
    def moveTask(self, queueFrom, queueTo, num):
        if (num > 0) and (num <= len(self.board[queueFrom])):
            openedTask = self.board[queueFrom].pop(num-1)
            self.board[queueTo].append(openedTask)
        elif len(self.board[queueFrom] == 0):
            print(f'{queueFrom} is empty.')
        else:
            print('Task does not exist please double check the number of your task.')

    # Методы которые перемещают задания из одной очереди в другую
    def openTask(self, num):
        self.moveTask('Backlog', 'Open', num)

    def resolveTask(self, num):
        self.moveTask('Open', 'Done', num)

    def fixTask(self, num):
        self.moveTask('Done', 'Fix', num)

    def resolveFixedTask(self, num):
        self.moveTask('Fix', 'Done', num)







a = Kanban()

a.addTask('fix the problem')
print(a.board)
a.addTask('fix the problem')
print(a.board)
a.addTask('add constraint')
print(a.board)
a.addTask('create website')
print(a.board)
a.addTask('create crm')
a.openTask(2)
print(a.board)
a.resolveTask(1)
print(a.board)
a.fixTask(1)
print(a.board)
a.resolveFixedTask(1)
print(a.board)