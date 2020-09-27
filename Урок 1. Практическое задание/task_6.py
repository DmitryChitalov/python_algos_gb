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

class QueueTasksClass:
    def __init__(self):
        self.tasks = []

    def is_empty(self):
        return self.tasks == []

    def show_elems_from_queue(self):
        for el in self.tasks:
            print(f'- {el}')

    def to_base_queue(self, item):
        self.tasks.insert(0, item)

    def from_base_queue_to_another(self, other):
        el = self.tasks.pop()
        other.tasks.insert(0, el)

    def size(self):
        return len(self.tasks)


base_queque = QueueTasksClass() # создаем основную очередь
revision_list = QueueTasksClass() # создаем очередь доработки
done_list = QueueTasksClass() # создаем очередь выполненных заданий

# наполняем основную очередь задачами

base_queque.to_base_queue('first task')
base_queque.to_base_queue('second task')
base_queque.to_base_queue('third task')
base_queque.to_base_queue('one more task')
base_queque.to_base_queue('very hard task')

# проверяем количество элментов каждой очереди и смотрим сами элементы
print(f'Базовая очередь имеет: {base_queque.size()} элементов')
base_queque.show_elems_from_queue()
print(f'Очередь доработки имеет: {revision_list.size()} элементов')
revision_list.show_elems_from_queue()
print(f'Очередь доработки имеет: {done_list.size()} элементов')
done_list.show_elems_from_queue()

# сразу отправляем первую задачку из основной очереди на доработку
base_queque.from_base_queue_to_another(revision_list)

# проверяем как это выглядит
print('----------------------')
print(f'Базовая очередь имеет: {base_queque.size()} элементов')
base_queque.show_elems_from_queue()
print(f'Очередь доработки имеет: {revision_list.size()} элементов')
revision_list.show_elems_from_queue()
print(f'Очередь выполненных задач имеет: {done_list.size()} элементов')
done_list.show_elems_from_queue()

# отправляем следующую задачу из основной очереди в список сделанных
base_queque.from_base_queue_to_another(done_list)

# отправляем следующую задачку из основной очереди на доработку
base_queque.from_base_queue_to_another(revision_list)

# отправляем следующую задачу из основной очереди в список сделанных
revision_list.from_base_queue_to_another(done_list)

# проверяем результат
print('-------------------------')
print('Result: \n')
print(f'Базовая очередь имеет: {base_queque.size()} элементов')
base_queque.show_elems_from_queue()
print(f'Очередь доработки имеет: {revision_list.size()} элементов')
revision_list.show_elems_from_queue()
print(f'Очередь выполненных задач имеет: {done_list.size()} элементов')
done_list.show_elems_from_queue()