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

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()


    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)


class Plates:
    __height = 3  # сколько тарелок в стопке максимум

    def __init__(self):
        self.elems = []
        self.elems.append(StackClass())

    def is_empty(self):
        return self.elems == []

    def stack_size(self):
        return self.__height * (len(self.elems) - 1) + self.elems[len(self.elems) - 1].stack_size()

    def get_val(self):
        return self.elems[len(self.elems) - 1].get_val()

    def push_in(self, el):
        if self.elems[len(self.elems) - 1].stack_size() == self.__height: # если последняя стопка заполнена
            self.elems.append(StackClass())   # создаем новую стопку
        self.elems[len(self.elems) - 1].push_in(el)

    def pop_out(self):
        if self.elems[len(self.elems) - 1].is_empty(): # если последняя стопка пустая
            self.elems.pop() # удаляем
        return self.elems[len(self.elems) - 1].pop_out()



SC_OBJ = Plates()

print(SC_OBJ.is_empty())  # -> стек пустой

# наполняем стек
SC_OBJ.push_in(10)
SC_OBJ.push_in('code')
SC_OBJ.push_in(False)
SC_OBJ.push_in(5.5)

# получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
print(SC_OBJ.get_val())  # -> 5.5

# узнаем размер стека
print(SC_OBJ.stack_size())  # -> 4

print(SC_OBJ.is_empty())  # -> стек уже непустой

# кладем еще один элемент в стек
SC_OBJ.push_in(4.4)

# убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())  # -> 4.4

# снова убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())  # -> 5.5

# вновь узнаем размер стека
print(SC_OBJ.stack_size())  # -> 3

# снова убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())  # ->

# снова убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())  # ->

print(SC_OBJ.pop_out())  # ->


