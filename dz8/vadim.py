from database import get_data, change_data, DIC_LOGIN

a = None


def print_job(x):
    global a

    if a is None:
        a = get_data(x)
    # a.setdefault(date, ['', '', ''])

    # return True
    return a



def create_job(x, date, time, txt):
    global a
    if a is None:
        a = get_data(x)
    a.setdefault(date, ['', '', ''])
    a[date][time-1] = txt

    return True

# Не понимаю почему удаление работает 1 раз.
# Если обратиться к дате, которой нет, то 1 раз он выдает то что дел на дату нет, но если в этом же цикле
# обратиться еще раз, то вылезает ошибка.
def delete_job(x, date, time):
    global a
    if a is None:
        a = get_data(x)
        a.setdefault(date, print('Дел на эту дату нет'))
    else:
        a[date][time - 1] = ''
    return True


def unlog_sys(x):
    global a
    if a is None:
        a = get_data(x)
    change_data(x, a)
    a = None
    return True