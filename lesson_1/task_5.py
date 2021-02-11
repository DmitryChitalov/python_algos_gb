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


class SetOfStackClass:
    def __init__(self, size_limit=2):
        self.elems = [[]]
        self.size_limit = size_limit

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems[-1]) == self.size_limit:
            self.elems.append([el])
        else:
            self.elems[-1].append(el)
        return self.elems

    def pop_out(self):
        res = self.elems[-1].pop()
        if len(self.elems[-1]) == 0:
            self.elems.pop()
        return self.elems

    def get_val(self):
        return self.elems[len(self.elems) - 1][-1]
        # return self.elems[-1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':

    SC_OBJ = SetOfStackClass(4)

    print(f'Стек пустой? {SC_OBJ.is_empty()}')

    # наполняем стек
    for i in range(14):
        print(SC_OBJ.push_in(i))

    # убираем элементы с вершины стека
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.pop_out())

    # узнаем размер стека
    print(SC_OBJ.stack_size())

    print(f'Стек пустой? {SC_OBJ.is_empty()}')

    # вновь узнаем размер стека
    print(f'количество стопок {SC_OBJ.stack_size()}')

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())
