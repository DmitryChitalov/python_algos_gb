"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""


class BinarySearchNode:
    def __init__(self, a_value):
        self._left = None
        self._right = None
        self._value = a_value

    def __insert(self, bsn, a_value):
        if bsn is None:
            return BinarySearchNode(a_value)
        else:
            if bsn.get_value() == a_value:
                return bsn
            elif a_value > bsn.get_value():
                bsn._right = self.__insert(bsn._right, a_value)
            else:
                bsn._left = self.__insert(bsn._left, a_value)
        return bsn

    def __search(self, bsn, a_value):
        if bsn is None or bsn.get_value() == a_value:
            print("search complete!")
            return bsn

        if bsn.get_value() < a_value:
            print(f"go to deeper; current value {bsn.get_value()}")
            return self.__search(bsn.get_right(), a_value)

        return self.__search(bsn.get_left(), a_value)

    def add_value(self, a_value):
        self.__insert(self, a_value)

    def search(self, a_value):
        return self.__search(self, a_value)

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def get_value(self):
        return self._value


def find_and_print_node(bts, value):
    res = bts.search(value)

    if res is not None:
        if res.get_right() is not None:
            right_txt = f'right {res.get_right().get_value()}'
        else:
            right_txt = 'right node is not exists'
        left_txt = f'left {res.get_left().get_value()}' if res.get_left() is not None else 'left node is not exists'
        print(f'value {res.get_value()}; {left_txt}; {right_txt}; ')
    else:
        print(f"node with value {value} is not exists")

    print(f"{'#' * 80}")


def main():
    pass
    try:
        # пример дерева из wiki
        # https: // en.wikipedia.org / wiki / Binary_search_tree
        # https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/200px-Binary_search_tree.svg.png
        print("Binary search tree example from wiki")
        bts = BinarySearchNode(8)
        bts.add_value(3)
        bts.add_value(1)
        bts.add_value(6)
        bts.add_value(4)
        bts.add_value(7)
        bts.add_value(10)
        bts.add_value(14)
        bts.add_value(13)

        print("""
   __8__     
 /      \  
 3       10  
/ \       \  
1  6       14  
  / \      /    
  4 7    13    
        """)

        find_and_print_node(bts, 8)
        find_and_print_node(bts, 3)
        find_and_print_node(bts, 1)
        find_and_print_node(bts, 6)
        find_and_print_node(bts, 4)
        find_and_print_node(bts, 7)

        find_and_print_node(bts, 10)
        find_and_print_node(bts, 14)
        find_and_print_node(bts, 13)

        find_and_print_node(bts, 23)

        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()

"""
Имел опыт работы с бинарными деревьями(неупорядоченными) и ООП. Приведенный пример был слишком неудобен для доработки. 
Написал свой вариант. Пример дерева брал из википедии, чтобы упростить проверку.
Binary search tree example from wiki
По заданию - данная реализация не позволяет вставить элемент не туда, т.к. этим занимается алгоритм метода add_value.
   __8__     
 /      \  
 3       10  
/ \       \  
1  6       14  
  / \      /    
  4 7    13    
        
search complete!
value 8; left 3; right 10; 
################################################################################
search complete!
value 3; left 1; right 6; 
################################################################################
search complete!
value 1; left node is not exists; right node is not exists; 
################################################################################
go to deeper; current value 3
search complete!
value 6; left 4; right 7; 
################################################################################
go to deeper; current value 3
search complete!
value 4; left node is not exists; right node is not exists; 
################################################################################
go to deeper; current value 3
go to deeper; current value 6
search complete!
value 7; left node is not exists; right node is not exists; 
################################################################################
go to deeper; current value 8
search complete!
value 10; left node is not exists; right 14; 
################################################################################
go to deeper; current value 8
go to deeper; current value 10
search complete!
value 14; left 13; right node is not exists; 
################################################################################
go to deeper; current value 8
go to deeper; current value 10
search complete!
value 13; left node is not exists; right node is not exists; 
################################################################################
go to deeper; current value 8
go to deeper; current value 10
go to deeper; current value 14
search complete!
node with value does not exists
################################################################################

Программа завершена!

Process finished with exit code 0

"""
