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


class PlateStack:
    def __init__(self, max_stack_size):
        self.all_el = [[]]
        self.max_stack_size = max_stack_size

    def __str__(self):
        return str(self.all_el)

    def stack_in(self, new_el):
        if len(self.all_el[len(self.all_el) - 1]) < self.max_stack_size:
            self.all_el[len(self.all_el) - 1].append(new_el)
        else:
            self.all_el.append([])
            self.all_el[len(self.all_el) - 1].append(new_el)

    def stack_out(self):
        result = self.all_el[len(self.all_el) - 1].pop()
        if len(self.all_el[len(self.all_el) - 1]) == 0:
            self.all_el.pop()
        return result

    def stack_num(self):
        return len(self.all_el)

    def num_el(self):
        sum = 0
        for s in self.all_el:
            sum += len(s)
        return sum

if __name__ == '__main__':
    stack1 = PlateStack(5)
    stack1.stack_in('1')
    stack1.stack_in('2')
    stack1.stack_in('3')
    stack1.stack_in('4')
    stack1.stack_in('5')
    stack1.stack_in('6')
    stack1.stack_in('7')
    stack1.stack_in('8')
    stack1.stack_in('9')
    stack1.stack_in('10')
    stack1.stack_in('11')
    print(stack1)
    print(stack1.stack_num())
    print(stack1.stack_out())
    print(stack1.num_el())
