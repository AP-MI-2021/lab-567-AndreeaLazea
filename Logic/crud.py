from domain.cheltuieli import creeaza_cheltuiala, get_id


def adauga_cheltuiala(id_1, numar_apartament, suma, data, tip, lista):
    """
    adauga o cheltuiala noua
    :param id_1: string
    :param numar_apartament: un string
    :param suma:  float
    :param data: string
    :param tip: string
    :param lista: adaugarea unei cheltuieli noi in lista
    :return: o lista noua
    """
    new_cheltuiala = creeaza_cheltuiala(id_1, numar_apartament, suma, data, tip)
    return lista + [new_cheltuiala]


def get_by_id(id_1, lst):
    """
    cauta cheltuiala asociata cu numarul de apartament cautat si o returneaza
    :param id_1: string
    :param lst: lista in care vom cauta
    :return: returneaza elementul din lista/cheltuiala in sine asociata cu nr de ap cautat
    """
    for cheltuiala in lst:
        if get_id(id_1) == id_1:
            return cheltuiala
    return None


def sterge_cheltuiala(id_1, lst):
    """
    sterge o cheltuiala din lista, asociata cu un nr de apartament
    :param id_1: string
    :param lst: lista in care cauta
    :return: noua lista fara apartamentul respectiv
    """
    new_list = []
    for cheltuiala in lst:
        if get_id(cheltuiala) != id_1:
            new_list.append(cheltuiala)
    return new_list


def modifica_cheltuiala(id_1, numar_apartament, suma, data, tip, lista):
    """
    modifica o cheltuiala dupa numar de apartament
    :param id_1: string
    :param numar_apartament: string
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: o lista noua
    :return: o lista noua modificata pentru un nr de apartament
    """
    if get_by_id(id_1, lista) is None:
        raise ValueError("Acest id nu exista!")
    new_list = []
    for cheltuiala in lista:
        if get_id(cheltuiala) == id_1:
            new_cheltuiala = creeaza_cheltuiala(id_1, numar_apartament, suma, data, tip)
            new_list.append(new_cheltuiala)
        else:
            new_list.append(cheltuiala)
    return new_list
