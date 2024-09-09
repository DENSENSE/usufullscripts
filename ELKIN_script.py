from datetime import *
from math import ceil



def ElkÍn():
    # Функция ELKÍN выводит True, если неделя - четная
    # А выводит False, если нечет


    first_month = 9 # точка отсчета в месяцов
    first_day = 2 # точка отсчета во днях
    days_in_month = [30, 31, 30, 31, 30, 28, 30, 31, 30, 31] # Нормальная система месяцев, чтоб все работало (отсчет с сентября)

    array_today= str(date.today()).split('-') # YEAR MONTH DAY

    curr_month, curr_day = int(array_today[1]), int(array_today[2]) 



    if curr_month < 9: # если месяц принадлежит промежутку от января до июня
        curr_month += 12 
    arr_curr_mont = curr_month - 9


    all_days = 0 
    while arr_curr_mont > 0: # суммируем все дни, которые были о этого момента(в месяцах)
        arr_curr_mont -= 1
        all_days += days_in_month[arr_curr_mont]
    all_days += curr_day # Добавляем день из даты
    all_days -= first_day
    all_days += 1


    if (ceil(all_days / 7) % 2 == 0): return True#
    return False

print(ElkÍn())


