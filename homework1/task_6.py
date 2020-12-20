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

class QueueTask:
    def __init__(self):
        self.elems = []

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def is_solved(self):
        return random.choice([False, True])

main_queue = QueueTask()

for i in range(10):
    if main_queue.is_solved():
        main_queue.to_queue(str(i + 1) + ' task')
    else:
        main_queue.to_queue(str(i+1) + ' task unsolved')

#print(main_queue)

rework_queue = QueueTask()
for i in range(10):
    print(main_queue)
    first = main_queue.from_queue()
    if 'unsolved' in first:
        rework_queue.to_queue(first)

print('main_queue = ' + str(main_queue))
print('rework_queue = ' + str(rework_queue))