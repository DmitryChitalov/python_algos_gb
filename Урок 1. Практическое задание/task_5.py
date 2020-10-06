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
import random


class StackClass:
    def __init__(self):
        self.elem_stack1 = []
        self.elem_stack2 = []
        self.elem_stack3 = []

    def is_empty(self):
        return self.elem_stack1 == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        if len(self.elem_stack1) < 10:
            self.elem_stack1.insert(0, el)
        elif len(self.elem_stack1) == 10 and len(self.elem_stack2) < 10:
            self.elem_stack2.insert(0, el)
        else:
            if len(self.elem_stack3) < 10:
                self.elem_stack3.insert(0, el)
            elif len(self.elem_stack3) == 10:
                print("Стек полностью заполнен!")
                return

    def pop_out(self):
        if len(self.elem_stack3):
            return self.elem_stack3.pop(0)
        elif len(self.elem_stack2):
            return self.elem_stack2.pop(0)
        else:
            return self.elem_stack1.pop(0)

    def get_val(self):
        if len(self.elem_stack3):
            return self.elem_stack3[0]
        elif len(self.elem_stack2):
            return self.elem_stack2[0]
        else:
            return self.elem_stack1[0]

    def stack_size(self):
        return f"В первом стеке {len(self.elem_stack1)} элементов, во втором стеке {len(self.elem_stack2)} элементов," \
               f" в третьем стеке {len(self.elem_stack3)} элементов"


Plate = StackClass()

print(Plate.is_empty())  # -> стек пустой

# наполняем стек
Plate.push_in(10)
Plate.push_in('code')
Plate.push_in(False)
Plate.push_in(5.5)

# получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
print(Plate.get_val())  # -> 5.5

# узнаем размер стека
print(Plate.stack_size())  # -> 4

print(Plate.is_empty())  # -> стек уже непустой

# кладем еще один элемент в стек
Plate.push_in(4.4)

# убираем элемент с вершины стека и возвращаем его значение
print(Plate.pop_out())  # -> 4.4

# снова убираем элемент с вершины стека и возвращаем его значение
print(Plate.pop_out())  # -> 5.5

# вновь узнаем размер стека
print(Plate.stack_size())  # -> 3

# заполним все стеки целиком, при попытке записать в переполненный стек будет сообщение
for i in range(30):
    Plate.push_in(random.randint(1, 1000))

# вновь узнаем размер стека
print(Plate.stack_size())  # cтеки полны
