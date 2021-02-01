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


class TaskList:
    basic: list = []
    solved: list = []
    revision: list = []
    last_number: int = 0

    def add_task(self, task_name):
        self.last_number = self.last_number + 1
        task = {"id": self.last_number, "task_name": task_name}
        self.basic.append(task)

    def send_to_revision(self, task_id):

        for i, item in enumerate(self.basic):
            if item["id"] == task_id:
                self.revision.append(item)
                self.basic.pop(i)
                break

    def solved_task(self, task_id):
        for i, item in enumerate(self.basic):
            if item["id"] == task_id:
                self.solved.append(item)
                self.basic.pop(i)
                break

    def __str__(self):
        res = "Basic:\n\r"
        for item in self.basic:
            res += str(item) + "\n\r"
        res += "Revision:\n\r"
        for item in self.revision:
            res += str(item) + "\n\r"
        res += "Solved:\n\r"
        for item in self.solved:
            res += str(item) + "\n\r"
        return res


task_list = TaskList()
for i in range(5):
    task_list.add_task("задача №" + str(i + 1))

print(task_list)
print("------------------")

task_list.send_to_revision(3)
task_list.send_to_revision(1)
task_list.send_to_revision(3)

print(task_list)
print("------------------")

task_list.solved_task(4)
task_list.solved_task(5)

print(task_list)
print("------------------")
