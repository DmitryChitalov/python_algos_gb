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


class QueueObj:
    def __init__(self):
        self._queue_items = []

    def is_empty(self):
        return self._queue_items == []

    def item_to_queue(self, item):
        self._queue_items.insert(0, item)

    def item_from_queue(self):
        if not self.is_empty():
            return self._queue_items.pop()

    def queue_size(self):
        return len(self._queue_items)

    def queue_list(self):
        return self._queue_items

    def next_item(self):
        if not self.is_empty():
            return self.queue_list()[-1]


class TaskBoard:
    def __init__(self):
        self._queues = {}
        self._priority = []
        self._executed = []

    def is_empty(self):
        return self._queues == {}

    def add_queue(self, name: str):
        if name in self._queues.keys():
            print('Такая очередь задач уже существует')
        self._queues[name] = QueueObj()
        self._priority.append(name)

    def new_task(self, name: str, item: str):
        if name not in self._queues.keys():
            self.add_queue(name)
        self._queues[name].item_to_queue(item)

    def execute_task(self):
        for el in self._priority:
            if self._queues[el].is_empty():
                continue
            self._executed.append(self._queues[el].item_from_queue())
            break

    def change_queue(self, old: str, new: str):
        self._queues[new].item_to_queue(
            self._queues[old].item_from_queue()
        )

    def show_queue(self, name):
        return self._queues[name].queue_list()

    def show_next_task(self, name=None):
        if name is None:
            for el in self._priority:
                if self._queues[el].is_empty():
                    continue
                name = el
                break
        return self._queues[name].queue_list()[-1]

    def queue_is_empty(self, name):
        return self._queues[name].is_empty()

    def executed(self):
        return self._executed

    def task_queues(self):
        return self._queues.keys()


if __name__ == '__main__':

    # Создаём новую доску задач
    NEW_B = TaskBoard()

    # Смотрим, что она пустая
    print('Доска задач пуста:', NEW_B.is_empty())

    # Добавляем новые очереди задач
    NEW_B.add_queue('urgent')
    NEW_B.add_queue('basic')
    NEW_B.add_queue('deferred')

    # Смотрим, что на доске задач появились очереди, но сами очереди пустые
    print('Доска задач пуста:', NEW_B.is_empty())
    print('Очередь задач "urgent" пуста:', NEW_B.queue_is_empty('urgent'))

    # Добавляем задачи в разные очереди
    NEW_B.new_task('urgent', 'do my homework')
    NEW_B.new_task('basic', 'feed fish')
    NEW_B.new_task('urgent', 'go to sleep!')
    NEW_B.new_task('urgent', 'write database')
    NEW_B.new_task('deferred', 'make breakfast')
    NEW_B.new_task('deferred', 'go for a walk')

    # Смотрим, что очередь задач уже не пуста
    print('Очередь задач "urgent" пуста:', NEW_B.queue_is_empty('urgent'))

    # Смена очереди для двух следующих задач

    NEW_B.change_queue('urgent', 'basic')
    NEW_B.change_queue('basic', 'urgent')

    # Смотрим список очередей задач

    print('Список очередей задач на доске задач:', NEW_B.task_queues())

    # Смотрим сами очереди задач
    print('Очередь urgent', NEW_B.show_queue('urgent'))
    print('Очередь basic', NEW_B.show_queue('basic'))
    print('Очередь deferred', NEW_B.show_queue('deferred'))

    # Смотрим следующее задание на доске задач
    print('next task in task board', NEW_B.show_next_task())

    # Смотрим следующее задание в очереди 'basic'
    print('next task in "basic"', NEW_B.show_next_task('basic'))

    # Выполняем задания в порядке приоритета
    NEW_B.execute_task()
    NEW_B.execute_task()
    NEW_B.execute_task()
    NEW_B.execute_task()
    NEW_B.execute_task()
    NEW_B.execute_task()

    # Определяем, что очередь пуста
    print('Очередь задач "urgent" пуста:', NEW_B.queue_is_empty('urgent'))
    print('Очередь задач "basic" пуста:', NEW_B.queue_is_empty('basic'))
    print('Очередь задач "deferred" пуста:', NEW_B.queue_is_empty('deferred'))


    # Смотрим список выполненных заданий
    print(NEW_B.executed())
