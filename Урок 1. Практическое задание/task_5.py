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


class FewStackClass:
    def __init__(self, stack_limit):
        self.elems = [[]]
        self.stack_limit = stack_limit  # придельный размер стека

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.stack_limit:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1]) - 1]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':
    plates = FewStackClass(2)

    # проверка, пустой ли стек
    print(plates.is_empty())  # -> True стек пустой

    # наполняем стек
    plates.push_in('Plate1')
    plates.push_in('Plate2')
    plates.push_in('Plate3')
    plates.push_in('Plate4')
    print(plates)  # -> [['Plate1', 'Plate2'], ['Plate3', 'Plate4']]

    # получаем значение первого элемента с вершины последнего стека, но не удаляем сам элемент из стека
    print(plates.get_val())  # -> 'Plate4'

    # узнаем размер стека (коилчество подстеков)
    print(plates.stack_size())  # -> 2

    # проверка, пустой ли стек
    print(plates.is_empty())  # -> false = стек уже непустой

    plates.push_in('Plate5')  # кладем еще один элемент в стек
    print(plates)  # -> [['Plate1', 'Plate2'], ['Plate3', 'Plate4'], ['Plate5']]
    print(plates.stack_size())  # -> 3

    # убираем элемент с вершины стека и возвращаем его значение
    print(plates.pop_out())  # -> 'Plate5'
    print(plates)  # -> [['Plate1', 'Plate2'], ['Plate3', 'Plate4']]

    # вновь узнаем размер стека
    print(plates.stack_size())  # -> 2
