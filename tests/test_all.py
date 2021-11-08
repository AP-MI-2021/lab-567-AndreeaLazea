from tests.test_crud import test_adauga_cheltuieli, test_sterge_cheltuiala
from tests.test_domain import test_cheltuiala
from tests.test_functionalitate import test_stergerea_tuturor_cheltuielilor, test_verificare_data, \
    test_corectitudine_data, test_ordonare_descrescatoare, test_cea_mai_mare_cheltuiala, test_suma_lunara_ap
from tests.test_undo_redo import test_undo_redo


def run_all_tests():
    test_cheltuiala()
    test_adauga_cheltuieli()
    test_sterge_cheltuiala()
    test_stergerea_tuturor_cheltuielilor()
    test_verificare_data()
    test_corectitudine_data()
    test_ordonare_descrescatoare()
    test_cea_mai_mare_cheltuiala()
    test_suma_lunara_ap()
    test_undo_redo()
