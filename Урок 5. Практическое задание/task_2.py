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
first = str(input("Введите первое число в Шестнадцатеричной системе счисления= "))
second = str(input("Введите второе число в Шестнадцатеричной системе счисления= "))

list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

if len(first) > len(second):
  first, second = second, first

second = second[::-1]
third = []

j = -1
k = 0
for i in second:
  one = list_of_numbers.index(i)
  two = list_of_numbers.index(first[j])
  third.append(list_of_numbers[(one + two + k) % 16])
  if (one + two) >= 15:
    k = 1
  else:
    k = 0
  j -= 1
  if j == -len(first)-1:
    break

diff = len(second) - len(first)

if diff:
    for i in second[-diff:]:
        third.append(list_of_numbers[(list_of_numbers.index(second[-diff]) + k) % 16])
        if list_of_numbers.index(second[-diff]) + 1 >= 15:
            k = 1
        else:
            k = 0
if k == 1:
  third.append('1')

print(third[::-1])

"""
def calc():
    nums = collections.defaultdict(list)
    
    #  defaultdict(<class 'list'>,
    #  {'1-A2': ['A', '2'], '2-C4F': ['C', '4', 'F']})
    for d in range(2):
        n = input(f"Введите {d+1}-e натуральное шестнадцатеричное число: ")
        nums[f"{d+1}-{n}"] = list(n)
    print(nums)
    
    #  16-указываем с числами какой системы делаем операции
    sum_res = sum([int(''.join(i), 16) for i in nums.values()])
    print(sum_res)
    #  '%X' Число в шестнадцатиричной системе счисления
    
    print("Сумма: ", list('%X' % sum_res))
    #  f'{15:x}' -> f
    mul_res = functools.reduce(lambda a, b: a * b,
                               [int(''.join(i), 16) for i in nums.values()])
    print("Произведение: ", list('%X' % mul_res))
    
"""