"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from random import randint


test_data = [randint(0, 10) for _ in range(15)]
print(test_data)

# в такой реализации возникают проблемы с неуникальными элементами
def med_check(data):
    for step in range(len(data)):
        more = less = 0
        for step2 in range(len(data)):
            if data[step] != data[step2]:
                if data[step] < data[step2]:
                    more += 1
                else:
                    less += 1
        if more == less:
            return f"Медианное значение: {data[step]}"
        # таким костыликом решил часть проблем с повторяющимися значениями
        # однако если повторы уходят в обе стороны - будет ошибка
        # возможно подошёл бы метод посчёта вхождений элемента и ...
        elif more + less + data.count(data[step]) >= len(data):
            # я забыл как побороть "ленивые" or и and, поэтому написал всё... прямолинейно
            # максимальный элемент не может быть медианой
            if more != 0:
                # как и минимальный
                if less != 0:
                    # если разница между кол-вом меньших и больших элементов не превышает число вхождений элемента
                    # то данный элемент является медианным
                    if abs(more - less) < data.count(data[step]):
                        return f"Медианное значение = {data[step]}"
        # elif more + data.count(data[step]) - 1 == less:
        #     return f"Медианное значение: {data[step]}"
        # elif less + data.count(data[step]) - 1 == more:
        #     return f"Медианное значение: {data[step]}"

        # использовалась для отлова значений
        # print(data[step], "-", less, more)

print(med_check(test_data))
test2 = sorted(test_data)
print(test2)
print("Check: ", test2[len(test2)//2])