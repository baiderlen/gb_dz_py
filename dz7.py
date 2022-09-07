a = None
print('Телефонный справочник.')


def menu():
    n = None
    while n != 1 and n != 2:
        n = int(input('Введите 1, если желаете добавить запись в справочник. 2, если хотите посмотреть справочник: '))
        if n == 1:
            add_new()
        elif n == 2:
            check()
        else:
            print('Ошибка! Введите 1 или 2!')


def add_new():
    def vvod_name():
        name = False
        while not name:
            x = input('Введите имя: ')
            if x.isdigit() is True:
                print('Имя не может состоять из цифр')
            elif x[0] == ' ':
                print('Имя не может быть пустым')
            elif [x for i in x if i.isdigit()]:
                print('Имя не может содержать цифры')
            elif len(x) <= 1:
                print('Имя не может состоять из одной буквы.')
            else:
                name = True
        return x

    def vvod_last_name():
        last_name = False
        while not last_name:
            x = input('Введите фамиию: ')
            if x.isdigit() is True:
                print('Фамилия не может состоять из цифр')
            elif x[0] == ' ':
                print('Фамилия не может быть пустой')
            elif [x for i in x if i.isdigit()]:
                print('Фамилия не может содержать цифры')
            elif len(x) <= 1:
                print('Фамилия не может состоять из одной буквы.')
            else:
                last_name = True
        return x

    def vvod_tel():
        tel = False
        while not tel:
            x = input('Введите номер телефона в формате 79999999999: ')
            if x.isdigit() is False:
                print('Номер должен содержать только цифры без пробелов')
            elif len(x) != 11:
                print('Номер телефона должен содержать 11 цифр: ')
            else:
                tel = True
        return x

    def vvod_comment():
        x = input('Введите комментарий: ')
        return x

    a = {'name': vvod_name(), 'last_name': vvod_last_name(), 'tel': vvod_tel(), 'comment': vvod_comment()}
    n = None
    while n != 1 and n != 2:
        n = int(input('Для записи данных в строку нажмите 1, для записи в столбец 2: '))
        if n == 1:
            load_line(a)
        elif n == 2:
            load_column(a)
        else:
            print('Неверный ввод, введите 1 или 2')

    return True


def load_column(a):
    with open('out.txt', 'a', encoding='utf8') as out:
        for key, val in a.items():
            out.write('{}:{}\n'.format(key, val))
        out.write('\n')
    return print('Данные успешно добавлены')


def load_line(a):
    with open('out.txt', 'a', encoding='utf8') as out:
        for key, val in a.items():
            out.write('{}:{} '.format(key, val))
        out.write('\n')
        out.write('\n')
    return print('Данные успешно добавлены')


def check():
    with open('out.txt') as inp:
        # for key in inp.readlines():
        a = inp.readlines()
        for i in a:
            print(i.strip())
    return True


menu()

