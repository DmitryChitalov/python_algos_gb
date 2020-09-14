"""
Задание 6.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие нескольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""

class Tasks():
    def __init__(self):
        self.basic = []
        self.solved = []
        self.waiting = []

    def __str__(self):
        return 'Базовые:\t' + ' -> '.join(self.basic) + '\nНа доработку:\t' + ' -> '.join(self.waiting) + '\nРешенные:\t' + ' -> '.join(self.solved)

    def add_task(self, new_task):
        '''Добавляем новую задачу в список ожидания.'''
        self.basic.insert(0, (str(new_task)))

    def to_solved(self):
        '''Отправляем задачу в решенные.'''
        if self.basic:
            self.solved.insert(0, self.basic.pop())

    def to_waiting(self):
        '''Отправляет задачу на доработку.'''
        if self.basic:
            self.waiting.insert(0, self.basic.pop())

    def to_basic(self):
        '''Отправляет задачу в очередь на решение после доработки.'''
        if self.waiting:
            self.basic.insert(0, self.waiting.pop())


our_tasks = Tasks()
# Добавляем задачи в очередь на решение.
for one_taks in range(14):
    our_tasks.add_task(one_taks + 1)

print(our_tasks)
print()

# Отправляем задачи 1, 2, 3, 4, 7 и 8 в решенные; а 5, 6, 9 и 10 на доработку.
for to_queue in [our_tasks.to_solved, our_tasks.to_solved, our_tasks.to_waiting, our_tasks.to_solved, our_tasks.to_waiting]:
    for _ in range(2):
        to_queue()

print(our_tasks)
print()

# Отправляем пару задач (5 и 6) снова в очередь на решение.
for _ in range(2):
    our_tasks.to_basic()

print(our_tasks)
