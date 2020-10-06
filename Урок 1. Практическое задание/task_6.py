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

class QueueClass:
    def __init__(self):
        self.tasks = []

    def is_empty(self):
        return self.tasks == []

    def to_queue(self, item):
        print('Новая задача...')
        self.tasks.insert(0, item)

    def from_queue(self):
        print('Задача выполнена.')
        return self.tasks.pop()

    def size(self):
        return len(self.tasks)

def check_tasks(queue):
    return 'Список задач пуст.' if queue.is_empty() else 'За работу!'

if __name__ == '__main__':
    main_queue = QueueClass()
    rework_queue = QueueClass()
    completed = []
    print('Начинается рабочий день.')
    print(check_tasks(main_queue))

    for i in range(10):
        task = 'TODO #' + str(i)
        main_queue.to_queue(task)
    print(check_tasks(main_queue))
    print()

    for i in range(len(main_queue.tasks)):
        task = main_queue.from_queue()
        if random.choice((True, False)):
            print('На доработку.')
            rework_queue.to_queue(task)
        else:
            completed.append(task)
    print()

    print(f'Задач на доработке: {rework_queue.size()}.')
    for i in range(len(rework_queue.tasks)):
        task = rework_queue.from_queue()
        completed.append(task)
    print()

    print(check_tasks(rework_queue))
    print('Сегодня решены:')
    for task in completed:
        print(task)
    print('Рабочий день закончен. Пора домой!')