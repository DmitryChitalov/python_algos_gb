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


class Plates:
    def __init__(self):
        self.plates = []

    def __str__(self):
        return str(self.plates)

    def __len__(self):
        return len(self.plates)

    def push_in(self, el):
        self.plates.append(el)

    def push_out(self):
        return self.plates.pop()

    def get_val(self):
        return self.plates[len(self.plates) - 1]


class StackClass:
    def __init__(self, max_size):
        self.elems = []
        self.max_size = max_size

    def is_empty(self):
        return self.elems == []

    def __str__(self):
        my_str = ''
        for el in self.elems:
            my_str += str(el)
        return my_str

    def push_in(self, el):
        if len(self.elems) == 0 or len(self.elems[len(self.elems) - 1]) >= self.max_size:
            self.elems.append(Plates())
            self.elems[len(self.elems) - 1].push_in(el)
        else:
            self.elems[len(self.elems) - 1].push_in(el)

    def pop_out(self):
        if len(self.elems[len(self.elems) - 1]) > 0:
            buf = self.elems[len(self.elems) - 1].push_out()
            if len(self.elems[len(self.elems) - 1]) == 0:
                self.elems.pop()
            return buf

    def get_val(self):
        return self.elems[len(self.elems) - 1].get_val()

    def stack_size(self):
        return len(self.elems)


SC_OBJ = StackClass(2)

print(SC_OBJ.is_empty())


SC_OBJ.push_in('Plate1')
SC_OBJ.push_in('Plate2')
SC_OBJ.push_in('Plate3')
print(SC_OBJ)
SC_OBJ.pop_out()
print(SC_OBJ)
SC_OBJ.push_in('Plate4')
SC_OBJ.push_in('Plate5')
SC_OBJ.push_in('Plate6')
SC_OBJ.push_in('Plate7')
print(SC_OBJ)
print(SC_OBJ.get_val())
SC_OBJ.pop_out()
print(SC_OBJ)
SC_OBJ.pop_out()
SC_OBJ.pop_out()
print(SC_OBJ)
SC_OBJ.push_in('Plate8')
SC_OBJ.push_in('Plate9')
SC_OBJ.push_in('Plate10')
SC_OBJ.push_in('Plate11')
print(SC_OBJ)
SC_OBJ.pop_out()
SC_OBJ.push_in('Plate12')
print(SC_OBJ)

print(SC_OBJ.get_val())

