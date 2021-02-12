"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов


    Одна из новых возможностей, появившихся в Python 3.7 — классы данных (Data classes).
Они призваны автоматизировать генерацию кода классов, которые используются для хранения данных.
Не смотря на то, что они используют другие механизмы работы,
их можно сравнить с "изменяемыми именованными кортежами со значениями по умолчанию.

    Основано на идее:
использовать структуру хранения в памяти, как у экземпляров классов со __slots__,
но не участвовать при этом в механизме циклической сборки мусора.

https://docs.python.org/3/library/dataclasses.html
https://www.python.org/dev/peps/pep-0557/
https://habr.com/ru/post/415829/
https://habr.com/ru/post/455722/

"""
from dataclasses import dataclass
from sys import getsizeof
from pympler import asizeof
import recordclass


class RegularBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


# Аналогичный код с декоратором dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

# Важно отметить, что аннотации типов обязательны. Все поля, которые не имеют отметок о типе будут проигнорированы.

#В результате мы получаем классс реализованными методами __init__, __repr__, __str__ и __eq__.
# Кроме того, это будет обычный класс и вы можете наследоваться от него или добавлять произвольные методы.


regular_book = RegularBook(title="Dandelion Wine", author="Bradbury", pages=345)
regular_book2 = RegularBook(title="Конституция Каир", author="Каирский народ", pages=1345)

book = Book(title="Fahrenheit 451", author="Bradbury", pages=256)
book2 = Book(title="Конституция РФ", author="Народ", pages=100)

print(asizeof.asizeof(book))
print(asizeof.asizeof(book2))
print(asizeof.asizeof(regular_book))
print(asizeof.asizeof(regular_book2))

print(getsizeof(Book))
print(getsizeof(RegularBook))
print(getsizeof(book))
print(getsizeof(regular_book))

# 280
# 320 !!!
# 280
# 344 !!!
# 536
# 536
# 24
# 24

# На единичных экземплярах разница в занимаемой памяти не видна, однако, как утверждает документация,
# при увеличении количества экземпляров разница в потребляемой памяти существенна
