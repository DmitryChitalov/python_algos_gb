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


class Stacks_of_Plt:
    def __init__(self):
        self.elems = [[]]
        self.max_size = 5

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

    def show_stacks(self):
        k = 1
        for i in self.elems:
            el_string = ''.join(i)
            print(el_string, ' - ', len(i), ' тарелок, ', k, 'я стопка')
            k += 1


if __name__ == '__main__':

    SC_OBJ = Stacks_of_Plt()
    SC_OBJ.push_in('*')
    SC_OBJ.push_in('*')
    SC_OBJ.push_in('*')
    SC_OBJ.push_in('*')
    SC_OBJ.push_in('*')
    SC_OBJ.push_in('*')
    SC_OBJ.push_in('*')
    SC_OBJ.push_in('*')
    SC_OBJ.push_in('*')

    # показываем стопки
    SC_OBJ.show_stacks()
