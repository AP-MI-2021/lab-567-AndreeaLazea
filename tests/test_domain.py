from domain.cheltuieli import creeaza_cheltuiala, get_alte_cheltuieli, get_suma
from domain.cheltuieli import get_canal, get_data_an, get_data_luna, get_data_zi, get_intretinere, get_numar_apartament

def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala(23, 200, 1, 3, 2021, 50, 30, 150)
    assert get_alte_cheltuieli(cheltuiala) == 150
    assert get_canal(cheltuiala) == 30
    assert get_intretinere(cheltuiala) == 50
    assert get_data_an(cheltuiala) == 2021
    assert get_data_luna(cheltuiala) == 3
    assert get_data_zi(cheltuiala) == 1
    assert get_suma(cheltuiala) == 200
    assert get_numar_apartament(cheltuiala) == 23

