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

# Для конкретности представим себе очередь в посудомоечную
# машину, с одной стороны поступают тарелки, а с другой
# забирают стопки, так что стопка ограничена вместимостью
# машины. Получается двусторонний стек, только с одного
# конца единицей является тарелка, а с другой -- стопка.
# Поскольку такая структура может пригодиться не только
# для тарелок, а, например, для бутылок и ящиков,
# обобщим понятия "тарелка" и "стопка" как
# "element" и "bundle"

from random import randrange

class NotEnoughElements(Exception):
    pass

class MultiStack:
    def __init__(self, bundle_size=10):
        self.elems = []
        self.bundle_size = bundle_size

    def is_empty(self):
        return self.elems == []
    
    def num_bundles(self):
        return len(self.elems) // self.bundle_size
    
    def num_elements(self):
        return len(self.elems)
    
    def push_element(self, el):
        self.elems.append(el)

    def pop_element(self):
        return self.elems.pop()
    
    def push_bundle(self, bundle):
        self.elems[0:0]=bundle

    def pop_bundle(self):
        if len(self.elems)<self.bundle_size:
            raise NotEnoughElements()
        ret = self.elems[0:self.bundle_size]
        self.elems[0:self.bundle_size] = []
        return ret

    def __repr__(self):
        lst = self.elems
        n = self.bundle_size
        return str(list(lst[i:i+n] for i in range(0, len(lst), n)))

ms = MultiStack(3)


for i in range(4):
    ms.push_element(chr(randrange(ord('A'), ord('Z'))))
print(ms)
print('Берем стопку ', ms.pop_bundle())
print(ms)
print('Добавляем стопку ', ['A','B','C'])
ms.push_bundle(['A','B','C'])
print(ms)
print(
    'Число полных стопок ', ms.num_bundles(),
    ', число тарелок ', ms.num_elements()
)




