from domain.cheltuieli import get_suma, get_id
from domain.cheltuieli import get_data
from Logic.crud import adauga_cheltuiala, sterge_cheltuiala, get_by_id


def test_adauga_cheltuieli():
    lst = []
    lst = adauga_cheltuiala(1, 23, 200, "1.3.2021", 50, lst)
    assert len(lst) == 1
    assert get_suma(lst[0]) == 200
    assert get_id(lst[0]) == 1
    assert get_data(lst[0]) == "1.3.2021"


def test_sterge_cheltuiala():
    lst = []
    lst = adauga_cheltuiala("1", "25", 200, "3, 5, 2021", 50, lst)
    lst = adauga_cheltuiala("2", "24", 200, "3, 5, 2021", 30, lst)
    lst = sterge_cheltuiala("2", lst)
    assert len(lst) == 1
    assert get_by_id("1", lst) is not None


def test_get_by_number():
    lst = []
    lst = adauga_cheltuiala("1", "25", 200, "3, 5, 2021", 50, lst)
    assert get_id(get_by_id("1", lst)) == "1"
