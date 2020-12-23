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


class QueueClass:
    def __init__(self):
        self.elems = []

    def __str__(self):
        self.str_elems = self.elems.copy()
        self.str_elems.reverse()
        self.str_elems = '\n- '.join(self.str_elems)
        return self.str_elems

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


new_tasks = QueueClass()
ready_tasks = QueueClass()
unsolved_problems = QueueClass()

new_tasks.to_queue('Сдать отчет по опросу удовлетворенности клиентов')
new_tasks.to_queue('Подписать рекламационные акты')
new_tasks.to_queue('Посетить организацию-клиента')
new_tasks.to_queue('Собрать совещание по вопросам ведения договорной работы')
new_tasks.to_queue('Сдать отчет по контролю качества продукции')
new_tasks.to_queue('Направить письмо в отдел технического контроля')
print(f'Список задач:\n- {new_tasks}')
print('_____')

ready_tasks.to_queue(new_tasks.from_queue())
ready_tasks.to_queue(new_tasks.from_queue())
print(f'Список решенных задач:\n- {ready_tasks}')
print('_____')

print(f'Список задач:\n- {new_tasks}')
print('_____')

unsolved_problems.to_queue(new_tasks.from_queue())
print(f'Список задач на доработке:\n- {unsolved_problems}')
print('_____')

ready_tasks.to_queue(unsolved_problems.from_queue())
print(f'Список решенных задач:\n- {ready_tasks}')
print('_____')
print(f'Список задач на доработке:\n- {unsolved_problems}')
