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
        self.elements_list = []

    def is_empty(self):
        return self.elements_list == []

    def to_queue(self, item):
        self.elements_list.insert(0, item)

    def from_queue(self):
        return self.elements_list.pop()

    def get_item(self):
        return self.elements_list[-1]

    def size(self):
        return len(self.elements_list)


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
        print(f'На доработку отправлена: {task}')
        self.other_tasks.to_queue(task)

    def get_task(self):
        task = self.base_tasks.get_item()
        return task

    def count_task(self):
        return self.base_tasks.size(), self.other_tasks.size(), len(self.closed_tasks)


ExObject = Kanban()

while 1 == 1:
    to_base_q, to_rework_q, done_q = ExObject.count_task()
    print(f'В базовой очереди: {to_base_q} задач\nНа доработку: {to_rework_q}\nЗадач уже выполнено: {done_q}')
    try:
        print(f'Что будем делать с задачей: {ExObject.get_task()}?')
    except IndexError:
        print('Задач пока нет')
    option = input(f'Добавить задачу - нажмите 1, отметить как решенную - 2, на доработку - 3, выход - 4: ')
    if len(option) == 0:
        break
    if option == "1":
        ExObject.add_task(input('Введите задачу:   '))
    elif option == "2":
        try:
            ExObject.close_task()
        except IndexError:
            print('Сначала добавь задачу')
    elif option == "3":
        try:
            ExObject.rework_task()
        except IndexError:
            print('Сначала добавь задачу')
    elif option == "4":
        break
    else:
        print('Неверная команда!')
