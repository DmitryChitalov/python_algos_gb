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

def calc_rate(c_data):
    """
    Возвращает словарь в формате 'НаименованиеКомпании':'ГодоваяПрибыль'
    """
    cr = dict()
    for c in c_data:
        cr[c[0]] = sum(c[1:])
    
    print("Годовая прибыль компаний",cr)
    return cr

def sort_companies(c_raiting):
    """ 
    Сортирует названия компаний в два списка  1 - список прибыль выше среднего значения
    2 - список прибыль ниже среднего

    """
    up_avg = list()
    dw_avg = list()
    n = len(c_raiting.keys())

    avp = sum(c_raiting.values())/n # считаем среднюю прибыль всех компаний
    print("Средняя годовая прибыль всех предприятий", round(avp,1))

    for key  in c_raiting:
        if c_raiting[key] > avp:
            up_avg.append(key)
        else:
            dw_avg.append(key)


    return up_avg, dw_avg

def user_poll():
    """
    Ввод данных по компаниям
    """
    n_comp = int(input("Введите количество предприятий для расчета прибыли \n"))

    c_data = list() # массив для хранения данных по компаниям

    # цикл ввод информаци по компаниям
    Company = namedtuple('Company','name Q1 Q2 Q3 Q4') 

    for i in range(0, n_comp):
        c_name = input(f"Введите название {i+1} предприятия \n")
        c_return = input(f"Через пробел введите квартальные прибыли предприятия (4 квартала) \n")
        qr = [float(el) for el in c_return.split(' ')]
        c_data.append(Company(c_name, qr[0], qr[1], qr[2], qr[3]))

    c_raiting = calc_rate(c_data)

    up, dw = sort_companies(c_raiting)

    print(f"Предприятия с прибылью выше среднего {up}\n")
    print(f"Предприятия с приыбылью ниже среднего {dw}\n")

    return


if __name__ == '__main__':
    user_poll()