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
    def __init__(self):
        self.elems = []
        self.elems2 = []
        self.max_size = 5

    def is_empty(self):
        return self.elems == [], self.elems2 == []

    def push_in(self, el):
        self.elems.append(el) if self.stack1_size() < self.max_size else self.elems2.append(el)

    def pop_out(self):
        return self.elems2.pop() if len(self.elems2) != 0 else self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1] if self.elems2 is True else self.elems2[len(self.elems2) - 1]

    def stack1_size(self):
        return len(self.elems)

    def stack2_size(self):
        return len(self.elems2)

if __name__ == '__main__':
    SC_OBJ = StackClass()

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    SC_OBJ.push_in(101)
    SC_OBJ.push_in(11)
    SC_OBJ.push_in(112)


    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> 112

    # узнаем размер 1го стека
    print(SC_OBJ.stack1_size())  # -> 5

    # узнаем размер 2го стека
    print(SC_OBJ.stack2_size())  # -> 2

    print(SC_OBJ.is_empty())  # -> стек уже непустой false

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> 4.4


    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4

    # проверяем 
    print(SC_OBJ.get_val())

