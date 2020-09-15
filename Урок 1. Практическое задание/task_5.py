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


class TrayStack:
    def __init__(self):
        self.count = 0
        self.max_tray = 3

    def is_empty(self):
        return self.count == 0

    def push_in(self):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if self.count >= self.max_tray:
            self.count = self.max_tray
            print('Стопка полная, создайте новую!')
        else:
            self.count += 1

    def pop_out(self):
        self.count -= 1
        return self.count

    def is_crowded(self):
        return self.count >= self.max_tray

    def stack_size(self):
        return self.count


SC_OBJ = TrayStack()

print(SC_OBJ.is_empty())  # -> стек пустой

# наполняем стек
SC_OBJ.push_in()
SC_OBJ.push_in()
SC_OBJ.push_in()
SC_OBJ.push_in()


# узнаем размер стека
print(SC_OBJ.stack_size())

print(SC_OBJ.is_empty())  # -> стек уже непустой

# кладем еще один элемент в стек
SC_OBJ.push_in()

# убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())

# снова убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())

# вновь узнаем размер стека
print(SC_OBJ.stack_size())


