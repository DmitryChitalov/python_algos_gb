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

def bubble_sort(input_array):
    iter_count = 0
    for i in range(len(input_array)):
        array_sorted = True
        for j in range(len(input_array) - i - 1):
            iter_count += 1
            if input_array[j] < input_array[j + 1]:
                input_array[j], input_array[j + 1] = input_array[j + 1], input_array[j]
                array_sorted = False
            if array_sorted:
                print(f"Iterations count - {iter_count}")
                return
    print(f"Iterations count - {iter_count}")


arr = [1, 7, 6, 5, 4, 3, 2]

print(arr)
bubble_sort(arr)
print(arr)
bubble_sort(arr)
print(arr)