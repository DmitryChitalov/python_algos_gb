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


class OwnError(Exception):
    """Собственное исключение."""
    def __init__(self, txt):
        self.txt = txt


class PlateClass:
    """
    Реализация класса "тарелка".
    При инициализации нового объкта получает уникальный номер.
    """
    __warehouse = []

    def __init__(self):
        """
        Инициализация нового объекта и помещение в склад для дальнейшей
        индентификации уникального номера.

        Последовательность номеров начинается с 1.
        """
        PlateClass.__warehouse.append(self)
        self.unique_number = PlateClass.__warehouse.index(self) + 1

    def __repr__(self):
        """Определяет вид объекта."""
        return f'Plate'
        # Возможен другой вариант реализации:
        # return f'Plate{self.unique_number}'
        # Но выглядит он не совсем коректно.

    def get_unique_number(self):
        """Вернуть уникальный номер тарелки."""
        return self.unique_number

    @staticmethod
    def get_plate(number):
        """Получить номер тарелки по номеру."""
        if not isinstance(number, int) or number <= 0 or number > len(PlateClass.__warehouse):
            raise OwnError('Тарелка c таким номером не существует!')
        return PlateClass.__warehouse[number-1]


class PlatesStack:
    """Реализция структуры "стопка тарелок" по принципу стека."""

    def __init__(self, stack_max):
        """Вид хранения стопок - вложенные списки."""
        self.__stacks_number = 0
        self.plates_number = 0
        self.stacks = []
        self.stack_max = stack_max

    def is_empty(self):
        """Проверить, является ли объект пустым."""
        return self.stacks == []

    def look_at_stacks(self):
        """Вид объекта."""
        return self.stacks

    def push_in(self, number=None):
        """Добавить тарелку в стопку.
        При заполнение стопки максимальным значением, будет создана новаястопка.
        """
        if number:
            try:
                plate = PlateClass.get_plate(number)
            except OwnError:
                raise OwnError('Тарелка c таким номером не существует!')
            for i in range(len(self.stacks)):
                if plate in self.stacks[i]:
                    raise OwnError('Нельзя добавить тарелку в стопку повторно!')
        else:
            plate = PlateClass()
        if self.is_empty():
            self.stacks.append([])
        if len(self.stacks[self.__stacks_number]) == self.stack_max:
            self.__stacks_number += 1
            self.stacks.append([])
        self.stacks[self.__stacks_number].append(plate)
        self.plates_number += 1

    def pop_out(self):
        """Удалить тарелку из стопки."""
        # Если стопок нет - будет возвращено исключение.
        if self.is_empty():
            raise OwnError('Тарелок нет!')
        else:
            plate = self.stacks[self.__stacks_number].pop()
            self.plates_number -= 1
            if len(self.stacks[self.__stacks_number]) == 0:
                self.__stacks_number -= 1
                self.stacks.remove([])
            return plate

    def get_stacks_number(self):
        """Вернуть количество стопок."""
        return self.__stacks_number + 1 if self.plates_number != 0 else 0

    def get_plates_number(self):
        """Вернуть количество тарелок."""
        return self.plates_number


if __name__ == '__main__':
    # Создаем класс стопок с максимальным значением.
    a = PlatesStack(10)

    print('Проверяем количество стопок:')
    print(a.get_stacks_number())

    print('\nПри попытке убрать тарелку из пустой стопки будет возвращено исключение:')
    try:
        a.pop_out()
    except OwnError as err:
        print(err)

    # Составляем стопки из 11 тарелок
    for _ in range(11):
        a.push_in()

    print('\nВид стопок после добавления тарелок:')
    print(a.look_at_stacks())
    print('\nКоличество стопок:')
    print(a.get_stacks_number())

    print('\nУбираем тарелку из стопки и проверяем ее номер:')
    print(a.pop_out().get_unique_number())
    print('\nВид стопок после удаления пустой стопки:')
    print(a.look_at_stacks())

    print('\nПроверка уникального номера первой тарелки в первой стопке:')
    print(a.look_at_stacks()[0][0].get_unique_number())

    print('\nПробуем добавить тарелку с несуществующим номером:')
    try:
        a.push_in(12)
    except OwnError as err:
        print(err)

    # Добавляем ранее удаленную из стопки тарелку номер 11
    a.push_in(11)

    print('\nПробуем добавить тарелку номер 11 еще раз:')
    try:
        a.push_in(11)
    except OwnError as err:
        print(err)
