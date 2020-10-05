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
class MainDesc:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.append(item)

    def solved(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)

    def __iter__(self):
        self.elems = 0
        return self

    def __next__(self):
        try:
            x = self.elems
            self.elems += 1
            return x
        except IndexError:
            raise StopIteration()


class SolvedDesc(MainDesc):
    def __init__(self):
        self.elems = []

    def upgrade(self, num):
        return self.elems.pop(num)


if __name__ == '__main__':
    main_desk_obj = MainDesc()
    solv_desk_obj = SolvedDesc()
    task_list = ["Wake Up", "Drink Coffee", "Suffer", "Sleep", "Go again"]

    for task in task_list:
        main_desk_obj.to_queue(task)

    print(f'Начальный размер основной очереди {main_desk_obj.size()}')
    solv_desk_obj.to_queue(main_desk_obj.solved())
    solv_desk_obj.to_queue(main_desk_obj.solved())
    solv_desk_obj.to_queue(main_desk_obj.solved())
    print(f'Размер очереди решённых задач после решения 3 задач {solv_desk_obj.size()}')

    print(f'Текущий размер основной очереди {main_desk_obj.size()}')
    for it in range(main_desk_obj.size()):
        print(main_desk_obj.elems[it])
    print(f'Текущий размер очереди решённых {solv_desk_obj.size()}')
    for it in range(solv_desk_obj.size()):
        print(solv_desk_obj.elems[it])
    print('-'*10)
    main_desk_obj.to_queue(solv_desk_obj.upgrade(2))
    solv_desk_obj.to_queue(main_desk_obj.solved())
    print(f'Текущий размер основной очереди {main_desk_obj.size()}')
    for it in range(main_desk_obj.size()):
        print(main_desk_obj.elems[it])
    print(f'Текущий размер очереди решённых {solv_desk_obj.size()}')
    for it in range(solv_desk_obj.size()):
        print(solv_desk_obj.elems[it])
# суть - решённые задачи это наследуемый класс, на доработку - возврат в основной класс