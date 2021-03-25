"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

# реализация через ООП, принцип расчётов тот же, что и в функциональной реализации,
# но переопределены методы сложения и умножения и не используется defaultdict


class HexNumber:

    alphabet = '0123456789ABCDEF'

    def __init__(self, number: str):
        self.number = list(number)

    def __str__(self):
        return str(self.number)

    def from_hex(self):
        """Переводит шестнадцатеричное число в виде списка в десятичное число"""
        num = dict()
        number = self.number[::-1]
        for idx in range(len(number)):
            if idx not in num:
                num[idx] = []
            num[idx].append(number[idx])
        result = [int(elem, 16) * 16 ** key
                  for key in num
                  for elem in num[key]]
        return sum(result)

    def to_hex(self, number, result=''):
        """Переводит десятичное число в объект класса"""
        if number == 0:
            return HexNumber(result)
        result = self.alphabet[number % 16] + result
        return self.to_hex(number // 16, result)

    def __add__(self, other):
        """Складывает два объекта класса и возвращает объект класса"""
        result = self.from_hex() + other.from_hex()
        return self.to_hex(result)

    def __mul__(self, other):
        """Перемножает два объекта класса и возвращает объект класса"""
        result = self.from_hex() * other.from_hex()
        return self.to_hex(result)


if __name__ == '__main__':

    number_1 = HexNumber(input('Введите первое число: '))
    number_2 = HexNumber(input('Введите второе число: '))
    print(f'Числа теперь выглядят так: {number_1} и {number_2}')
    print(f'Сумма чисел: {number_1 + number_2}')
    print(f'Произведение чисел: {number_1 * number_2}')
