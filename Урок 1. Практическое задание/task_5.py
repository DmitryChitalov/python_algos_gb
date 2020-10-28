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


class PlateStackClass:
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size  # размер стопки

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        # предполагаем, что верхний элемент стека находится в конце списка
        # если размер стопки равен пороговому значению, то создается новая стопка и туда кладется значение
        if len(self.elems[len(self.elems) - 1]) < self.max_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        # берем тарелку из крайней стопки, если она пустая удаляем ее
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1][self.elems[len(self.elems) - 1] - 1]

    def stack_size(self):
        # общее количество тарелок
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        # количество стоек
        return len(self.elems)


if __name__ == 'main':
    plates = PlateStackClass(3)
    plates.push_in('Plate1')
    plates.push_in('Plate2')
    plates.push_in('Plate3')
    plates.push_in('Plate4')
    print(plates.get_val())  # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(plates.is_empty())  # не пустой
    print(plates.stack_size())  # узнаем размер стека
    print(plates.pop_out())  # убираем элемент с вершины стека и возвращаем его значение
