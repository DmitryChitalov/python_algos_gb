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


class StackClass:

    def __init__(self, max_stack=4):
        self.elems = [[]]
        self.max_stack = max_stack

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems[-1]) < self.max_stack:
            self.elems[-1].append(el)
        else:
            self.elems.append([el])

    def pop_out(self):
        if len(self.elems[-1]) == 1:
            last_elem = self.elems[-1].pop()
            del self.elems[-1]
            return last_elem
        return self.elems[-1].pop()

    def get_val(self):
        return self.elems[-1][-1]

    def stack_size(self):
        return len(self.elems)

    def print_stack(self):
        print(self.elems)


if __name__ == '__main__':
    SC_OBJ = StackClass()
    print(SC_OBJ.is_empty())
    SC_OBJ.push_in(1)
    SC_OBJ.push_in(2)
    SC_OBJ.push_in(3)
    SC_OBJ.push_in(4)
    SC_OBJ.push_in(5)
    SC_OBJ.push_in(6)
    SC_OBJ.push_in(7)
    print(SC_OBJ.get_val())
    SC_OBJ.print_stack()
    print(SC_OBJ.pop_out())
    SC_OBJ.print_stack()
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    SC_OBJ.print_stack()
    print(SC_OBJ.pop_out())
    SC_OBJ.print_stack()
    SC_OBJ.push_in('wer')
    SC_OBJ.push_in('qer')
    SC_OBJ.push_in('aer')
    SC_OBJ.push_in('ser')
    SC_OBJ.push_in('der')
    SC_OBJ.push_in('ter')
    SC_OBJ.print_stack()



