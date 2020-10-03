"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

from memory_profiler import profile


class NotNumber(Exception):
    pass


class Exclusion:
    @staticmethod
    def enter_data():
        result = [el for el in range(101010)]
        while True:
            try:
                data = 0  # input('Вводите элементы через пробел (или нажмите ВВОД) - ')
                if not data:
                    return f'Введенные числа - {result}'

                result.extend(map(int, data.split()))

            except Exception:
                raise NotNumber(f'Надо вводить числа! \nУспели ввести - {result}')

    @profile
    def __str__(self):
        return self.enter_data()


if __name__ == '__main__':
    data_1 = Exclusion()
    try:
        print(data_1)
    except NotNumber as e:
        print(f'{e}')

'''
Line #    Mem usage    Increment   Line Contents
================================================
    33     12.6 MiB     12.6 MiB       @profile
    34                                 def __str__(self):
    35     14.0 MiB      1.3 MiB           return self.enter_data()
    
Не понял как доказать оптимизацию и эффективность, но замеры сделал, 
понял как работает и что бывают погрешности
'''
