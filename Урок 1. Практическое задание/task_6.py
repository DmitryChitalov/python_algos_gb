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


class MyQueueClass:
    def __init__(self):
        self.q_tasks = []  # Очередь задач, отсюда будем их брать
        self.d_tasks = []  # Решенные задачи будем помещать сюда
        self.pd_tasks = []  # Частично решенные "на доработку"
        self.current = 0

    @property
    def q_empty(self):
        return not bool(self.q_size)

    @property
    def q_size(self):
        return len(self.q_tasks)

    @property
    def p_empty(self):
        return not bool(self.p_size)

    @property
    def p_size(self):
        return len(self.pd_tasks)

    def put(self):
        self.current += 1
        self.q_tasks.insert(0, f'Задача {self.current}')

    def done(self):
        if not self.q_empty:
            self.d_tasks.insert(0, self.q_tasks.pop())
        else:
            print('Задач в очереди нет!')

    def done_partial(self):
        if not self.p_empty:
            self.d_tasks.insert(0, self.pd_tasks.pop())
        else:
            print('Задач "на доработку" нет!')

    def to_partial(self):
        if not self.q_empty:
            self.pd_tasks.insert(0, self.q_tasks.pop())
        else:
            print('Задач в очереди нет!')

    def __str__(self):
        return f'Текущие задачи: {self.q_tasks}\n' \
               f'На доработку: {self.pd_tasks}\n' \
               f'Решенные задачи: {self.d_tasks}'


tasks_board = MyQueueClass()
while True:
    ans = input('(+) - добавить задачу, (v) - решить задачу, (-) - на доработку, (=) - дорешать, (q) - выход: ').lower()
    if ans == 'q':
        break
    if ans == '+':
        tasks_board.put()
    elif ans == 'v':
        tasks_board.done()
    elif ans == '=':
        tasks_board.done_partial()
    elif ans == '-':
        tasks_board.to_partial()
    print(tasks_board)
