def creeaza_cheltuiala(numar_apartament, suma, zi, luna, an, intretinere, canal, alte_cheltuieli):
    """
    creeaza un dictionar ce reprezinta o cheltuiala
    :param numar_apartament: string
    :param suma: float
    :param zi: int
    :param luna: int
    :param an: int
    :param intretinere: float
    :param canal: float
    :param alte_cheltuieli: float
    :return: o lista 
    """
    cheltuiala = []
    cheltuiala.append(numar_apartament)
    cheltuiala.append(suma)
    cheltuiala.append(zi)
    cheltuiala.append(luna)
    cheltuiala.append(an)
    cheltuiala.append(intretinere)
    cheltuiala.append(canal)
    cheltuiala.append(alte_cheltuieli)
    return cheltuiala


def get_numar_apartament(cheltuiala):
    """
    da numarul de apartament asociat cu o cheltuiala
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return:numarul de apartament al cheltuielii
    """
    return cheltuiala[0]


def get_suma(cheltuiala):
    return cheltuiala[1]


def get_data_zi(cheltuiala):
    return cheltuiala[2]


def get_data_luna(cheltuiala):
    return cheltuiala[3]


def get_data_an(cheltuiala):
    return cheltuiala[4]


def get_intretinere(cheltuiala):
    return cheltuiala[5]


def get_canal(cheltuiala):
    return cheltuiala[6]


def get_alte_cheltuieli(cheltuiala):
    return cheltuiala[7]


def to_string(cheltuiala):
    """
    va printa sub forma de string datele
    :param cheltuiala: lista
    :return: datele sub forma de string
    """
    return "numar_apartament: {}, suma: {}. zi: {}, luna: {}, an: {}, intretinere: {}, canal: {}, alte_cheltuieli: {} ".format(
        get_numar_apartament(cheltuiala),
        get_suma(cheltuiala),
        get_data_zi(cheltuiala),
        get_data_luna(cheltuiala),
        get_data_an(cheltuiala),
        get_intretinere(cheltuiala),
        get_canal(cheltuiala),
        get_alte_cheltuieli(cheltuiala)
    )
