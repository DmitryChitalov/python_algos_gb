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
        self.plates = []
        self._archive = []

    def is_empty(self):
        return self.plates == []

    def is_epmty_archive(self):
        return self._archive == []

    def push_in(self, el):
        if len(self.plates) == 5:
            self.check_full_stack()
            self.plates.append(el)
        else:
            self.plates.append(el)

    def _show_archive(self):
        return self._archive

    def show_stack(self):
        return self.plates

    def pop_out(self):
        if len(self.plates) == 1:
            return self.check_empty_stack()
        else:
            return self.plates.pop()

    def get_val(self):
        return self.plates[len(self.plates) - 1]

    def stack_size(self):
        return len(self.plates)

    def check_full_stack(self):
        _var = self.plates.copy()
        self._archive.append(_var)
        return self.plates.clear()

    def check_empty_stack(self):
        self.plates.pop()
        _var = self._archive.pop()
        for el in _var:
            self.plates.append(el)


SC_OBJ = StackClass()

# Заполняем стек значениями
SC_OBJ.push_in('z')
SC_OBJ.push_in('x')
SC_OBJ.push_in('c')
SC_OBJ.push_in('v')
SC_OBJ.push_in(1)
SC_OBJ.push_in(2)
SC_OBJ.push_in(3)
SC_OBJ.push_in(4)
SC_OBJ.push_in(5)
SC_OBJ.push_in('a')
SC_OBJ.push_in('b')
SC_OBJ.push_in('c')
SC_OBJ.push_in('d')
SC_OBJ.push_in('e')
SC_OBJ.push_in('f')

# Смотрим размер текущего стека
print(f'размер: {SC_OBJ.stack_size()}')

# Смотрим текущий стек
print(SC_OBJ.show_stack())

# Смотрим стек, куда складируем предыдущие
print(SC_OBJ._show_archive())

# Убираем из стека определённое кол-во позиций
SC_OBJ.pop_out()
SC_OBJ.pop_out()
SC_OBJ.pop_out()
SC_OBJ.pop_out()
SC_OBJ.pop_out()
SC_OBJ.pop_out()

# Смотрим текущий стек
print(SC_OBJ.show_stack())

# Смотрим стек, куда складируем предыдущие
print(SC_OBJ._show_archive())
