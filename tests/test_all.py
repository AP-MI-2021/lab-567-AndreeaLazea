from tests.test_crud import test_adauga_cheltuieli, test_sterge_cheltuiala
from tests.test_domain import test_cheltuiala


def run_all_tests():
    test_cheltuiala()
    test_adauga_cheltuieli()
    test_sterge_cheltuiala()
