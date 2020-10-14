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


class TasksQueue:
    """
    Класс очереди
    """

    def __init__(self, title):
        """
        :param title: Название очереди
        """
        self.__title = title
        self.__tasks = []

    def title(self):
        """
        :return: Возвращает наименование текущей очереди
        """
        return self.__title

    def add_task(self, task_id, description):
        """Добавление задачи в очередь

        :param task_id: ID задачи, присвоенный менеджером очередей
        :param description: Описание задачи
        """
        self.__tasks.append({
            'id': task_id,
            'description': description
        })

    def remove_task(self):
        """Удаление задачи из очереди

        :return: Возвращает удаленную задачу
        """
        if self.tasks_count() > 0:
            return self.__tasks.pop(0)
        else:
            return None

    def current_task(self):
        """Вывод на экран текущей задачи в очереди
        """
        print(f"\n{'=' * 30}\nТекущая задача в очереди \"{self.__title}\":\n{'=' * 30}")
        if self.tasks_count() > 0:
            print(f"{self.__tasks[0]['id']}: {self.__tasks[0]['description']}")
        else:
            print('Нет задач')
        print("=" * 30, end='\n\n')

    def tasks_show(self):
        """Вывод на экран всех задач из очереди

        """
        print(f"\n{'=' * 30}\nЗадачи очереди \"{self.__title}\":\n{'=' * 30}")
        if self.tasks_count() > 0:
            for i, task in enumerate(self.__tasks, 1):
                print(f"{i}: {task['description']} ({task['id']})")
        else:
            print('В очереди нет задач')
        print("=" * 30, end='\n\n')

    def tasks_count(self):
        """
        :return: Возвращает количество задач в очереди
        """
        return len(self.__tasks)


class Queues:
    """
    Класс для управления очередями
    """
    __last_task_id = 0

    def __init__(self):
        self.__queues = []
        self.__completed_tasks = []

    def create_queue(self, title):
        """Создание очереди

        :param title: Наименование очереди
        """
        self.__queues.append(TasksQueue(title))

    def show_queues(self):
        """Просмотр всех очередей с количеством задач в них
        """
        print(f"\n{'=' * 30}\nОчереди:\n{'=' * 30}")
        if len(self.__queues) > 0:
            for i, queue in enumerate(self.__queues):
                print(f"{i}: {queue.title()} (Задач: {queue.tasks_count()})")
        else:
            print("Нет очередей")
        print(f"{'-' * 30}\nЗавершенных задач: {len(self.__completed_tasks)}")

        print("=" * 30, end='\n\n')

    def add_task(self, queue_id, description):
        """Добавление задачи в очередь

        :param queue_id: Индекс очереди, в которую добавляется задача
        :param description: Описание добавляемой задачи
        :return: Возвращает True или False в зависимости от результата
        """
        if self.__check_index(queue_id):
            self.__last_task_id += 1
            self.__queues[queue_id].add_task(self.__last_task_id, description)
            return True
        else:
            return False

    def current_task(self, queue_id):
        """Просмотр текущей задачи в очереди

        :param queue_id: Индекс интересуемой очереди
        """
        if self.__check_index(queue_id):
            self.__queues[queue_id].current_task()
        else:
            print('Такой очереди нет')

    def move_task(self, from_id, to_id):
        """Перемещение задачи из одной очереди в другую

        :param from_id: Индекс очереди, из которой забирается задача
        :param to_id: Индекс очереди в которую перемещается задача
        :return: Возвращается True или False в зависимости от результата
        """
        if self.__check_index(from_id) and self.__check_index(to_id):
            task = self.__queues[from_id].remove_task()
            if task:
                self.__queues[to_id].add_task(task['id'], task['description'])
                return True
            else:
                return False
        else:
            return False

    def task_completed(self, queue_id):
        """Перемещение задачи из очереди в список выполненных задач

        :param queue_id: Индекс очереди, из которой забирается задача
        :return: Возвращается True или False в зависимости от результата
        """
        if self.__check_index(queue_id):
            task = self.__queues[queue_id].remove_task()
            if task:
                self.__completed_tasks.append(task)
                return True
            else:
                return False
        else:
            return False

    def show_queue_tasks(self, queue_id):
        """Просмотр всех задач очереди

        :param queue_id: Индекс очереди, задачи которой вывести на экран
        """
        if self.__check_index(queue_id):
            self.__queues[queue_id].tasks_show()
        else:
            print('Такой очереди нет')

    def __check_index(self, queue_id):
        """Проверка на существование очереди

        :param queue_id: Индекс очереди, которую необходимо проверить на наличие
        :return: Возвращает True или False в зависимости от результата
        """
        if len(self.__queues) > queue_id:
            return True
        else:
            return False


###################################

tq = Queues()
tq.show_queues()

# Добавляем задачи в очередь (очередь еще не создана)
print(tq.add_task(1, 'Создать задачу'))
# Просмотр задач несуществуюущей очереди
tq.show_queue_tasks(1)

# Создаем очереди
tq.create_queue('План')
tq.create_queue('В работе')
tq.create_queue('На доработку')
tq.show_queues()

# Добавляем задачи в очередь
tq.add_task(0, 'Создать задачу')
tq.add_task(0, 'Глобальный улучшайзинг')
tq.add_task(0, 'Корпоратив')
tq.add_task(1, 'Срочно добавить функционал')
tq.add_task(1, 'уже не так срочно, но сделать')

tq.show_queues()

# Просмотр всех задач в очередях
tq.show_queue_tasks(0)
tq.show_queue_tasks(1)
tq.show_queue_tasks(2)

# Просмотр текущей задачи в очереди
tq.current_task(0)
tq.current_task(1)
tq.current_task(2)

# Перенброс задачи из Плана В работу
tq.show_queue_tasks(0)
tq.show_queue_tasks(1)
tq.show_queue_tasks(2)
tq.move_task(0, 1)
tq.move_task(1, 2)
tq.show_queue_tasks(0)
tq.show_queue_tasks(1)
tq.show_queue_tasks(2)

# Перенос задачи в выполненные
tq.task_completed(1)
tq.show_queue_tasks(1)
tq.show_queues()
