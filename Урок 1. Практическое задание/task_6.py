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
        self.current_tasks = []
        self.executed_tasks = []
        self.revision_tasks = []

    def to_queue(self, item):
        self.current_tasks.insert(0, item)

    def size(self):
        return len(self.current_tasks)

    def view_current(self):
        return self.current_tasks

    def view_executed(self):
        return self.executed_tasks

    def view_revision(self):
        return self.revision_tasks

    def task_solved(self):
        self.executed_tasks.insert(0, self.current_tasks[-1])
        return self.current_tasks.pop()

    def task_rejected(self):
        self.revision_tasks.insert(0, self.current_tasks[-1])
        return self.current_tasks.pop()

    def task_fixed(self):
        self.current_tasks.insert(0, self.revision_tasks[-1])
        return self.revision_tasks.pop()


qc_obj = QueueClass()

# Накидываем задач в очередь
qc_obj.to_queue('task1')
qc_obj.to_queue('task2')
qc_obj.to_queue('task3')
qc_obj.to_queue('task4')
qc_obj.to_queue('task5')
qc_obj.to_queue('task6')

# Просматриваем очереди
print(qc_obj.view_current())
print(qc_obj.view_executed())
print(qc_obj.view_revision())

# Так как это очередь, решил не делать возможность указать что выполнить. Выполняем по очереди вызовом

qc_obj.task_solved()
qc_obj.task_solved()

# Просматриваем очереди
print(qc_obj.view_current())
print(qc_obj.view_executed())
print(qc_obj.view_revision())

# А вот эту задачу отправим на доработку!

qc_obj.task_rejected()

# Просматриваем очереди
print(qc_obj.view_current())
print(qc_obj.view_executed())
print(qc_obj.view_revision())

# Ну и логично было бы реализовать механизм возвращения из доработки в текущую очередь :)

qc_obj.task_fixed()

# Просматриваем очереди
print(qc_obj.view_current())
print(qc_obj.view_executed())
print(qc_obj.view_revision())
