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
    def __init__(self, initsize):
        self.elems = [[]]
        self.initsize = initsize

    def is_empty(self):
        return self.elems == [[]]

    def return_all(self):
        return self.elems

    def push_in(self, el):
        if len(self.elems[self.get_val() - 1]) < self.initsize:
            self.elems[self.get_val() - 1].append(el)
        else:
            self.elems.append([])
            self.elems[self.get_val() - 1].append(el)

    def pop_out(self):
        self.elems[self.get_val() - 1].pop()
        if len(self.elems[self.get_val() - 1]) == 0 and self.get_val() > 1 :
            self.elems.pop()

    def get_val(self):
        return len(self.elems)

    def stack_size(self):
        counter_plate = 0
        for el in self.elems:
            counter_plate += len(el)
        return counter_plate

    def all_size(self):
        counter_plate = 0
        counter_stack = 0
        for el in self.elems:
            counter_stack += 1
            counter_plate += len(el)
        if counter_stack == 1 and counter_plate == 0:
            counter_stack = 0  # костыль
        return f'{counter_plate} тарелок, {counter_stack} кучек'


if __name__ == '__main__':
    washing_up = StackClass(3)
    # print(washing_up.is_empty())
    print(washing_up.all_size())  # здесь нужен был костыль
    washing_up.push_in("tarelka1")
    print(washing_up.all_size())
    washing_up.push_in("tarelka2")
    washing_up.push_in("tarelka3")
    washing_up.push_in("tarelka4")
    washing_up.push_in("tarelka5")
    washing_up.push_in("tarelka6")
    washing_up.push_in("tarelka7")
    washing_up.push_in("tarelka8")
    washing_up.push_in("tarelka9")
    washing_up.push_in("tarelka10")
    washing_up.push_in("tarelka11")
    washing_up.push_in("tarelka12")
    print(washing_up.all_size())
    washing_up.pop_out()
    print(washing_up.all_size())
    washing_up.pop_out()
    print(washing_up.all_size())
    washing_up.pop_out()
    print(washing_up.all_size())
    washing_up.pop_out()
    washing_up.pop_out()
    washing_up.pop_out()
    washing_up.pop_out()
    washing_up.pop_out()
    washing_up.pop_out()
    washing_up.pop_out()
    washing_up.pop_out()
    washing_up.pop_out()
    print(washing_up.all_size())
    print(washing_up.is_empty())
    # print(washing_up.return_all())
    washing_up.push_in("tarelka12")
    print(washing_up.all_size())
