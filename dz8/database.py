DIC_LOGIN = \
    {
        1: ('Konstantin', 'Seminary\\konstatin.txt'),
        2: ('Lada', 'Seminary\\lada.txt'),
        3: ('Vadim', 'Seminary\\vadim.txt'),
        4: ('Sergey', 'Seminary\\sergey.txt')
    }

# Если не было передано никакой информации для записи и мы хотим разлогиниться, то вылезает ошибка,
# я так понимаю потому что функция ждет что ей что-то передадут. Тоже не разобрался как решить.
# И если файл не создан, то тоже ошибка, при смене mode на 'a' - ошибка.
def get_data(login):
    readed_data = []
    with open(DIC_LOGIN[login][1], mode='r', encoding='utf-8') as data:
        for line in data:
            readed_data.append(line.replace('\n', ''))
    data = list(map(lambda d: d.split('|'), readed_data))
    down_data = {}
    for i in data:
        down_data[i[0]] = i[1:]

    return down_data




def change_data(login, dict_data):
    uploaded_list = [f'{key}|{"|".join(dict_data[key])}' for key in dict_data]
    uploaded_str = '\n'.join(uploaded_list)
    with open(DIC_LOGIN[login][1], mode='w', encoding='utf-8') as data:
        data.write(uploaded_str)
    return True

# print(change_data(1, 1))