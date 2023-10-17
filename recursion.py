my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def lr(list_r):
    if len(list_r) <= 0:
        return print('Конец списка')
    else:
        print(list_r[0])
        lr(list_r[1::])


lr(my_list)