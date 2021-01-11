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


import time


class TaskBoard:
    def __init__(self):
        self.on_working = []
        self.to_upgrade = []
        self.done = []

    def push_in_on_working(self, task):
        self.on_working.insert(0, task)

    def push_in_to_done(self):
        if not self.on_working:
            print("Задачи отсутствуют")
        else:
            task = self.on_working.pop()
            self.done.insert(0, task)

    def push_in_to_done_from_to_update(self):
        task = self.to_upgrade.pop()
        self.done.insert(0, task)

    def push_in_to_upgrade_from_on_working(self):
        task = self.on_working.pop()
        self.to_upgrade.insert(0, task)

    def push_in_to_upgrade(self):
        task = self.to_upgrade.pop()
        self.to_upgrade.insert(0, task)

    def take_from_on_working(self):
        if not self.on_working:
            print("Задачи отсутствуют")
            return False
        else:
            x = self.on_working[-1]
            print(f"Работаем над {x}")
            return x

    def take_from_to_upgrade(self):
        if not self.to_upgrade:
            print("Задачи отсутствуют")
            return False
        else:
            x = self.to_upgrade[-1]
            print(f"Работаем над {x}")
            return x

if __name__ == "__main__":

    my_tasks = TaskBoard()

    while True:
        task = input("1 - добавить новую задачу\n2 - взять задачу в работу\n"
                     "3 - взять из доработки\n4 - показать списки дел\n5 - завершить на сегодня\n")

        if task.strip() == '1':
            task = input("Добавьте задачу ")
            my_tasks.push_in_on_working(task)
            print(f"Текущие задачи {my_tasks.on_working}")

        elif task.strip() == '2':
            check = my_tasks.take_from_on_working()
            while check:
                time.sleep(5)
                answer = input("1 - добавить задачу в решенные\n2 - отправить на доработку\n")
                if answer.strip() == '1':
                    my_tasks.push_in_to_done()
                    print(f"Решенные задачи {my_tasks.done}")
                    break
                elif answer.strip() == '2':
                    my_tasks.push_in_to_upgrade_from_on_working()
                    print(f"В доработке {my_tasks.to_upgrade}")
                    break
                else:
                    print("Вы ввели неверное значение")

        elif task.strip() == '3':
            check = my_tasks.take_from_to_upgrade()
            while check:
                time.sleep(5)
                answer = input("1 - добавить задачу в решенные\n2 - вновь отправить на доработку\n")
                if answer.strip() == '1':
                    my_tasks.push_in_to_done_from_to_update()
                    print(f"Решенные задачи {my_tasks.done}")
                    break
                elif answer.strip() == '2':
                    my_tasks.push_in_to_upgrade()
                    print(f"В доработке {my_tasks.to_upgrade}")
                    break
                else:
                    print("Вы ввели неверное значение")

        elif task.strip() == '4':
            print(f"Осталось сделать {my_tasks.on_working}\n"
                  f"В доработке {my_tasks.to_upgrade}\nСделано {my_tasks.done}\n")

        elif task.strip() == '5':
            break
        else:
            print("Вы ввели неверное значение")

    print(f"Осталось сделать {my_tasks.on_working}\n"
          f"В доработке {my_tasks.to_upgrade}\nСделано {my_tasks.done}\n")
