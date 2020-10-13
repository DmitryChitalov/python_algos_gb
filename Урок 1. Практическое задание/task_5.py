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
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elems);

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, elem):
        if len(self.elems[len(self.elems)-1]) < len(self.elems):
            self.elems[len(self.elems)-1].append(elem)
        else:
            self.elems[len(self.elems) - 1].append([''])
            self.elems[len(self.elems) - 1].append(elem)

    def pop_out(self):
        res = self.elems[len(self.elems)-1].pop()
        if len(self.elems[len(self.elems)-1]) ==0:
            self.elems.pop()
        return res;

    def get_value(self):
        return self.elems[len(self.elems)-1]

    def stack_size(self):
        elem_sum=0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.elems)

if __name__ == '__main__':
    plates = PlateStack(3)
    plates.push_in('pl1')
    plates.push_in('pl2')
    plates.push_in('pl3')
    plates.push_in('pl4')
    plates.push_in('pl5')

    print(plates);
    print(plates.pop_out());
    print(plates.get_value());
    print(plates.stack_size());
    print(plates.stack_count());

