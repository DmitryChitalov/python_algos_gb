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

class Queue:

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def put_in_queue(self, elem):
        self.elems.insert(0, elem)

    def remove_from_queue(self):
        return self.elems.pop()

    def size_queue(self):
        return len(self.elems)

    def __str__(self):
        for elem in self.elems:
            print(elem)
        print('\n')

    def __repr__(self):
        return str(self.elems)

class agileDashboard:

    def __init__(self):
        self.TODO = Queue()
        self.INPROGRESS = Queue()
        self.INTEST = Queue()
        self.DONE = Queue()

    def add_in_todo(self,task):
        self.TODO.put_in_queue(task)

    def move_task_to_progress(self):
        try:
            self.INPROGRESS.put_in_queue(self.TODO.remove_from_queue())
        except:
            print('not task in todo')

    def move_task_to_test(self):
        try:
            self.INTEST.put_in_queue(self.INPROGRESS.remove_from_queue())
        except:
            print('not task in inprogress')
    def move_task_to_done(self):
        try:
            self.DONE.put_in_queue(self.INTEST.remove_from_queue())
        except:
            print('not task in intest')

    def show_todo_tasks(self):
        self.TODO.__str__()

    def show_inprogress_tasks(self):
        self.INPROGRESS.__str__()

    def show_intest_tasks(self):
        self.INTEST.__str__()

    def show_done_tasks(self):
        self.DONE.__str__()

    def get_count_done_tasks(self):
        return self.DONE.size_queue()

myagileboard = agileDashboard()

myagileboard.add_in_todo('task1')
myagileboard.add_in_todo('task2')
print(myagileboard.show_todo_tasks())
myagileboard.move_task_to_progress()
print(myagileboard.show_todo_tasks())
print(myagileboard.show_inprogress_tasks())
myagileboard.move_task_to_progress()
myagileboard.move_task_to_progress()
myagileboard.move_task_to_test()
myagileboard.move_task_to_test()
myagileboard.move_task_to_done()
print(myagileboard.get_count_done_tasks())