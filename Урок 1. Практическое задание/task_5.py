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
для реализации этой структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class PlateClass:
    def __init__(self, limit_size):
        self.elems = [[]]
        self.limit_size = limit_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка.
        Если размер пачки с тарелками равен limit_size, создается новая пачка, куда кладется новая тарелка"""
        if len(self.elems[len(self.elems) - 1]) < self.limit_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1]) -1]

    def stack_size(self):
        """здесь вытягиваем значение, сколько всего тарелок"""
        elem_overall = 0
        for stack in self.elems:
            elem_overall += len(stack)
        return elem_overall

    def stack_qty(self):
        """здесь вытягиваем количество стеков"""
        return len(self.elems)


if __name__ == '__main__':
    plates = PlateClass(6)
    plates.push_in('First plate')
    plates.push_in('Second plate')
    plates.push_in('Third plate')
    plates.push_in('Fourth plate')
    plates.push_in('Fifth plate')
    plates.push_in('Sixth plate')
    plates.push_in('Seventh plate')
    print(plates)
    print(plates.pop_out())
    print(plates.get_val())
    print(plates.stack_size())
    print(plates.stack_qty())
    print(plates)