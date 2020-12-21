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

import random


class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, element):
        self.__queue.append(element)

    def dequeue(self):
        if len(self.__queue) == 0:
            return None
        el = self.__queue[0]
        self.__queue = self.__queue[1:]

        return el


class Tasks:
    def __init__(self):
        self.__todo = Queue()
        self.__retry = Queue()
        self.__done = []

    def run(self):
        for i in range(0, 15):
            self.__todo.enqueue(f'task {i}')

        while True:
            task = self.__todo.dequeue()
            if task is None:
                break

            print('processing task:', task)
            if random.randint(0, 10) < 5:
                print('task failed, will be retried later')
                self.__retry.enqueue(task)
                continue
            self.__done.append(task)

        while True:
            task = self.__retry.dequeue()
            if task is None:
                break

            print('retrying task:', task)
            self.__done.append(task)

    def result(self):
        return self.__done


t = Tasks()
t.run()
print(t.result())
