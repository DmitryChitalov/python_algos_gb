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


class Jira:
    """Очередь задач"""
    todo: list
    inprogress: list
    torework: list
    done: list

    def __init__(self):
        self.todo = []
        self.inprogress = []
        self.torework = []
        self.done = []

    def take_task(self):
        """Берем задачу в работу"""
        if len(self.todo) > 0:
            res = self.todo.pop()
            self.inprogress.insert(0, res)
            return res
        return False

    def put_task(self, task):
        """Добавляем новую задачу"""
        self.todo.insert(0, task)

    def put_rework(self, task):
        """Отправляем на доработку"""
        succeed = 1
        try:
            self.inprogress.remove(task)
        except ValueError:
            succeed = 0

        if succeed == 1:
            self.torework.insert(0, task)
            return True
        return False

    def put_done(self, task):
        """Задача сделана"""
        succeed1 = 1
        succeed2 = 1

        try:
            self.inprogress.remove(task)
        except ValueError:
            succeed1 = 0
        try:
            self.torework.remove(task)
        except ValueError:
            succeed2 = 0
        if succeed1 ==1 or succeed2 == 1:
            self.done.insert(0, task)
            return True
        return False

    def __str__(self):
        """Вывод очереди задач"""
        res = "Сделать: " + str(self.todo) + \
              "\nВ процессе: " + str(self.inprogress) + \
              "\nДоработать: " + str(self.torework) + \
              "\nГотово: " + str(self.done)
        return res


my = Jira()
for i in range(10):
    my.put_task("task"+str(i))

print(my)

print("Берем в работу задачи")
t1 = my.take_task()
t2 = my.take_task()
t3 = my.take_task()
print(my)

print("Часть выполнена, часть доработать")
my.put_done(t1)
my.put_rework(t3)
print(my)
