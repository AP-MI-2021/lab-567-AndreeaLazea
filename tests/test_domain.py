from domain.cheltuieli import creeaza_cheltuiala, get_suma, get_id, get_data, get_tip
from domain.cheltuieli import get_numar_apartament


def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala(1, 23, 200, "1.3.2021", "150")
    assert get_id(cheltuiala) == 1
    assert get_suma(cheltuiala) == 200
    assert get_numar_apartament(cheltuiala) == 23
    assert get_data(cheltuiala) == "1.3.2021"
    assert get_tip(cheltuiala) == "150"
