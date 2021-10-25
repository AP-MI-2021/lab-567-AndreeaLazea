from domain.cheltuieli import get_suma
from domain.cheltuieli import get_data_luna, get_data_zi, get_numar_apartament
from Logic.crud import adauga_cheltuiala, sterge_cheltuiala, get_by_number


def test_adauga_cheltuieli():
    lst = []
    lst = adauga_cheltuiala(23, 200, 1, 3, 2021, 50, 30, 150, lst)
    assert len(lst) == 1
    assert get_suma(lst[0]) == 200
    assert get_numar_apartament(lst[0]) == 23
    assert get_data_luna(lst[0]) == 3
    assert get_data_zi(lst[0]) == 1


def test_sterge_cheltuiala():
    lst = []
    lst = adauga_cheltuiala("25", 200, 3, 5, 2021, 50, 30, 50, lst)
    lst = adauga_cheltuiala("24", 200, 3, 5, 2021, 50, 30, 50, lst)
    lst = sterge_cheltuiala("24", lst)
    assert len(lst) == 1
    assert get_by_number("24", lst) is None
    assert get_by_number("25", lst) is not None


def test_get_by_number():
    lst = []
    lst = adauga_cheltuiala("25", 200, 3, 5, 2021, 50, 30, 50, lst)
    assert get_numar_apartament(get_by_number("25", lst)) == "25"
