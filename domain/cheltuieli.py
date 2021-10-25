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
    :return:
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
    return cheltuiala["numar_ap"]


def get_suma(cheltuiala):
    return cheltuiala["suma"]


def get_data_zi(cheltuiala):
    return cheltuiala["data_zi"]


def get_data_luna(cheltuiala):
    return cheltuiala["data_luna"]


def get_data_an(cheltuiala):
    return cheltuiala["data_an"]


def get_intretinere(cheltuiala):
    return cheltuiala["intretinere"]


def get_canal(cheltuiala):
    return cheltuiala["canal"]


def get_alte_cheltuieli(cheltuiala):
    return cheltuiala["alte_cheltuieli"]


def to_string(cheltuiala):
    """

    :param cheltuiala:
    :return:
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
