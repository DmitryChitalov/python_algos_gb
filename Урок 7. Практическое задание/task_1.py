"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import random
import time
import turtle as tt

n = 20
some_list1 = [60, 33, 24, 59, 67, 7, 14, 81, 73, 64, 57, 52, 82, 8, 89, 62, 59, 17, 78, 86, 49, 4, 80, 55, 17, 86, 80, 96, 91, 80, 24, 8, 19, 64, 38, 83, 32, 53, 0, 61, 85, 68, 90, 38, 31, 17, 88, 32, 96, 93, 25, 43, 24, 54, 50, 46, 95, 62, 40, 96, 84, 91, 54, 1, 48, 4, 53, 10, 21, 15, 40, 70, 26, 32, 15, 8, 41, 94, 40, 63, 72, 12, 93, 11, 75, 0, 93, 21, 28, 81, 30, 1, 3, 55, 40, 66, 35, 100, 71, 8]
some_list = [random.randint(0,n) for i in range(n)]


def boble_sorte(list):
    list = list[:]
    max_item = len(list) - 1
    for i in range(max_item):
        yield list
        for i in range(max_item):
            if list[i] > list[i + 1]:
                list[i], list[i+1] = list[i+1], list[i]
    yield list


def some_sorte(list):
    list = list[:]
    n = 1
    for k in range(len(list)-n):
        yield list
        for i in range(len(list)-n):
            if list[i] > list[len(list)-n]:
                list[i], list[len(list)-n] = list[len(list)-n], list[i]
        n = n+1



def drawing():
    left = 0
    joe = tt.Turtle()
    joe.hideturtle()
    joe.penup()
    joe.setpos(-300, -200)
    joe.speed(0)
    joe.left(90)
    joe.pendown()
    for i in boble_sorte(some_list):
        joe.clear()
        for j in i:
            joe.forward(j)
            joe.left(180)
            joe.forward(j)
            joe.left(90)
            joe.forward(3)
            joe.left(90)
        joe.setpos(-300, -200)
        time.sleep(0.5)
    time.sleep(10)

drawing()

