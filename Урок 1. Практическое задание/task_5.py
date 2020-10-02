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

# никак не получилось сделать автоматический переход на новый стек и заполнение его, что только не пробовал, но никак.
# Максимумчто вышло - когда стопка тарелок переполняется, то все остальные клады по одной на каждую стопку.
# Сидел весь вечер, голова не соображает уже))
# Может я как-то неверно понял задание.

class PlatesClass:
    def __init__(self):
        self.plates = []

    def stack_size(self):
        return len(self.plates)

    def show_stack_plates(self):
        self.plates.reverse()
        for plate in self.plates:
            print(plate)

    def is_empty(self):
        return self.plates == []

    def how_much_plates_before_limit(self):
        limit = 5
        return (limit - self.stack_size())

    def new_stack_creation(self):
        newinstance = PlatesClass()
        return newinstance

    def new_stack_add(self, plate):
        self.plates.append(plate)


    def put_plates_on_top(self, plate):
        limit = 5
        if len(self.plates) < limit:
            self.plates.append(plate)
        elif len(self.plates) == limit:
            newinstance = self.new_stack_creation()
            newinstance.new_stack_add(plate)
            #newinstance.show_stack_plates()
        #elif len(self.plates) > limit and idx%limit != 0:
            #newinstance.new_stack_add(plate)
            #newinstance.show_stack_plates()


    def remove_plates_from_top(self):
        return self.plates.pop()

stack_1 = PlatesClass()
stack_1.put_plates_on_top('first')
stack_1.put_plates_on_top('second')
stack_1.put_plates_on_top('third')
stack_1.put_plates_on_top('four')
stack_1.put_plates_on_top('five')
stack_1.put_plates_on_top('six')
stack_1.put_plates_on_top('seven')
stack_1.put_plates_on_top('eight')
stack_1.put_plates_on_top('nine')


print('--------')
stack_1.show_stack_plates()
print('--------')

#stack_1.remove_plates_from_top()
#stack_1.remove_plates_from_top()
#stack_1.show_stack_plates()




