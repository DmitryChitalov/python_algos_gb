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


class StackOfPlates:

    def __init__(self, size_stack):
        self.elems = [[]]
        self.size_stack = size_stack

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, elem):
        if len(self.elems[len(self.elems) - 1]) < self.size_stack:
            self.elems[len(self.elems) - 1].append(elem)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(elem)

    def pop_out(self):
        deleted_item = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return deleted_item

    def get_val(self):
        return self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1]) - 1]

    def num_plates(self):
        sum_plates = 0
        for stack in self.elems:
            sum_plates += len(stack)
        return sum_plates

    def num_stacks(self):
        return len(self.elems)

    def __str__(self):
        for stack in self.elems:
            print(stack)
        print('\n')

    def __repr__(self):
        return repr(self.elems)


if __name__ == '__main__':
    test_stack = StackOfPlates(3)
    print(test_stack.is_empty())
    test_stack.__str__()
    test_stack.push_in(1)
    print(test_stack.is_empty())
    test_stack.__str__()
    test_stack.push_in(2)
    test_stack.__str__()
    test_stack.push_in('abc')
    test_stack.__str__()
    test_stack.push_in('wow')
    test_stack.__str__()
    test_stack.push_in(10)
    test_stack.__str__()
    test_stack.pop_out()
    test_stack.__str__()
    print(test_stack.__repr__())
    print(test_stack.num_stacks())
    print(test_stack.num_plates())
