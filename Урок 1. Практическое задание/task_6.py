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


class TaskBoard():
    def __init__(self):
        self.task = []
        self.exec = []

    def push_in(self, task):
        return self.task.insert(0,task)

    def base_exec(self):
        self.exec.append(self.task.pop())
        return self.exec

    def return_exec_task(self):
        return self.task

    def refine_task(self):
        self.task.insert(0,self.task.pop())
        return self.task

class1 = TaskBoard()
for i in range(5):
    class1.push_in(f'task {i}')
print(class1.task)

print(class1.base_exec())
print(class1.return_exec_task())
print(class1.refine_task())
print(class1.base_exec())
print(class1.refine_task())

