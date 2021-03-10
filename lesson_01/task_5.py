"""
Задание 5.
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

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class PlatesStack:
    def __init__(self):
        self.cur_height = 0
        self.elements = []

    def __str__(self):
        return str(self.elements)

    def is_empty(self):
        return self.elements == []

    def push_in(self, el):
        self.elements.append(el)
        self.cur_height += 1

    def pop_out(self):
        if not self.is_empty():
            self.cur_height -= 1
            return self.elements.pop()

    def get_val(self):
        return self.elements[-1]

    def stack_size(self):
        return len(self.elements)


class StackOfStacks:
    def __init__(self, max_height):
        self.items = []
        self.max_height = max_height
        self.add_stack()

    def __str__(self):
        result = [f'{elem}\n' for elem in self.items]
        return ''.join(result)

    def add_stack(self):
        self.items.append(PlatesStack())

    def pop_stack(self):
        if not self.is_empty():
            return self.items.pop()

    def add_plate(self, el):
        if self.max_height == self.items[-1].cur_height or self.is_empty():
            self.add_stack()
        self.items[-1].push_in(el)

    def pop_plate(self):
        if not self.is_empty() and self.items[-1].is_empty():
            self.pop_stack()
        if not self.is_empty():
            return self.items[-1].pop_out()

    def is_empty(self):
        return self.items == []

    def stack_size(self):
        return len(self.items)


if __name__ == '__main__':

    # Добавляем 100 тарелок при высоте стопки 10 тарелок:
    stacks_plates_1 = StackOfStacks(10)
    for _ in range(100):
        stacks_plates_1.add_plate('Тарелочка')
    print(stacks_plates_1)

    # Забираем 11 тарелок:
    for _ in range(11):
        stacks_plates_1.pop_plate()
    print(stacks_plates_1)

    # Убираем последнюю стопку тарелок:
    stacks_plates_1.pop_stack()
    print(stacks_plates_1)

    # Добавляем блюдца:
    for _ in range(5):
        stacks_plates_1.add_plate('Блюдечко')
    print(stacks_plates_1)
