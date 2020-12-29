"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового
значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере
 с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class Stack:
    def __init__(self):
        self.elems = []

    def push(self, param):
        self.elems.append(param)

    def is_full(self):
        return len(self.elems) == 10

    def is_empty(self):
        return self.elems == []


def create_dish_stack(n):
    """Создает стопки тарелок по 10 штук на общее количество тарелок n.
    Записывает результат в список, возвращает итоговый список (стопки)"""
    result = []
    temp_stack = Stack()
    while n > 0:
        temp_stack.push('(')
        if temp_stack.is_full():
            result.append(temp_stack.elems)
            temp_stack = Stack()
        n -= 1
    if temp_stack.is_empty():
        return result
    else:
        result.append(temp_stack.elems)
        return result


print(create_dish_stack(25))
print(create_dish_stack(20))
print(create_dish_stack(1))
print(create_dish_stack(0))
print(create_dish_stack(3))
print(create_dish_stack(14))
print(create_dish_stack(16))
