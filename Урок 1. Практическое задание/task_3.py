"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
import random as rnd
import string


class Company:
    def __init__(self, name, profit):
        self.name = name
        self.profit = profit


class Companies:
    def __init__(self):
        self.data = []

    def add_company(self, cmp):
        k = 0
        for item in self.data:  # O(n)
            if cmp.profit < item.profit:
                k += 1
            else:
                break
        self.data.insert(k, cmp)  # O(n)

    def topk(self, k):
        print(f'top {k} companies:')
        for j in self.data[:k]:  # O(1), несмотря на цикл-на входе константа k,сложность не зависит от кол-ва элементов
            print(f'company: {j.name}')


class CompaniesTwo:
    def __init__(self):
        self.data = []

    def add_company(self, cmp):
        self.data.append(cmp)  # O(1)

    def topk(self, k):
        print(f'top {k} companies:')
        data_max = self.data[:]
        for _ in range(k):
            c = self.__popmax(data_max)
            print(c.name, c.profit)

    """ Возвращает максимальное значение и удаляет из списка
    """
    def __popmax(self, c):
        max_index = 0
        max_value = Company('', 0)
        for index, item in enumerate(c):  # O(n)
            if item.profit > max_value.profit:
                max_value = item
                max_index = index
        c.pop(max_index)  # O(n)
        return max_value


if __name__ == '__main__':
    """ Решение первое.
    Сортируем компании по прибыли при добавлении в каталог. Сложность поиска - константная О(1).
    Сложность добавления n элементов - O(n^2) : O(2*n) при добавлении одного и O(1/2*n) все добавления
    Может использоваться в случаях, когда добавление происходит реже, чем обращение к элементам по рейтингу.

    """
    c1 = Company('C1', 10)
    C = Companies()
    C.add_company(c1)
    C.add_company(Company('C2', 100))
    C.add_company(Company('C3', 1))
    C.add_company(Company('C4', 5))
    C.topk(3)

    """ Решение второе.
    Для выдачи топ компаний, создаем копию списка, и обходим список k раз для поиска максимальных прибылей, удаляя 
    найденные максимумы. Сложность - O(n * k), где n - количество компаний, k - количество искомых из топа
    может быть лучше первого решения если компании добавляются часто и не требуется частый доступ к топу компаний.
    """
    C2 = CompaniesTwo()
    for _ in range(10):
        C2.add_company(Company([''.join(rnd.choice(string.ascii_lowercase) for _ in range(6))], rnd.randint(10, 100)))
    for i in C2.data:
        print(i.name, i.profit)
    C2.topk(3)
