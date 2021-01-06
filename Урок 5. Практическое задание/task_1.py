"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple


# from collections import Counter


def create_data(quantity):
    Firm = namedtuple('tuple_for_firm', 'firm_name, v_1st v_2nd v_3rd v_4th')
    for quant in range(quantity):
        firm_name = input(f'Введите название компании {quant + 1}: ')
        try:
            new_data = list(map(int, input(f'Введите через пробел квартальные прибыли фирмы {firm_name}: ').split()))
            globals()[f"firm_{quant + 1}"] = Firm(firm_name=firm_name, v_1st=new_data[0], v_2nd=new_data[1],
                                                  v_3rd=new_data[2],
                                                  v_4th=new_data[3])
            # попытка генерить имя по счетчику цикла; через exec не завелось почему-то.
            # Глобалки мне тут не нравятся, потом переделаю...
        except ValueError:
            print('вводите числа цифрами!')
            break
        except UnboundLocalError:
            print('something wrong')
        except IndexError:
            print('минимум 4 квартала!')
            break


def get_avg(quantity):
    create_data(quantity)
    res_dict = {}
    main_summ = 0
    for quant in range(quantity):
        firm_avg = sum(globals()[f"firm_{quant + 1}"][1:5]) / 4
        res_dict.update([(globals()[f"firm_{quant + 1}"][0], firm_avg)])
        main_summ += firm_avg
    try:
        main_avg = main_summ / quantity
    except ZeroDivisionError:
        return 'Нечего считать'

    return f'Средняя годовая прибыль всех предприятий: {main_avg}\n' \
           f'Предприятия, с прибылью выше среднего: {", ".join([key for key in res_dict if res_dict[key] > main_avg])}\n' \
           f'Предприятия, с прибылью меньше среднего:{", ".join([key for key in res_dict if res_dict[key] < main_avg])}'

'''
второй вариант использования namedtuple, навернео зря
def create_data2(quantity):
    Firm = namedtuple('tuple_for_firm', 'firm_name, v_1st v_2nd v_3rd v_4th')
    for quant in range(quantity):
        firm_name = input(f'Введите название компании {quant + 1}: ')
        Firm = namedtuple(firm_name, 'v_1st v_2nd v_3rd v_4th')
        new_data = list(map(int, input(f'Введите через пробел квартальные прибыли фирмы {firm_name}: ').split()))
        new_obj = Firm(v_1st=new_data[0], v_2nd=new_data[1], v_3rd=new_data[2], v_4th=new_data[3])
        return new_obj.v_2nd
'''

if __name__ == '__main__':
    try:
        quantity = int(input(f'Введите количество компаний цифрами: '))

    except ValueError:
        print("Серьезно?")
        exit(1)
    # print(get_avg(quantity))  # вариант 1, если ввести 0 пойдет в вариант 2
    # quantity = int(input(f'Введите количество компаний цифрами: '))
    # print(create_data2(quantity))

