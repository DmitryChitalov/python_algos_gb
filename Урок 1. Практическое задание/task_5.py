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
    def __init__(self, max_size_stack):
        self.max_size_stack = max_size_stack
        self.all_stacks = [[]]

    def is_empty(self):
        return self.all_stacks == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.all_stacks[-1]) < self.max_size_stack:
            self.all_stacks[-1].append(el)
        else:
            self.all_stacks.append([el])

    def pop_out(self):
        if len(self.all_stacks[-1]) == 1:
            deleted_var = self.all_stacks.pop()
            if not self.all_stacks:
                self.all_stacks = [[]]
            return deleted_var
        else:
            return self.all_stacks[-1].pop()

    def get_val(self):
        return self.all_stacks[-1][-1]

    def stack_size(self):
        num_of_stacks = len(self.all_stacks)
        num_of_items = (len(self.all_stacks) - 1) * self.max_size_stack + len(self.all_stacks[-1])
        return num_of_stacks, num_of_items

    def __repr__(self):
        return self.all_stacks


if __name__ == '__main__':
    SC_OBJ = StackClass(3)

    print(SC_OBJ.is_empty())  # -> стек пустой True

    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)

    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> 5.5

    # узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 4

    print(SC_OBJ.is_empty())  # -> стек уже непустой False

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)

    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 5.5

    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 3

    print(SC_OBJ.all_stacks)
