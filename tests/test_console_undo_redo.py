from Logic.crud import adauga_cheltuiala


def test_add_undo_redo():
    undo = []
    redo = []
    lst = []
    lst = adauga_cheltuiala(1, 25, 200, "03.05.2021", "canal", lst)
    undo.append(lst)
    lst = adauga_cheltuiala(2, 25, 200.5, "03.05.2021", "canal", lst)
    undo.append(lst)
    lst = adauga_cheltuiala(3, 24, 140, "03.05.2020", "alte cheltuieli", lst)
    undo.append(lst)
    if len(undo) > 0:
        redo.append(lst)
        list_1 = undo.pop()
    elif len(undo) <= 0:
        print("nu se poate realiza undo la o lista goala")
    if len(redo) > 0:
        undo.append(list_1)
        list_1 = redo.pop()
    elif len(redo) <= 0:
        print("nu se poate realiza redo la o lista goala")

    assert lst == [[1, 25, 200, "03.05.2021", "canal", lst], [2, 25, 200.5, "03.05.2021", "canal", lst]]

