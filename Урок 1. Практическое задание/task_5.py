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


class StackClass:
    max_size = 3

    def __init__(self):
        self.elems = [[]]

    def is_empty(self):
        return self.elems == [[]]

    def get_last_inner_index(self):
        return len(self.elems) - 1

    def is_empty_inner(self):
        return self.elems[self.get_last_inner_index()] == []

    def have_space_inner(self):
        return self.stack_size_inner() < self.max_size

    def push_in_inner(self, el):
        if self.have_space_inner():
            """Предполагаем, что верхний элемент стека находится в конце списка"""
            self.elems[self.get_last_inner_index()].append(el)
        else:
            self.elems.append([el])

    def pop_out_inner(self):
        el = self.elems[self.get_last_inner_index()].pop()
        if self.is_empty_inner():
            self.elems.pop()
        return el

    def get_val_inner(self):
        return self.elems[self.get_last_inner_index()][self.stack_size_inner() - 1]

    def stack_size_inner(self):
        return len(self.elems[self.get_last_inner_index()])


if __name__ == '__main__':
    SC_OBJ = StackClass()

    print('is empty =>>>', SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in_inner(10)
    SC_OBJ.push_in_inner('code')
    SC_OBJ.push_in_inner(False)
    SC_OBJ.push_in_inner(5.5)

    print('elems after push =>>>', SC_OBJ.elems)

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print('get value =>>>', SC_OBJ.get_val_inner())  # -> 5.5

    # узнаем размер стека
    print('check size =>>>', SC_OBJ.stack_size_inner())  # -> 1

    print('second stack is_empty =>>>', SC_OBJ.is_empty_inner())  # -> вторая стопка непустая

    # кладем еще один элемент в стек
    SC_OBJ.push_in_inner(4.4)

    # убираем элемент с вершины стека и возвращаем его значение
    print('second el from second stack =>>>', SC_OBJ.pop_out_inner())  # -> 4.4

    # снова убираем элемент с вершины стека и возвращаем его значение
    print('first el from second stack =>>>', SC_OBJ.pop_out_inner())  # -> 5.5

    # вновь узнаем размер стека
    print('size of first stack =>>>', SC_OBJ.stack_size_inner())  # -> 3

    print('first stack elements =>>>', SC_OBJ.elems[0])
