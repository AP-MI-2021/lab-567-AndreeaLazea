from domain.cheltuieli import get_numar_apartament, get_data, get_suma, get_id, get_tip, creeaza_cheltuiala
import re


def stergerea_tuturor_cheltuielilor(numar_apartament, lst):
    """
    sterge toate cheltuielile unui apartament
    :param numar_apartament: numarul de apartament pentru care este sters
    :param lst: lista initiala
    :return: o lista noua, fara cheltuielile listei precedente
    """
    new_lst = []
    for cheltuialaa in lst:
        if get_numar_apartament(cheltuialaa) != numar_apartament:
            new_lst.append(cheltuialaa)
    return new_lst


def corectitudine_data(data_tastatura):
    """
    vedrifica corectitudinea datii
    :param data_tastatura: o data de la tastatura
    :return: True, daca data este scrisa corect si False in caz contrar
    """
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


def check_if_str_is_special_character(list_1):
    """
    verifica daca in lista exista alte caractere, inafara de numere
    :param list_1: o lista
    :return: True daca e format doar din cifre si False in caz contrar
    """
    for x in list_1:
        string_check = re.compile('[@_!#$%^&*()<>?/|}{~:,`abcdefghijklmnopqrstuvwxy]')
        if string_check.search(x) is not None:
            return False
    return True


def verificare_data(data_tastatura, lst, number):
    """
    Verifica
    :param data_tastatura:
    :param lst:
    :param number:
    :return:
    """
    list_of_string = list(data_tastatura)
    if check_if_str_is_special_character(list_of_string) is False:
        return []
    if corectitudine_data(data_tastatura) is False:
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
    """
    realizeaza ordonarea descrescatoare a unei liste
    :param list_1: o lista
    :return: lista ordonata desc
    """
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


def cea_mai_mare_cheltuiala(list_1):
    suma_canal = 0
    suma_intretinere = 0
    suma_alte_cheltuieli = 0
    for cheltuiala in list_1:
        if get_tip(cheltuiala) == "canal":
            suma_canal = suma_canal + get_suma(cheltuiala)
        elif get_tip(cheltuiala) == "intretinere":
            suma_intretinere = suma_intretinere + get_suma(cheltuiala)
        elif get_tip(cheltuiala) == "alte cheltuieli":
            suma_alte_cheltuieli = suma_alte_cheltuieli + get_suma(cheltuiala)
    if suma_canal == 0 and suma_intretinere == 0 and suma_alte_cheltuieli == 0:
        raise ValueError('lista este goala deja')
    else:
        if suma_canal > suma_intretinere and suma_canal > suma_alte_cheltuieli:
            maxim = suma_canal
        elif suma_intretinere > suma_canal and suma_intretinere > suma_alte_cheltuieli:
            maxim = suma_intretinere
        else:
            maxim = suma_alte_cheltuieli
        new_list = []  # in cazul in care sunt mai multe cu aceeasi suma, le va adauga in lista pe care o va returna!
        if suma_canal == maxim:
            new_list = new_list + ["canal"]
        if suma_intretinere == maxim:
            new_list = new_list + [" intretinere"]
        if suma_alte_cheltuieli == maxim:
            new_list = new_list + [" alte cheltuieli"]
        return new_list


def suma_lunara_ap(list_1):
    """

    :param list_1:
    :return:
    """
    dictionary = {}
    for cheltuiala in list_1:
        numar_apartament = get_numar_apartament(cheltuiala)
        suma = get_suma(cheltuiala)
        data = get_data(cheltuiala)
        list_of_string = list(data)
        if list_of_string[3] == '0':
            month = int(list_of_string[4])
        else:
            new_string = list_of_string[3] + list_of_string[4]
            month = int(new_string)
        year = list_of_string[6] + list_of_string[7] + list_of_string[8] + list_of_string[9]
        year_1 = int(year)
        if numar_apartament in dictionary:
            if year in dictionary[numar_apartament]:
                if month in dictionary[numar_apartament][year]:
                    dictionary[numar_apartament][year][month] = dictionary[numar_apartament][year][month] + suma
                else:
                    dictionary[numar_apartament][year][month] = suma
            else:
                dictionary[numar_apartament][year] = {month : suma}
        else:
            dictionary[numar_apartament] = {year: {month: suma}}
    return dictionary
