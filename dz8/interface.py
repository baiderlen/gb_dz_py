from datetime import datetime

from vadim import create_job, delete_job, print_job, unlog_sys
# from  database import  get_data, change_data

def login(names):
    ok = False
    print("Добрый день! Необходимо залогиниться")
    print(f"{names}")
    print("Представьтесь, кто Вы?")
    while not ok:
        x = input("Введите число от 1 до 4: ")
        if x.isdigit() and 1 <= int(x) <= 4:
            ok = True
        else:
            print("Вы ошиблись!")
    return x


def inp_date(date):
    d = input("Введите дату: ")


def inp_period(perod):
    ok = False
    print("Выберите период времени")
    print(f"{period}")
    while not ok:
        x = input("Введите число от 1 до 3: ")
        if x.isdigit() and 1 <= int(x) <= 3:
            ok = True
        else:
            print("Вы ошиблись!")
    return x


def inp_menu(menu):
    ok = False
    print("Что Вы хотите сделать?")
    print(f"{menu}")
    while not ok:
        x = input("Введите число от 1 до 4: ")
        if x.isdigit() and 1 <= int(x) <= 4:
            ok = True
        else:
            print("Вы ошиблись!")
    return x


def inp_txt():
    return input("Опишите суть дела:")

# Добавил проверку корректности введенной даты.
def date_test():
    ok = False
    while not ok:
        date = input("Введите дату в формате 01.01.2000: ")
        date = date.replace(',', '.')
        if date.replace('.', '').isdigit() is False:
            print('Дата не может содержать буквы!')
        elif len(date) != 10:
            print('Вы ввели дату в неверном формате.')
        elif int(date[date.find('.') + 1:date.rfind('.')]) > 12:
            print('Количество месяцев не может быть больше 12!')
        elif int(date[date.find('.') - 2:date.find('.')]) > 31:
            print('Дней в году не может быть больше 31!')
        elif int(date[date.rfind('.') + 1:-2]) != 20:
            print('В таком возрасте у вас не должно быть дел)')
        else:
            ok = True
    return date


names = ("1. Константин 2. Лада 3. Вадим 4. Сергей")
menu = ("1. Создать дело 2. Удалить дело 3. Вывести все дела 4. Разлогиниться")
period = ("1. Утро 2. День 3. Вечер")

name_kode = int(login(names))
while True:
    menu_kode = int(inp_menu(menu))

    if menu_kode == 1:
        date = date_test()
        time_kode = int(inp_period(period))
        text_delo = inp_txt()
        Flag = create_job(name_kode, date, time_kode, text_delo)
        if Flag:
            print("Дело успешно создано")

    if menu_kode == 2:
        date = date_test()
        time_kode = int(inp_period(period))
        Flag1 = delete_job(name_kode, date, time_kode)
        if Flag1:
            print("Дело успешно удалено")

#Изменил, чтобы выводило весь список дел на все имеющиеся даты.
# Не всегда можно запомнить на какую дату есть дела, а на какую нет.
# Но не смог сделать красивый вывод, чтобы каждая новая дата начиналась с новой строки.
    if menu_kode == 3:
        # date = date_test()
        print(print_job(name_kode))

    if menu_kode == 4:
        unlog_sys(name_kode)
        break


