from tests.test_crud import test_adauga_cheltuieli, test_sterge_cheltuiala
from tests.test_domain import test_cheltuiala
from tests.test_functionalitate import test_stergerea_tuturor_cheltuielilor, test_verificare_data, \
    test_corectitudine_data, test_ordonare_descrescatoare


def run_all_tests():
    test_cheltuiala()
    test_adauga_cheltuieli()
    test_sterge_cheltuiala()
    test_stergerea_tuturor_cheltuielilor()
    test_verificare_data()
    test_corectitudine_data()
    test_ordonare_descrescatoare()
