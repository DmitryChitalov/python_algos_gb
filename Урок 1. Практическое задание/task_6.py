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
    __queues = []
    __current_id = 0
    __completed_tasks = []

    def add_task(self, queue_id, description):
        """Добавление задачи в очередь
        """
        if self.__check_queue_id(queue_id):
            self.__current_id += 1
            self.__queues[queue_id]['tasks'].append({
                'id': self.__current_id,
                'description': description
            })
            return True
        else:
            return False

    def current_task(self, queue_id):
        """Просмотр текущей задачи в очереди
        """
        if self.__check_queue_id(queue_id):
            print(f"\n{'=' * 30}\nТекущая задача в очереди \"{self.__queues[queue_id]['title']}\":\n{'=' * 30}")
            if len(self.__queues[queue_id]['tasks']) > 0:
                task = self.__queues[queue_id]['tasks'][0]
                print(f"{task['id']}: {task['description']}")
            else:
                print('Нет задач')
            print("=" * 30, end='\n\n')
        else:
            print('Такой очереди нет')

    def show_queue_tasks(self, queue_id):
        """Просмотр всех задач очереди
        """
        if self.__check_queue_id(queue_id):
            print(f"\n{'=' * 30}\nЗадачи очереди \"{self.__queues[queue_id]['title']}\" ({queue_id}):\n{'=' * 30}")
            if len(self.__queues[queue_id]['tasks']) > 0:
                for i, task in enumerate(self.__queues[queue_id]['tasks'], 1):
                    print(f"{i}: {task['description']} ({task['id']})")
            else:
                print('В очереди нет задач')
            print("=" * 30, end='\n\n')
        else:
            print('Такой очереди нет')
    
    def create_queue(self, title):
        """Создание очереди
        """
        self.__queues.append({
            'title': title,
            'tasks': []
        })

    def move_task(self, from_id, to_id):
        """Перемещение задачи из одной очереди в другую
        """
        if self.__check_queue_id(from_id) and self.__check_queue_id(to_id) and len(self.__queues[from_id]['tasks']) > 0:
            self.__queues[to_id]['tasks'].append(self.__queues[from_id]['tasks'].pop(0))
            return True
        else:
            return False
    
    def task_completed(self, queue_id):
        """Перемещение задачи из очереди в список выполненных задач
        """
        if self.__check_queue_id(queue_id) and len(self.__queues[queue_id]['tasks']) > 0:
            self.__completed_tasks.append(self.__queues[queue_id]['tasks'].pop(0))
            return True
        else:
            return False

    def show_queues(self):
        """Просмотр всех очередей с количеством задач в них
        """
        print(f"\n{'=' * 30}\nОчереди:\n{'=' * 30}")
        if len(self.__queues) > 0:
            for i, queue in enumerate(self.__queues):
                print(f"{i}: {queue['title']} (Задач: {len(queue['tasks'])})")
        else:
            print("Нет очередей")
        print(f"{'-' * 30}\nЗавершенных задач: {len(self.__completed_tasks)}")

        print("=" * 30, end='\n\n')

    def __check_queue_id(self, queue_id):
        """Проверка на существование очереди
        """
        if len(self.__queues) > queue_id:
            return True
        else:
            return False


###################################

tq = TasksQueue()
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
