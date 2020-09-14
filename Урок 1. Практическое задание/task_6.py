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
########################################################################################################3
"""
Реализованно 3 очереди: 1 - базовая, 2 - решенные, 3 - требующие корректировки
Для примера решаеться задача сложенния 2х чисел, если вместо int или float приходит str задача отправляеться 
на корректировку
"""


class TaskBoard:
    def __init__(self):
        self.tasks = []
        self.made_tasks = []
        self.correction_tasks = []

    def is_empty(self):
        return self.tasks == []

    def to_queue_tasks(self, item: list):
        """
        функция добавляеть задачу в базовую очередь
        """
        self.tasks.insert(0, item)

    def from_queue_tasks(self):
        """
        функция забирает задачу из базовой очереди
        """
        return self.tasks.pop()

    def to_queue_correction_tasks(self, elem):
        """
        функция добавляеть задачу в очередь на коректировку
        """
        self.correction_tasks.insert(0, elem)

    def from_queue_correction_tasks(self):
        """
        функция забирает задачу из очереди на коректировку
        """
        return self.correction_tasks.pop()

    def to_queue_made_tasks(self, num):
        """
         функция добавляеть задачу в очередь решенных задач
        """
        self.made_tasks.insert(0, num)

    def from_made_tasks(self):
        """
        функция забирает задачу из очереди решенных задач
        """
        return self.made_tasks.pop()

    def sum_number(self):
        """
        функция решает задачу сложенния двух чисел
        и сортирует решения по очередям
        """
        try:
            tmp = self.from_queue_tasks()
            self.to_queue_made_tasks(sum(tmp))
        except Exception as e:
            self.to_queue_correction_tasks(tmp)

    def print_all_queue(self):
        """
        для визуального контроля очередей, стандартный вывод перезагружать не стал
        """
        print(self.tasks)
        print(self.made_tasks)
        print(self.correction_tasks)
        print('_____________________________')


if __name__ == '__main__':
    list_task = [[1, 2],
                 [10, 100],
                 [11, 22],
                 ["11", 10],
                 [14, 100],
                 [223, '25'],
                 [1.2, 2.5],
                 [2, 5]
                 ]

    TestObj = TaskBoard()
    # запалняем базовую очередь
    for el in list_task:
        TestObj.to_queue_tasks(el)

    TestObj.print_all_queue()
    # решаем задачи
    for el in range(len(list_task) - 1):
        TestObj.sum_number()

    TestObj.print_all_queue()
    # забираем решения
    print(TestObj.from_made_tasks())
    # забираем задачи на корректировку
    print(TestObj.from_queue_correction_tasks())
