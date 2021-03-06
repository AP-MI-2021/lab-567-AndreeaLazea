from Logic.crud import adauga_cheltuiala
from Logic.functiionalitate import stergerea_tuturor_cheltuielilor, verificare_data, corectitudine_data, \
    ordonare_descrescatoare, cea_mai_mare_cheltuiala, suma_lunara_ap


def test_stergerea_tuturor_cheltuielilor():
    lst = []
    lst = adauga_cheltuiala(1, 25, 200, "3, 5, 2021"," ", lst)
    lst = adauga_cheltuiala(2, 25, 200, "3, 5, 2021", " ", lst)
    lst = adauga_cheltuiala(3, 25, 200, "3, 5, 2021", " ", lst)
    lst = adauga_cheltuiala(4, 24, 200, "3, 5, 2021", " ", lst)
    lst = stergerea_tuturor_cheltuielilor(25, lst)
    assert [[4, 24, 200, "3, 5, 2021", " "]] == lst
    lst = stergerea_tuturor_cheltuielilor(24, lst)
    assert lst == []


def test_verificare_data():
    lst = []
    lst = adauga_cheltuiala(1, 25, 200, "03.05.2021", " ", lst)
    lst = adauga_cheltuiala(2, 25, 200, "03.05.2021", " ", lst)
    lst = adauga_cheltuiala(3, 24, 200, "03.05.2021", " ", lst)
    lst = adauga_cheltuiala(4, 24, 200, "04.05, 2021", " ", lst)
    data_tastatura = "02.03.2021"
    lst = verificare_data(data_tastatura, lst, 5)
    assert lst == [[1, 25, 200, '03.05.2021', ' '], [2, 25, 200, '03.05.2021', ' '], [3, 24, 200, '03.05.2021', ' '], [4, 24, 200, '04.05, 2021', ' ']]
    lst = verificare_data('03.05.2021', lst, 10)
    assert lst == [[1, 25, 210, '03.05.2021', ' '], [2, 25, 210, '03.05.2021', ' '], [3, 24, 210, '03.05.2021', ' '], [4, 24, 200, '04.05, 2021', ' ']]



def test_corectitudine_data():
    assert corectitudine_data("22.30.2002") is False
    assert corectitudine_data("31.04.2002") is False
    assert corectitudine_data("30.03.2002") is True


def test_ordonare_descrescatoare():
    lst = []
    lst = adauga_cheltuiala(1, 25, 200, "03.05.2021", " ", lst)
    lst = adauga_cheltuiala(2, 25, 200.5, "03.05.2021", " ", lst)
    lst = adauga_cheltuiala(3, 24, 140, "03.05.2021", " ", lst)
    lst = ordonare_descrescatoare(lst)
    assert lst == [[2, 25, 200.5, "03.05.2021", ' '], [1, 25, 200, "03.05.2021", ' '], [3, 24, 140, "03.05.2021", ' ']]


def test_cea_mai_mare_cheltuiala():
    lst = []
    lst = adauga_cheltuiala(1, 25, 200, "03.05.2021", "canal", lst)
    lst = adauga_cheltuiala(2, 25, 200.5, "03.05.2021", "canal", lst)
    lst = adauga_cheltuiala(3, 24, 140, "03.05.2021", "alte cheltuieli", lst)
    lst = adauga_cheltuiala(4, 25, 150, "09.10.2021", "intretinere", lst)
    assert cea_mai_mare_cheltuiala(lst) == ["canal"]


def test_suma_lunara_ap():
    lst = []
    lst = adauga_cheltuiala(1, 25, 200, "03.05.2021", "canal", lst)
    lst = adauga_cheltuiala(2, 25, 200.5, "03.05.2021", "canal", lst)
    lst = adauga_cheltuiala(3, 24, 140, "03.05.2020", "alte cheltuieli", lst)
    lst = adauga_cheltuiala(4, 25, 150, "05.05.2020", "intretinere", lst)
    lst = adauga_cheltuiala(4, 25, 150, "09.10.2021", "intretinere", lst)
    assert suma_lunara_ap(lst) == {25: {'2021': {5: 400.5, 10: 150}, '2020': {5: 150}}, 24: {'2020': {5: 140}}}
