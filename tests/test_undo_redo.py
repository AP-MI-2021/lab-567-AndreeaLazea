from Logic.crud import adauga_cheltuiala


def test_undo_redo():
    lst = []
    'Pas 1. Creearea unei liste goale'
    undo_list = []
    redo_list = []
    'pas 2. Adaugarea a unei cheltuieli/ Primul obiect adaugat'
    cheltuiala = adauga_cheltuiala(1, 25, 200, "3, 5, 2021", " ", lst)
    undo_list.append(lst)
    lst = cheltuiala
    cheltuiala = adauga_cheltuiala(2, 25, 200, "3, 5, 2021", " ", lst)
    undo_list.append(lst)
    lst = cheltuiala
    cheltuiala = adauga_cheltuiala(3, 25, 200, "3, 5, 2021", " ", lst)
    undo_list.append(lst)
    lst = cheltuiala
    'Pas 3. Primul undo -> vor ramane doar primele doua cheltuieli'
    redo_list.append(lst)
    lst = undo_list.pop()
    assert lst == [[1, 25, 200, "3, 5, 2021", " "], [2, 25, 200, "3, 5, 2021", " "]]
    'Pas 4. Al doilea undo -> ramane un singur element'
    redo_list.append(lst)
    lst = undo_list.pop()
    assert lst == [[1, 25, 200, "3, 5, 2021", " "]]
    'Pas 5. Undo -> Ramane lista de elemente goala'
    redo_list.append(lst)
    lst = undo_list.pop()
    assert lst == []
    'Pas 6. Undo -> lista ramane inca goala '
    if len(undo_list) > 0:
        redo_list.append(lst)
        lst = undo_list.pop()
    assert lst == []
    'Pas 7. Adaugam trei obiecte'
    cheltuiala = adauga_cheltuiala(1, 25, 200, "3, 5, 2021", " ", lst)
    undo_list.append(lst)
    lst = cheltuiala
    redo_list.clear()
    cheltuiala = adauga_cheltuiala(2, 25, 200, "3, 5, 2021", " ", lst)
    undo_list.append(lst)
    lst = cheltuiala
    cheltuiala = adauga_cheltuiala(3, 25, 200, "3, 5, 2021", " ", lst)
    undo_list.append(lst)
    lst = cheltuiala
    'Pas 8. Redo ->  nu face nimic'
    if len(redo_list) > 0:
        undo_list.append(lst)
        lst = redo_list.pop()
    assert lst == [[1, 25, 200, "3, 5, 2021", " "], [2, 25, 200, "3, 5, 2021", " "], [3, 25, 200, "3, 5, 2021", " "]]
    'Pas 9. Undo & Undo -> va ramane doar primul element'
    redo_list.append(lst)
    lst = undo_list.pop()
    redo_list.append(lst)
    lst = undo_list.pop()
    assert lst == [[1, 25, 200, "3, 5, 2021", " "]]
    'Pas 10. Redo -> Ne vom intoarce la doua elemente'
    if len(redo_list) > 0:
        undo_list.append(lst)
        lst = redo_list.pop()
    assert lst == [[1, 25, 200, "3, 5, 2021", " "], [2, 25, 200, "3, 5, 2021", " "]]
    'Pas 11. Redo -> 3 elemente'
    if len(redo_list) > 0:
        undo_list.append(lst)
        lst = redo_list.pop()
    assert lst == [[1, 25, 200, "3, 5, 2021", " "], [2, 25, 200, "3, 5, 2021", " "], [3, 25, 200, "3, 5, 2021", " "]]
    'Pas 12. Undo & Undo -> un singur element ramas'
    redo_list.append(lst)
    lst = undo_list.pop()
    redo_list.append(lst)
    lst = undo_list.pop()
    assert lst == [[1, 25, 200, "3, 5, 2021", " "]]
    'Pas 13. Adauga obiect nou -> Obiect 4'
    cheltuiala = adauga_cheltuiala(4, 25, 150, "05.05.2020", "intretinere", lst)
    undo_list.append(cheltuiala)
    lst = cheltuiala
    redo_list.clear()
    'Pas 14. Redo -> nu ar trebui sa faca nimic'
    if len(redo_list) > 0:
        undo_list.append(lst)
        lst = redo_list.pop()
    assert lst == [[1, 25, 200, "3, 5, 2021", " "], [4, 25, 150, "05.05.2020", "intretinere"]]
    'Pas 15. Undo & Undo -> lista goala'
    redo_list.append(lst)
    lst = undo_list.pop()
    redo_list.append(lst)
    lst = undo_list.pop()
    assert lst == []
    'Pas 16. Redo & Redo -> readauga elementele in lista'
    if len(redo_list) > 0:
        undo_list.append(lst)
        lst = redo_list.pop()
    if len(redo_list) > 0:
        undo_list.append(lst)
        lst = redo_list.pop()
    assert lst == [[1, 25, 200, "3, 5, 2021", " "], [4, 25, 150, "05.05.2020", "intretinere"]]
    'Pas 16. Redo -> nu face nimic'
    if len(redo_list) > 0:
        undo_list.append(lst)
        lst = redo_list.pop()
    assert lst == [[1, 25, 200, "3, 5, 2021", " "], [4, 25, 150, "05.05.2020", "intretinere"]]
