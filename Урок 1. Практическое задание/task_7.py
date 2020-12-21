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


class OwnError(Exception):
    """Собственное исключение."""
    def __init__(self, txt):
        self.txt = txt


class TaskBoard:
    """
    Реализция структуры "доска задач" по принципу очереди.

    Структура имеет буфер, для определения дальнейших действий с задачей.
    В буфере в один момент времени может находиться только одна задача
    каждого типа.
    """
    def __init__(self):
        self.__basic_tasks = []
        self.__revision_tasks = []
        # Реализуем буфер в виде словаря для двух видов задач,
        # хотя практическая польза от этого сомнительна, и, возможно, следовало
        # реализовать буфер только на одну задачу.
        self.__tasks_buffer = {'Basic': None, 'Revision': None}
        self.solved_tasks = []

    def is_empty_basic(self):
        """Проверить является ли базовая очередь пустой."""
        return self.__basic_tasks == []

    def is_empty_revision(self):
        """Проверить является ли очередь на доработку пустой."""
        return self.__revision_tasks == []

    def basic_task_adding(self, task):
        """Добвить задачу в базовую очередь."""
        self.__basic_tasks.insert(0, task)

    def consider_basic_task(self):
        """Рассмотреть следующую задачу из базовой очереди."""
        if self.is_empty_basic():
            raise OwnError('Очередь пуста!')
        if self.__tasks_buffer['Basic']:
            raise OwnError('Необходимо определить действия для предыдущей задачи!')
        self.__tasks_buffer['Basic'] = self.__basic_tasks.pop()

    def consider_revision_task(self):
        """Рассмотреть следующую задачу из очереди задач, отправленых на доработку."""
        if self.is_empty_revision():
            raise OwnError('Очередь пуста!')
        if self.__tasks_buffer['Revision']:
            raise OwnError('Необходимо определить действия для предыдущей задачи!')
        self.__tasks_buffer['Revision'] = self.__revision_tasks.pop()

    def solve_task(self, task):
        """Решить задачу.
        Задача будет помещена в список решенных.
        """
        if task in self.__tasks_buffer.values():
            for key, value in self.__tasks_buffer.items():
                if task == value:
                    self.solved_tasks.append(task)
                    self.__tasks_buffer[key] = None
        else:
            raise OwnError('Такая задача в данный момент не рассматривается!')

    def send_task_for_revision(self, task):
        """Отправить задачу на доработку."""
        if task in self.__tasks_buffer.values():
            for key, value in self.__tasks_buffer.items():
                if task == value:
                    self.__revision_tasks.insert(0, task)
                    self.__tasks_buffer[key] = None
        else:
            raise OwnError('Такая задача в данный момент не рассматривается!')

    def basic_tasks_size(self):
        """Вернуть размер очереди базовых задач."""
        return len(self.__basic_tasks)

    def revision_tasks_size(self):
        """Вернуть размер очереди задач, отправленых на доработку."""
        return len(self.__revision_tasks)

    def get_basic_buffer(self) -> object:
        """Вернуть базовую задачу из буфера."""
        return self.__tasks_buffer['Basic']

    def get_revision_buffer(self) -> object:
        """Вернуть из буфера задачу, которая была взята из очереди задач на дороботку."""
        return self.__tasks_buffer['Revision']


if __name__ == '__main__':
    # Создаем класс "доска задач".
    a = TaskBoard()

    # Добавляем 21 задачу в очередь базовых задач.
    for i in range(21):
        a.basic_task_adding(f'Задача{i+1}')

    print('Проверяем размер базовой очереди:')
    print(a.basic_tasks_size())

    # Отправляем на доработку задачи, в названни которых есть цифра "2", остальные довбавляем в список решенных
    for _ in range(a.basic_tasks_size()):
        a.consider_basic_task()
        tsk = a.get_basic_buffer()
        if '2' in tsk:
            a.send_task_for_revision(tsk)
        else:
            a.solve_task(tsk)

    print('\nПробуем взять задачу из пустой очереди:')
    try:
        a.consider_basic_task()
    except OwnError as err:
        print(err)

    print('\nПроверяем размер очереди задач, которые были отправлены на доработку:')
    print(a.revision_tasks_size())
    print('\nСмотрим на список решенных задач:')
    print(a.solved_tasks)
    print('\nПроверяем размер базовой очереди:')
    print(a.basic_tasks_size())

    print('\nПытаемся рассмотреть сразу две задачи из задач на доработку:')
    try:
        a.consider_revision_task()
        a.consider_revision_task()
    except OwnError as err:
        print(err)

    # Решаем задачу из буфера
    a.solve_task(a.get_revision_buffer())
    print('\nСписок решенных задач пополнился задачой номер 2:')
    print('Задача2' in a.solved_tasks)

    print('\nПробуем решить задачу, которая не находится на рассмотрении:')
    try:
        a.solve_task('Задача20')
    except OwnError as err:
        print(err)

# подумать над проблемой дублирования задач