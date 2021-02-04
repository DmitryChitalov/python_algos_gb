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


class PlateClass:
    def __init__(self, size):
        self.elems = [[]]
        self.size = size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        # self.elems.append(el)
        if len(self.elems[len(self.elems) - 1]) < self.size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        # return self.elems.pop()
        if len(self.elems[len(self.elems) - 1]) > 1:
            return self.elems[len(self.elems) - 1].pop()
        else:
            val = self.elems[len(self.elems) - 1].pop()
            self.elems.pop()
            return val

    def get_val(self):
        # return self.elems[len(self.elems) - 1]
        return self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1]) - 1]

    def stack_size(self):
        # return len(self.elems)
        total_len = 0
        for i in range(len(self.elems)):
            total_len += len(self.elems[i])
        return total_len

    def last_stack_count(self):
        return len(self.elems[len(self.elems) - 1])

    def stacks_count(self):
        return len(self.elems)


if __name__ == '__main__':
    plates = PlateClass(5)

    print(plates.is_empty())  # -> стек пустой

    # наполняем стек
    for i in range(1, 15):
        plates.push_in(f'тарелка {i}')

    # узнаем число стопок
    print(plates.stacks_count())

    # узнаем число элементов в последней стопке
    print(plates.last_stack_count())

    # узнаем общее число тарелок
    print(plates.stack_size())

    # берем верхнюю тарелку из последней стопки, смотрим на нее и убираем
    print(plates.pop_out())

    # узнаем число элементов в последней стопке
    print(plates.last_stack_count())

    # смотрим на верхнюю тарелку в последней стопке, не трогая ее
    print(plates.get_val())

    # узнаем число элементов в последней стопке
    print(plates.last_stack_count())
