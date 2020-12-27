"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class Stack:
    def __init__(self, max_len):
        self.items = []
        self.max_len = max_len

    def isempty_all(self):
        return self.items == []

    def isempty(self):
        return self.items[-1] == []

    def push(self, elem):
        if self.isempty_all():
            self.items.append([elem])
        elif self.isempty():
            self.items.append([elem])
        elif len(self.items[-1]) == self.max_len:
            self.items.append([elem])
        else:
            self.items[-1].append(elem)

    def pop(self):
        cur = self.items[-1].pop()
        if self.isempty():
            self.items.pop[-1]
        return cur

    def len(self):
        return len(self.items[-1])

    def len_all(self):
        return len(self.items)

    def ontop(self):
        return self.items[-1][-1]

    def show(self):
        print('\n'.join(', '.join(map(str, st)) for st in self.items))


rings = Stack(4)
rings.push('R1')
rings.push('R2')
rings.push('R3')
rings.push('R4')
rings.push('R5')
rings.push('R6')
print(f'Длина общая = {rings.len_all()}; Длина крайнего = {rings.len()}')
print(f'На вершине - {rings.ontop()}')
rings.show()
print(f'Выброшенный - {rings.pop()}')
print(f'На вершине - {rings.ontop()}')
print(f'Длина общая = {rings.len_all()}; Длина крайнего = {rings.len()}')
rings.show()
