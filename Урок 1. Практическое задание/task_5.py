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


class PlatesStackClass:
    stack_number = 0    # Номер стопки
    MAX_NUM_PLATES = 13 # Максимальное количество тарелок в стопке

    def __init__(self):
        PlatesStackClass.stack_number += 1
        print(f"Создаем стопку № {PlatesStackClass.stack_number}")
        self.num_plates = 0

    def is_empty(self):
        return self.num_plates == 0

    def push_in(self, el):
        print(f"Добавляем {el} тарелок")
        self.num_plates += el
        if self.num_plates > PlatesStackClass.MAX_NUM_PLATES:
            print(f"Заполняем стопку {PlatesStackClass.stack_number} до {PlatesStackClass.MAX_NUM_PLATES} тарелок")
            excess = self.num_plates - PlatesStackClass.MAX_NUM_PLATES
            self.num_plates = PlatesStackClass.MAX_NUM_PLATES
            stack_of_plates.append(PlatesStackClass())
            stack_of_plates[PlatesStackClass.stack_number - 1].push_in(excess)

    def pop_out(self, el):
        print(f"Забираем {el} тарелок")
        if el > PlatesStackClass.MAX_NUM_PLATES:
            print('Можно забирать не более ', PlatesStackClass.MAX_NUM_PLATES, ' тарелок')
            el = self.num_plates
            return
        if el > self.num_plates:
            print(f"В стопке {PlatesStackClass.stack_number} осталось только {self.num_plates} тарелок")
            shortage = el - self.num_plates
            print(f"Вынимаем {self.num_plates} тарелок из стопки {PlatesStackClass.stack_number}")
            self.num_plates = 0
            stack_of_plates[PlatesStackClass.stack_number - 1].__del__()
            stack_of_plates[PlatesStackClass.stack_number - 1].pop_out(shortage)
            return
        print(f"Вынимаем {el} тарелок из стопки {PlatesStackClass.stack_number}")
        self.num_plates -= el

    def get_full_stacks_qty(self):
        print(f"Количество полностью заполненых стопок : {PlatesStackClass.stack_number - 1}")

    def stack_size(self):
        print(f"Стопка № {PlatesStackClass.stack_number} содержит {self.num_plates} тарелок")

    def __del__(self):
        print(f"Удаляем стопку № {PlatesStackClass.stack_number}")
        PlatesStackClass.stack_number -= 1


stack_of_plates = [PlatesStackClass()]  # Инициализируем список стопок тарелок
print('\n')
print(stack_of_plates[PlatesStackClass.stack_number - 1].is_empty())  # проверяем новую стопку на "пустоту"
print('\n')
stack_of_plates[PlatesStackClass.stack_number - 1].push_in(1)  # пополняем стопку одной тарелками
print('\n')
stack_of_plates[PlatesStackClass.stack_number - 1].push_in(3)  # пополняем стопку тремя тарелками
print('\n')
stack_of_plates[PlatesStackClass.stack_number - 1].push_in(5)  # пополняем стопку пятью тарелками
print('\n')
stack_of_plates[PlatesStackClass.stack_number - 1].stack_size()  # проверяем количество тарелок в стопке
print('\n')
print(stack_of_plates[PlatesStackClass.stack_number - 1].is_empty())  # проверяем новую стопку на "пустоту"
print('\n')
stack_of_plates[PlatesStackClass.stack_number - 1].push_in(10)  # пополняем стопку десятью тарелками
print('\n')
stack_of_plates[PlatesStackClass.stack_number - 1].get_full_stacks_qty()  # узнаём количество заполненных стопок
print('\n')
stack_of_plates[PlatesStackClass.stack_number - 1].stack_size()  # проверяем количество тарелок в стопке
print('\n')
stack_of_plates[PlatesStackClass.stack_number - 1].pop_out(9)  # забираем 9 тарелок из стопки
print('\n')
stack_of_plates[PlatesStackClass.stack_number - 1].stack_size()  # проверяем количество тарелок в стопке
print('\n')

"""
Вопрос к преподавателю: Дмитрий, в функции pop_out при попытки вынуть из 'n'-й стопки количиство тарелок, большее чем
имеется я организовал выемку всех тарелок с последующей выемкой недостающего количества тарелок из предыдущей, 'n-1'-й
стопки. В промежутке этих действий, в строке 56 я вызываю закрытие экземпляра текущей, "опустошенной" стопки. Вроде всё
функционирует, но не уверен, правильно ли это; тем более в конце исполнения появляется вывод "Удаляем стопку № 0", 
которой как бы и не было... Как бы вы посоветовали правильно обыграть такую ситуацию?
"""