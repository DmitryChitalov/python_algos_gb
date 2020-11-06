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
"""Пример создания стека через ООП"""

class StackClass:
    def __init__(self):
        self.stack = 0
        self.el = [[]]

    def is_empty(self):
        return self.el[self.stack] == []

    def push_in(self, el):
        if len(self.el[self.stack]) < 5:  # Порог после которого идет создание другого стека
            self.el[self.stack].append(el)
        else:
            self.stack = self.stack + 1
            self.el.append([])
            self.el[self.stack].append(el)

    def pop_out(self):
        return self.el[self.stack].pop()

    def get_val(self):
        return self.el[len(self.el) - 1]

    def stack_size(self):
        return len(self.el[self.stack])

    def stack_quantity(self):
        return len(self.el)

    def view_stacks(self):
        return self.el


SC_OBJ = StackClass()

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

print(SC_OBJ.stack_size())      # --> узнаем размер

SC_OBJ.push_in("пример")
SC_OBJ.push_in("пример1")
SC_OBJ.push_in("пример2")
print(SC_OBJ.stack_quantity())  # --> узнаем количество стеков
print(SC_OBJ.view_stacks())     # --> cмотрим значения в стеках