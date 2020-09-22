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
class plates:
    def __init__(self, max_):
        self.el = [[]]
        self.max_ = max_

    def __str__(self):
        return str(self.el)

    def get_in(self, el):
        if len(self.el[len(self.el) - 1]) < self.max_:
            self.el[len(self.el) - 1].append(el)
        else:
            self.el.append([])
            self.el[len(self.el) - 1].append(el)

    def get_out(self, el):
        for idx in self.el:
            for name in idx:
                if name == el:
                    idx.remove(el)
                    return print('ok del')
        return print(f'Can find {el} in list')

    def size(self, type_size):
        el_sum = 0
        if type_size:
            for pack in self.el:
                el_sum += len(pack)
            return print(f'Size of stack is {el_sum}')
        else:
            return print(f'Size of list is {len(self.el)}')


if __name__ == '__main__':
    plat = plates(2)
    plat.get_in('plate_1')
    plat.get_in('plate_2')
    plat.get_in('plate_3')
    print(f'{plat}')
    plat.get_out('plate_7')
    print(f'{plat}')
    plat.size(1)
    plat.get_in('plate_4')
    print(f'{plat}')