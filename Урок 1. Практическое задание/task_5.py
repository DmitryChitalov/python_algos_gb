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
"""


class PlatesStackClass:
    def __init__(self, max_size):
        self.elements = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elements)

    def is_empty(self):
        return self.elements == [[]]

    def push_in(self, el):
        if len(self.elements[len(self.elements) - 1]) < self.max_size:
            self.elements[len(self.elements) - 1].append(el)
        else:
            self.elements.append([])
            self.elements[len(self.elements) - 1].append(el)

    def pop_out(self):
        result = self.elements[len(self.elements) - 1].pop()
        if len(self.elements[len(self.elements) - 1]) == 0:
            self.elements.pop()
        return result

    def get_val(self):
        return self.elements[len(self.elements) - 1][len(self.elements[len(self.elements) - 1]) - 1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.elements:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.elements)


if __name__ == '__main__':
    plates = PlatesStackClass(3)
    for i in range(1, 11):
        plates.push_in(f'Plate{i}')
    print(plates)
    print(plates.pop_out())
    print(plates.get_val())
    print(plates.stack_size())
    print(plates.stack_count())
    print(plates)
