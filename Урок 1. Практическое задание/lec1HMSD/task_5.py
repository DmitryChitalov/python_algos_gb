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
class St_Plates:
    def __init__(self, colvo):
        self.elems = [[]]
        self.max_size = colvo

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems)-1]) < self.max_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        if len(self.elems[len(self.elems) - 1]) != 0:
            self.elems = self.elems[len(self.elems) - 1].pop()
        else:
            self.elems = self.elems.pop()

    def view_cupboard(self):
        k = 1
        for i in self.elems:
            print(f'В {k}ой стопке лежит {len(i)} тарелки(а): {i}')
            k += 1

cupboard = St_Plates(4)
cupboard.push_in('1')
cupboard.push_in('2')
cupboard.push_in('3')
cupboard.push_in('4')
cupboard.push_in('5')
cupboard.push_in('6')
cupboard.push_in('7')
cupboard.push_in('8')
cupboard.push_in('9')
cupboard.push_in('A')
cupboard.push_in('B')

cupboard.view_cupboard()