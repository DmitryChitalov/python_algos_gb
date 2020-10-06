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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class Task:
    pass


if __name__ == '__main__':
    todo = QueueClass()  # очередь задач
    tofix = QueueClass()  # очередь на доработку
    solved = []  # список решеных задач

    # создаем задачи
    task_1 = Task()
    task_2 = Task()
    task_3 = Task()
    task_4 = Task()
    task_5 = Task()

    # наполняем очередь задачами
    todo.to_queue(task_1)
    todo.to_queue(task_2)
    todo.to_queue(task_3)
    todo.to_queue(task_4)
    todo.to_queue(task_5)

    print(todo.size(), tofix.size(), len(solved))

    # решаем три задачи из очереди, а четвертую и пятую отправляем на доработку
    solved.append(todo.from_queue())
    solved.append(todo.from_queue())
    solved.append(todo.from_queue())
    tofix.to_queue((todo.from_queue()))
    tofix.to_queue((todo.from_queue()))

    print(todo.size(), tofix.size(), len(solved))
