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
class Dashboard:
    """ Создание очередей задач в разрезе статусов new, revision, in_progress, done"""
    def __init__(self):
        self.tasks = {
            'new': [],
            'revision': [],
            'in_progress': [],
            'done': []
        }

    def _change_status_(self, from_status, to_status):
        """ Берем задачу из очереди статуса from_status, добавляем в очередь to_status """
        self.tasks[to_status].append(self.tasks[from_status][0])
        self.tasks[from_status].pop(0)

    def add_new_task(self,item):
        """ Добавляем новую задачу в очередь new"""
        self.tasks['new'].append(item)

    def get_in_progress(self, from_status):
        """ Добавляем задачу в работу из очереди указанного статуса"""
        self._change_status_(from_status, 'in_progress')

    def resolve_task(self):
        """ Закрываем задачу"""
        self._change_status_('in_progress', 'done')

    def send_for_revision(self, from_status):
        """ Отправляем на доработку из очереди указанного статуса"""
        self._change_status_(from_status, 'revision')

    def view_tasks(self, status):
        """ Выводим очередь задач указанного статусе"""
        return self.tasks.get(status)

    def view_first_task_in_status(self, status):
        """ Выводим первую задачу в очереди указанного статуса"""
        # вывод первой задачи в очереди
        return self.tasks.get(status)[0]


if __name__ == '__main__':

    my_tasks = Dashboard()
    my_tasks.add_new_task('сделать 1')
    my_tasks.add_new_task('сделать 2')
    my_tasks.add_new_task('сделать 3')
    my_tasks.add_new_task('сделать 4')

    print(my_tasks.view_tasks('new'))

    my_tasks.get_in_progress('new')
    my_tasks.get_in_progress('new')

    print(my_tasks.view_tasks('in_progress'))
    print(my_tasks.view_first_task_in_status('in_progress'))

    my_tasks.resolve_task()
    my_tasks.send_for_revision('in_progress')
    print(my_tasks.view_tasks('in_progress'))
