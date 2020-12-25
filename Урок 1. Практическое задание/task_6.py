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

# класс очереди

class TaskQueue():
    def __init__(self):
        """ Конструктор объекта"""
        self.elems = []
        return

    def is_empty(self):
        """ Проверка на пустоту"""
        return self.elems == []

    def to_queue(self, n_item):
        """ Добавление нового элемента в очередь"""
        self.elems.insert(0, n_item)
        return
    
    def from_queue(self):
        if self.is_empty() == False:
            return self.elems.pop()
        else: 
            return

    def current_item(self):
        """ Выводит значение первого  в очереди (последний в списке) элемента"""
        if self.is_empty() == False:
            return self.elems[-1]
        else:
            return

    def items(self):
        """Гетер возвращает список элементов в очереди """
        return self.elems
    
    def size(self):
        """ Размер очереди """
        return len(self.elems)

# класс менеджер задач

class TaskHandler():
    def __init__(self):
        """ Конструктор класса"""
            
        # инициализируем очереди задач
        self.basicTasks = TaskQueue() # Базовые задачи 
        self.closedTasks = TaskQueue() # Решенные задачи
        self.unclosedTasks = TaskQueue() # Задачи на доработке

        return

    def add_basic_task(self, task_name):
        """ Добавляем задачу в список бызовых (вновь поступившая)"""
        self.basicTasks.to_queue(task_name)
        return

    def basic_to_closed_task(self):
        """ Перемещает базовую задачу в список решенных"""
        self.closedTasks.to_queue(self.basicTasks.from_queue())
        return

    def basic_to_unclosed_task(self):
        """Перемещает базовую задачу в список на доработку """
        self.unclosedTasks.to_queue(self.basicTasks.from_queue())
        return

    def unclosed_to_closed_task(self):
        """ Перемещает задачу из доработки в завершенные"""
        self.closedTasks.to_queue(self.unclosedTasks.from_queue())
        return

    def get_current_basic_task(self):
        """ Текущая базовая задача"""
        return self.basicTasks.current_item()
    
    def get_current_unclosed_task(self):
        """ Teкущая задача из отправленных на доработку"""
        return self.unclosedTasks.current_item()

    # Гетеры возращающие списки задач

    def get_all_tasks(self):
        return {'Basic': self.basicTasks.items(), 
                'Unclosed': self.unclosedTasks.items(),
                'Closed': self.closedTasks.items()}

    def get_task_list(self, key = 'Basic'):
        """ Возвращает список задач заданного класса key"""
        return get_all_tasks().get(key)


# клиентская часть программы

if __name__ == '__main__':

    my_tasks = TaskHandler()

    #определяем задачи
    my_tasks.add_basic_task('Cделать первую домашку по алгоритмам')
    my_tasks.add_basic_task('Cделать первую домашку по линейке')
    my_tasks.add_basic_task('Cделать вторую домашку по алгоритмам')
    my_tasks.add_basic_task('Cделать вторую домашку по линейке')

    print('Выводим текущую базовую задачу  ',my_tasks.get_current_basic_task())
    my_tasks.basic_to_unclosed_task() # отправляем в доработку
    my_tasks.basic_to_closed_task() # закрываем следующую задачу

    print('Выводим текущую базовую задачу  ', my_tasks.get_current_basic_task())
    my_tasks.basic_to_closed_task() # решили еще задачу

    print('Выводим все очереди задач \n', my_tasks.get_all_tasks())


