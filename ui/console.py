from Logic.crud import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala
import Logic.functiionalitate
from domain.cheltuieli import to_string, get_id


def print_menu():
    print("1.a - Adaugare cheltuiala")
    print("1.s - stergere cheltuiala")
    print("1.m - modificare cheltuiala")
    print("1.2 - Ștergerea tuturor cheltuielilor pentru un apartament dat.")
    print("1.3 - Adunarea unei valori la toate cheltuielile dintr-o dată citită.")
    print("1.4 - Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("1.5 - Ordonarea cheltuielilor descrescător după sumă.")
    print("1.6 - Afișarea sumelor lunare pentru fiecare apartament.")
    print("1.7 - Undo.")
    print("1.8 - Redo")
    print("a. Afisare cheltuiala")
    print("x. iesire")


def ui_adaugare_cheltuiala(list_1, undo, redo):
    try:
        id_1 = input("dati id-ul cheltuielii")
        for cheltuiala in list_1:
            if get_id(cheltuiala) == id_1:
                print("ID invalid, deja exista un apartament cu acest id! Va rugam reincercati!")
                return list_1
        nr_apartament = int(input("dati numarul de apartament: "))
        suma = float(input("dati suma: "))
        data = input("data este: ")
        string_list = data
        tip = input("tipul cheltuielii este(întreținere/ canal/ alte cheltuieli): ")
        list_check = ["canal", "intretinere", "alte cheltuieli"]
        bool_check = 0
        for x in list_check:
            if x == tip:
                bool_check = 1
        if bool_check == 0:
            print("Eroare! Ati introdus un tip gresit! Va rog reincercati cu: întreținere/ canal/ alte cheltuieli ")
            return list_1
        if len(string_list) != 10:
            print("Data nu este introdusa corect! va rugam urmati exemplul DD.MM.YYYY cu tot cu '.' . Daca "
                  "luna sau ziua este de o singura cifra(<=9) se va scrie cu tot cu 0 in fata. Spre exemplu, "
                  "luna 1 si ziua 1 a anului 2000"
                  "se va scrie 01.01.2000. Va vom intoarce la meniul principal.")
            return list_1
        elif Logic.functiionalitate.corectitudine_data(data) is False:
            print("Data nu este introdusa corect! va reamintim ca data trebuie a fi "
                  "introdusa corect calendaristic, spre exemplu, luna <= 12, "
                  " iar zilele conform numarului de zile din luna respectiva.")
            return list_1
        undo.append(list_1)
        redo.clear()
        return adauga_cheltuiala(id_1, nr_apartament, suma, data, tip, list_1)
    except ValueError:
        print("eroare! nu ati dat un numar intreg pentru id/numar apartament sau un numar zecimal pentru suma")
        return list_1


def ui_sterge_cheltuiala(list_1, undo, redo):
    id_1 = input("dati id-ul de la cheltuiala pe care doriti sa o stergeti: ")
    try:
        undo.append(list_1)
        redo.clear()
        return sterge_cheltuiala(id_1, list_1)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        show_all(list_1)
        return list_1


def ui_modifica_cheltuiala(list_1, undo, redo):
    try:
        id_1 = input("dati id-ul apartamentului de modificat: ")
        nr_apartament = int(input("dati numarul nou de apartament: "))
        suma = float(input("dati noua suma: "))
        data = input("data noua este: ")
        if Logic.functiionalitate.corectitudine_data(data) is False:
            print("data nu este scrisa sub formatul corect. Va reamintim urmatoarele:"
                  " urmati exemplul DD.MM.YYYY cu tot cu '.' . Daca "
                  "luna sau ziua este de o singura cifra(<=9) se va scrie"
                  " cu tot cu 0 in fata. Spre exemplu, "
                  "luna 1 si ziua 1 a anului 2000"
                  "se va scrie 01.01.2000. Va vom intoarce la meniul principal.")
            return list_1
        tip = input("tipul nou este: ")
        list_check = ["canal", "intretinere", "alte cheltuieli"]
        bool_check = 0
        for x in list_check:
            if x == tip:
                bool_check = 1
        if bool_check == 0:
            print("Eroare! Ati introdus un tip gresit! Va rog reincercati cu: întreținere/ canal/ alte cheltuieli ")
            return list_1
        undo.append(list_1)
        redo.clear()
        return modifica_cheltuiala(id_1, nr_apartament, suma, data, tip, list_1)
    except ValueError:
        print("eroare! nu ati dat un numar intreg pentru numar de apartament"
              "sau un numar zecimal pentru suma! va vom intoarce la meniul principal")
        return list_1


def show_all(list_1):
    if bool(list_1) is False:
        print("Lista de cheltuieli este acum goala")
    else:
        for cheltuiala in list_1:
            print(to_string(cheltuiala))


def ui_stergerea_tuturor_cheltuielilor(list_1, undo, redo):
    try:
        numar_apartament = int(input("dati numarul de apartament pe care doriti sa il stergeti: "))
        undo.append(list_1)
        redo.clear()
        return Logic.functiionalitate.stergerea_tuturor_cheltuielilor(numar_apartament, list_1)
    except ValueError:
        print(
            "EROARE! Nu ati introdus un numar intreg pentru"
            "numarul de apartament! Va vom intoarce la meniul principal!")
        return list_1


def ui_verificare_data(list_1, undo, redo):
    data_tastatura = input("dati data de la tastatura, in format DD.MM.YYYY cu tot cu '.' . "
                           "SPRE EXEMPLU: daca ziua sau luna este 1/2/3/etc(<=9), va rugam sa precizati "
                           "sub forma 01/02/03/etc")
    try:
        number = float(input("dati un numar, pe care doriti sa il adaugat la suma din data ceruta"))
    except ValueError:
        print("ati dat o valoare gresita pentru numar! va rog reincercati")
        return list_1
    if Logic.functiionalitate.verificare_data(data_tastatura, list_1, number) == []:
        print("ati dat o valoare gresita la data de la tastatura! va rugam reincercati!")
        return list_1
    else:
        rezultat = Logic.functiionalitate.verificare_data(data_tastatura, list_1, number)
        undo.append(list_1)
        redo.clear()
        return rezultat


def ui_ordonare_descrescatoare(list_1, undo, redo):
    undo.append(list_1)
    redo.clear()
    return Logic.functiionalitate.ordonare_descrescatoare(list_1)


def ui_cea_mai_mare_cheltuiala(list_1):
    try:
        return Logic.functiionalitate.cea_mai_mare_cheltuiala(list_1)
    except ValueError as ve:
        print("Eroare: {}".format(ve))


def ui_suma_lunara_ap(list_1):
    dictionary = Logic.functiionalitate.suma_lunara_ap(list_1)
    for numar_ap in dictionary:
        for year in dictionary[numar_ap]:
            for month in dictionary[numar_ap][year]:
                print("Apartamentul {} are cheltuieli in valoare de {} in anul {} si respectiv luna {} ".format(
                    numar_ap,
                    dictionary[numar_ap][year][month],
                    year,
                    month
                ))


def run_menu(list_1):
    undo = []
    redo = []
    while True:
        print_menu()
        option = input("dati optiunea")
        if option == "1.a":
            list_1 = ui_adaugare_cheltuiala(list_1, undo, redo)
        elif option == "1.s":
            list_1 = ui_sterge_cheltuiala(list_1, undo, redo)
        elif option == "1.m":
            list_1 = ui_modifica_cheltuiala(list_1, undo, redo)
        elif option == 'a':
            show_all(list_1)
        elif option == '1.2':
            list_1 = ui_stergerea_tuturor_cheltuielilor(list_1, undo, redo)
        elif option == '1.3':
            list_1 = ui_verificare_data(list_1, undo, redo)
        elif option == '1.4':
            print(ui_cea_mai_mare_cheltuiala(list_1))
        elif option == '1.5':
            list_1 = ui_ordonare_descrescatoare(list_1, undo, redo)
        elif option == '1.6':
            print(ui_suma_lunara_ap(list_1))
        elif option == '1.7':
            if len(undo) > 0:
                redo.append(list_1)
                list_1 = undo.pop()
            else:
                print("nu se poate realiza undo la o lista goala")
        elif option == '1.8':
            if len(redo) > 0:
                undo.append(list_1)
                list_1 = redo.pop()
            else:
                print("nu se poate realiza redo la o lista goala")
        elif option == 'x':
            break
        else:
            print("optiune invalida, reincercati!")
