from domain.cheltuieli import creeaza_cheltuiala, get_numar_apartament


def adauga_cheltuiala(numar_apartament, suma, zi, luna, an, intretinere, canal, alte_cheltuieli, lista):
    """
    adauga o cheltuiala noua
    :param numar_apartament: un string
    :param suma:  float
    :param zi: int
    :param luna: int
    :param an: int
    :param intretinere: float
    :param canal: float
    :param alte_cheltuieli: float
    :param lista: adaugarea unei cheltuieli noi in lista
    :return:
    """
    new_cheltuiala = creeaza_cheltuiala(numar_apartament, suma, zi, luna, an, intretinere, canal, alte_cheltuieli)
    return lista + [new_cheltuiala]


def get_by_number(numar_apartament, lst):
    """
    cauta cheltuiala asociata cu numarul de apartament cautat si o returneaza
    :param numar_apartament: string
    :param lst: lista in care vom cauta
    :return: returneaza elementul din lista/cheltuiala in sine asociata cu nr de ap cautat
    """
    for cheltuiala in lst:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            return cheltuiala
    return None


def sterge_cheltuiala(numar_apartament, lst):
    """
    sterge o cheltuiala din lista, asociata cu un nr de apartament
    :param numar_apartament: string
    :param lst: lista in care cauta
    :return: noua lista fara apartamentul respectiv
    """
    return [cheltuiala for cheltuiala in lst if get_numar_apartament(cheltuiala) != numar_apartament]


def modifica_cheltuiala(numar_apartament, suma, zi, luna, an, intretinere, canal, alte_cheltuieli, lista):
    """
    modifica o cheltuiala dupa numar de apartament
    :param numar_apartament: string
    :param suma: float
    :param zi: int
    :param luna: int
    :param an: int
    :param intretinere: float
    :param canal: float
    :param alte_cheltuieli: float
    :param lista: o lista noua
    :return: o lista noua modificata pentru un nr de apartament
    """
    new_list = []
    for cheltuiala in lista:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            new_cheltuiala = creeaza_cheltuiala(numar_apartament, suma, zi, luna, an, intretinere, canal, alte_cheltuieli)
            new_list.append(new_cheltuiala)
        else:
            new_list.append(cheltuiala)
    return new_list
