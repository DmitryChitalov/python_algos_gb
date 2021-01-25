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

    def get_str(self):
        res = '<'
        for rec in self.elems:
            res += rec + ', '
        res += '>'
        return res

class PileArr:
    max_in_pile  = 3
    cur_pile_ind = 0
    elem_count   = 0

    def __init__(self):
        self.piles = []
        self.piles.append(StackClass())

    def is_empty(self):
        return self.elem_count == 0

    def push_in(self, el):
        if self.piles[PileArr.cur_pile_ind].stack_size() < PileArr.max_in_pile:
            self.piles[PileArr.cur_pile_ind].push_in(el)
        else:
            self.piles.append(StackClass())
            PileArr.cur_pile_ind += 1
            self.piles[PileArr.cur_pile_ind].push_in(el)

        PileArr.elem_count += 1

    def pop_out(self):
        if(self.piles[PileArr.cur_pile_ind].stack_size() == 0) and (PileArr.cur_pile_ind == 0):
            return None

        if(self.piles[PileArr.cur_pile_ind].stack_size() == 0):
            del self.piles[PileArr.cur_pile_ind]
            PileArr.cur_pile_ind -= 1;

        PileArr.elem_count -= 1

        return self.piles[PileArr.cur_pile_ind].pop_out()

    def get_val(self):
        return self.piles[PileArr.cur_pile_ind].get_val()

    def stack_size(self):
        return PileArr.elem_count

    def __repr__(self):
        res = f'Всего элементов: <{PileArr.elem_count}>: '
        cur_pile = 0
        for rec in self.piles:
            cur_pile += 1
            res += f'стопка <{cur_pile}>: '+rec.get_str()+', '
        return res

    def pile_count(self):
        return PileArr.cur_pile_ind+1

##########
# Шаг 1: создание стека стопок и наполнени его 5 тарелками.
# При этом создается две стопки:
# в первой три элемента, во торой два.
SC_OBJ = PileArr()
SC_OBJ.push_in('P1')
SC_OBJ.push_in('P2')
SC_OBJ.push_in('P3')
SC_OBJ.push_in('P4')
SC_OBJ.push_in('P5')
print(SC_OBJ)
print('pile_count():', SC_OBJ.pile_count())
##########
# Шаг 2: удаление трех тарелок.
# При этом остается одна стопка.
print('pop_out():', SC_OBJ.pop_out())
print('pop_out():', SC_OBJ.pop_out())
print('pop_out():', SC_OBJ.pop_out())
print(SC_OBJ)
print('pile_count():', SC_OBJ.pile_count())
##########
