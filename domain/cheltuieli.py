def creeaza_cheltuiala(id_1, numar_apartament, suma, data, tip):
    """
    creeaza o lista ce reprezinta o cheltuiala
    :param id_1: string
    :param numar_apartament: int
    :param suma: float
    :param data: string
    :param tip: string
    :return: o lista
    """
    cheltuiala = [id_1, numar_apartament, suma, data, tip]
    return cheltuiala


def get_id(cheltuiala):
    """
    da id-ul cheltuielii
    :param cheltuiala: o lista ce contine o cheltuiala
    :return: id-ul cheltuielii
    """
    return cheltuiala[0]


def get_numar_apartament(cheltuiala):
    """
    da numarul de apartament asociat cu o cheltuiala
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return:numarul de apartament al cheltuielii
    """
    return cheltuiala[1]


def get_suma(cheltuiala):
    return cheltuiala[2]


def get_data(cheltuiala):
    return cheltuiala[3]


def get_tip(cheltuiala):
    return cheltuiala[4]


def to_string(cheltuiala):
    """
    un text care prezinta toate datele dintr-o cheltuiala
    :param cheltuiala:
    :return: un text
    """
    return "id: {}, numar_apartament: {}, suma: {}. data: {}, tipul: {} ".format(
        get_id(cheltuiala),
        get_numar_apartament(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tip(cheltuiala)
    )
