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


class QueueClass:
    """
    Создается структура из двух очередей. Первая очередь - для хранения новых задач. Вторая - задач требующих доработки.
    Каждая задача хранится в отдельном словаре, содержащем название задачи и маркер 'is_done', который изначально
    находится в состоянии False. Маркер изменяется методом для задачи, находящейся в конце очереди. Если задача на
    момент извлечения из первой очереди имеет маркер False, она отправляется во вторую очередь на доработку, если True -
    отправляется в список завершенных задач. При извлечении задачи из второй очереди ее флаг меняется на True и задача
    считается доработанной и помещается в список завершенных задач
    """

    def __init__(self):
        self.tasks = []  # очередь для новых задач
        self.completed = []  # список для хранения завершенных задач
        self.revision = []  # очередь для задач, требующих доработки

    def is_empty_tasks(self):
        """Проверяет, есть ли задачи в очереди, которые еще не рассматривались"""
        return self.tasks == []

    def is_empty_revision(self):
        """Проверяет, есть ли рассмотренные задачи, требующие доработки"""
        return self.revision == []

    def to_tasks(self, task):
        """Добавляет новую задачу в первый список задач"""
        self.tasks.insert(0, task)

    def to_done(self):
        """Помечает первую задачу в первой очереди как выполненную"""
        self.tasks[len(self.tasks) - 1]['is_done'] = True

    def from_tasks(self):
        """Извлекает задачу из первого списка. Если она выполнена, отправляет в выполненные. Если нет - на доработку"""
        if self.tasks[len(self.tasks) - 1]['is_done']:
            self.completed.append(self.tasks.pop())
        else:
            self.revision.insert(0, self.tasks.pop())

    def from_revision(self):
        """Извлекает задачу из очереди на доработку и отправляет ее в список завершенных"""
        self.revision[len(self.revision) - 1]['is_done'] = True  # помечает задачу как выполненную
        self.completed.append(self.revision.pop())

    def size_tasks(self):
        """Возвращает количество не рассмотренных задач и задач на доработке"""
        return f'Не рассмотренных задач: {len(self.tasks)}, задач на доработке: {len(self.revision)}'

    def __str__(self):
        """Спикок завершенных задач"""
        return f' Завершенные на данный момент задачи: {self.completed}'


if __name__ == '__main__':
    task_queue = QueueClass()

    # Смотрим изначальное состояние списка выполненных задач
    print(task_queue)

    # Добавляем три новых задачи
    task_queue.to_tasks({'name': 'task1', 'is_done': False})
    task_queue.to_tasks({'name': 'task2', 'is_done': False})
    task_queue.to_tasks({'name': 'task3', 'is_done': False})
    print(task_queue.tasks)
    print('_' * 100)

    # Помечаем первую в очереди задачу как выполненную, извлекаем и помещаем в список выполненных
    task_queue.to_done()
    task_queue.from_tasks()
    print(task_queue)

    # В очереди остались две не рассмотренные задачи
    print(task_queue.tasks)
    print('_' * 100)

    #  Извлекаем первую задачу из очереди, не пометив ее как выполненную. И смотрим состояние очереди на доработку
    task_queue.from_tasks()
    print(task_queue.revision)

    #  Извлекаем задачу из очереди на доработку. Она автоматически попадает в список выполненных
    task_queue.from_revision()
    print(task_queue)
    print(task_queue.revision)
    print('_' * 100)

    # Извлекаем последнюю задачу из первой очереди, не пометив ее, как выполненную
    task_queue.from_tasks()
    print(task_queue)  # список выполненных
    print(task_queue.tasks)  # первая очередь опустела
    print(task_queue.revision)  # последняя извлеченная из первой очереди попала в очередь на доработку
    print('_' * 100)

    task_queue.to_tasks({'name': 'task4', 'is_done': False})  # добавили новую задачу в первую очередь
    print(task_queue.tasks)  # первая очередь
    print('_' * 100)
    # Смотрим кол-во не рассмотренных задач и задач на доработке
    print(task_queue.size_tasks())
