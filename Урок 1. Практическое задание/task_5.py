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
class PlateStack:
    def __init__(self,maxstacksize):
        self.elems = [[]]
        self.maxstacksize = maxstacksize

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, elem):
        if (len(self.elems[len(self.elems)-1])) <= self.maxstacksize:
            self.elems[len(self.elems)-1].append(elem)
        else:
            self.elems.append([elem])

    def pop_out(self):
        tempplate =self.elems[len(self.elems)-1].pop()
        if(len(self.elems[len(self.elems)-1]) == 0):
            self.elems.pop()
        return tempplate


    def size(self):
        return len(self.elems[len(self.elems)-1]) + (len(self.elems)-1) * self.maxstacksize

    def __str__(self):
        return str(self.elems)

platesSatack = PlateStack(2)
platesSatack.push_in('1')
platesSatack.push_in('1')
print(platesSatack.size())
platesSatack.push_in('1')
platesSatack.push_in('1')
platesSatack.push_in('1')
platesSatack.push_in('1')
platesSatack.push_in('1')
platesSatack.push_in('1')
platesSatack.push_in('1')
platesSatack.pop_out()
platesSatack.pop_out()
print(platesSatack)