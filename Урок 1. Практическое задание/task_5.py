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
import random


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

    def stack_clear(self):
        return self.elems.clear()

    def stack_call(self):
        return self.elems

    def extend(self, list_values):
        return self.elems.extend(list_values)


if __name__ == '__main__':
    def plate_stacks_ver_1(list_values):
        """
        Функция перезаписывает значения списка в значения словаря,
        с ограничением не больше 8 элементов на 1 ключ.

        :param list_values:
        :return:
        """
        pl_obj = StackClass()
        ind = 1
        dict_stacks = {}
        while len(list_values) > 0:
            for i in range(0, len(list_values)):
                pl_obj.push_in(list_values.pop(0))
                if pl_obj.stack_size() == 8 or len(list_values) == 0:
                    arch = pl_obj.stack_call()
                    dict_stacks[ind] = list(arch)
                    ind += 1
                    pl_obj.stack_clear()
        return dict_stacks


    def plate_stacks_ver_2(list_values):
        """
        Второй вариант функции: перезаписывает значения списка в значения словаря,
        с ограничением не больше 8 элементов на 1 ключ.

        :param list_values:
        :return:
        """

        pl_obj = StackClass()
        pl_obj.extend(list_values)
        list_task = []
        dict_stacks = {}
        index = 1
        while not pl_obj.is_empty():
            list_task.append(pl_obj.pop_out())
            dict_stacks[index] = list_task
            if len(list_task) == 8:
                list_task = []
                index += 1
        return dict_stacks


    list_sample = [random.randint(1, 10) for i in range(0, random.randint(16, 48))]
    print(f'Сформированный список: {list_sample}')
    print(f'Вариант 2: {plate_stacks_ver_2(list_sample)}')
    print(f'Вариант 1 : {plate_stacks_ver_1(list_sample)}')
