from domain.cheltuieli import get_numar_apartament, get_data, get_suma, get_id, get_tip, creeaza_cheltuiala


def stergerea_tuturor_cheltuielilor(numar_apartament, lst):
    """
    sterge toate cheltuielile unui apartament
    :param numar_apartament: numarul de apartament pentru care este sters
    :param lst: lista initiala
    :return: o lista noua, fara cheltuielile listei precedente
    """
    new_lst = []
    for cheltuiala in lst:
        if get_numar_apartament(cheltuiala) != numar_apartament:
            new_lst.append(cheltuiala)
    return new_lst


def corectitudine_data(data_tastatura):
    list_of_string = list(data_tastatura)
    if len(list_of_string) < 10 or len(list_of_string) > 10:
        return False
    if list_of_string[2] != list_of_string[5] and list_of_string[5] != '.':
        return False
    count = 0
    for x in list_of_string:
        if x == '.':
            count = count + 1
    if count != 2:
        return False
    if list_of_string[0] == '0':
        day = int(list_of_string[1])
    else:
        new_string = list_of_string[0] + list_of_string[1]
        day = int(new_string)
    if list_of_string[3] == '0':
        month = int(list_of_string[4])
    else:
        new_string = list_of_string[3] + list_of_string[4]
        month = int(new_string)
    if month > 12:
        return False
    if month == 1 and day > 31:
        return False
    if month == 2 and day > 29:
        return False
    if month == 3 and day > 31:
        return False
    if month == 4 and day > 30:
        return False
    if month == 5 and day > 31:
        return False
    if month == 6 and day > 30:
        return False
    if month == 7 and day > 31:
        return False
    if month == 8 and day > 31:
        return False
    if month == 9 and day > 30:
        return False
    if month == 10 and day > 31:
        return False
    if month == 11 and day > 30:
        return False
    if month == 12 and day > 31:
        return False
    return True


def verificare_data(data_tastatura, lst, number):
    list_of_string = list(data_tastatura)
    if corectitudine_data(data_tastatura) is False:
        return []
    else:
        for x in list_of_string:
            if x[1:].isdigit() is True and x != '.':
                return []
    new_list = []
    for cheltuiala in lst:
        if get_data(cheltuiala) == data_tastatura:
            suma = get_suma(cheltuiala) + number
            id_1 = get_id(cheltuiala)
            numar_apartament = get_numar_apartament(cheltuiala)
            tip = get_tip(cheltuiala)
            data = get_data(cheltuiala)
            new_cheltuiala = creeaza_cheltuiala(id_1, numar_apartament, suma, data, tip)
            new_list.append(new_cheltuiala)
        else:
            new_list.append(cheltuiala)
    return new_list


def ordonare_descrescatoare(list_1):
    n = len(list_1)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if get_suma(list_1[j]) < get_suma(list_1[j + 1]):
                list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
                already_sorted = False
        if already_sorted:
            break
    return list_1
