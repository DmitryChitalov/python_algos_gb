import time
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
#################################################################################


''' В этой структуре данных - очередь. Я не реализововал доставание задачи среди всех, или перемещение какой либо из них,
    кроме первой ибо это уже будет не очередь, а скорее менеджер ежедневных задач
    То есть можно добавить задачу в конец и удалить с начала. Приоритетов нету.
'''

class Queue:
    __general_queue = []
    __done = []
    __temporarily = []

    def __init__(self, task):
        self.__task_text = task
        self.__new_task = [time.time(), self.__task_text]
        Queue.__general_queue.append(self.__new_task)      # Сразу добавляем нашу задачу в список при ее создании

    def show_date(self):
        return print(time.ctime(self.__new_task[0]))

    def all_gen_taks(self):
        print('Current tasks:')
        [print(f'Task: {i[1]} Date: {time.ctime(i[0])}') for i in Queue.__general_queue]

    def mark_as_done(self):
        choise = input(f'Будет отмечена как "Завершенная" эта задача:\n>> {Queue.__general_queue[0][1]} <<\n'
                       f'Чтобы подтвердить, введите "y" и нажмите ENTER\n')
        if choise == 'y':
            Queue.__done.append(Queue.__general_queue.pop(0))
            print('Подтвержденно!')
        else:
            print('Не завершенно')

    def show_dane(self):
        print('Done tasks:')
        [print(f'Task: {i[1]} Date: {time.ctime(i[0])}') for i in Queue.__done]

    def to_temporarily(self):
        Queue.__temporarily.append(Queue.__general_queue.pop(0))
        print('Done')

    def clear_tasks(self):
        Queue.__general_queue.clear()


a = Queue('hello')
a.show_date()
a.all_gen_taks()
a.mark_as_done()
b = Queue('world')
a.all_gen_taks()
a.show_dane()
a.clear_tasks()
a.all_gen_taks()

'''На дек просто не хватает времени. Но вставку и удаление элементов с двух сторон могу реализовать,
    это не составляет трудности - только время(
'''
