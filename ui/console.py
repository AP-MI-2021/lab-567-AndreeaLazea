from Logic.crud import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala, \
    get_by_id
from Logic.functiionalitate import stergerea_tuturor_cheltuielilor, verificare_data, corectitudine_data, \
    ordonare_descrescatoare
from domain.cheltuieli import to_string


def print_menu():
    print("1.a - Adaugare cheltuiala")
    print("1.s - stergere cheltuiala")
    print("1.m - modificare cheltuiala")
    print("1.2 - Ștergerea tuturor cheltuielilor pentru un apartament dat.")
    print("1.3 - Adunarea unei valori la toate cheltuielile dintr-o dată citită.")
    print("1.4 - Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.")
    print("1.5 - Ordonarea cheltuielilor descrescător după sumă.")
    print("1.6 - Afișarea sumelor lunare pentru fiecare apartament.")
    print("1.7. Undo.")
    print("1.8 Redo")
    print("a. Afisare cheltuiala")
    print("x. iesire")


def ui_adaugare_cheltuiala(list_1):
    try:
        id_1 = input("dati id-ul cheltuielii")
        nr_apartament = int(input("dati numarul de apartament: "))
        suma = float(input("dati suma: "))
        data = input("data este: ")
        string_list = data
        tip = input("tipul cheltuielii este(întreținere/ canal/ alte cheltuieli): ")
        if len(string_list) != 10:
            print("Data nu este introdusa corect! va rugam urmati exemplul DD.MM.YYYY cu tot cu '.' . Daca "
                  "luna sau ziua este de o singura cifra(<=9) se va scrie cu tot cu 0 in fata. Spre exemplu, "
                  "luna 1 si ziua 1 a anului 2000"
                  "se va scrie 01.01.2000. Va vom intoarce la meniul principal.")
            return list_1
        elif corectitudine_data(data) is False:
            print("Data nu este introdusa corect! va reamintim ca data trebuie a fi "
                  "introdusa corect calendaristic, spre exemplu, luna <= 12, "
                  " iar zilele conform numarului de zile din luna respectiva.")
            return list_1
        return adauga_cheltuiala(id_1, nr_apartament, suma, data, tip, list_1)
    except ValueError:
        print("eroare! nu ati dat un numar intreg pentru id/numar apartament sau un numar zecimal pentru suma")
        return list_1


def ui_sterge_cheltuiala(list_1):
    id_1 = input("dati id-ul de la cheltuiala pe care doriti sa o stergeti: ")
    if get_by_id(id_1, list_1) is None:
        print("nu exista apartament cu id-ul dat de la tastatura, apartamentele valabile sunt: ")
        show_all(list_1)
        print("va vom intoarce la meniul principal!")
        return list_1
    else:
        return sterge_cheltuiala(id_1, list_1)


def ui_modifica_cheltuiala(list_1):
    try:
        id_1 = input("dati id-ul apartamentului de modificat: ")
        nr_apartament = int(input("dati numarul nou de apartament: "))
        suma = float(input("dati noua suma: "))
        data = input("data noua este: ")
        if corectitudine_data(data) is False:
            print("data nu este scrisa sub formatul corect. Va reamintim urmatoarele:"
                  " urmati exemplul DD.MM.YYYY cu tot cu '.' . Daca "
                  "luna sau ziua este de o singura cifra(<=9) se va scrie"
                  " cu tot cu 0 in fata. Spre exemplu, "
                  "luna 1 si ziua 1 a anului 2000"
                  "se va scrie 01.01.2000. Va vom intoarce la meniul principal.")
            return list_1
        tip = input("tipul nou este: ")
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


def ui_stergerea_tuturor_cheltuielilor(list_1):
    try:
        numar_apartament = int(input("dati numarul de apartament pe care doriti sa il stergeti: "))
        return stergerea_tuturor_cheltuielilor(numar_apartament, list_1)
    except ValueError:
        print(
            "EROARE! Nu ati introdus un numar intreg pentru"
            "numarul de apartament! Va vom intoarce la meniul principal!")
        return list_1


def ui_verificare_data(list_1):
    data_tastatura = input("dati data de la tastatura, in format DD.MM.YYYY cu tot cu '.' . "
                           "SPRE EXEMPLU: daca ziua sau luna este 1/2/3/etc(<=9), va rugam sa precizati "
                           "sub forma 01/02/03/etc")
    try:
        number = float(input("dati un numar, pe care doriti sa il adaugat la suma din data ceruta"))
    except ValueError:
        print("ati dat o valoare gresita pentru numar! va rog reincercati")
        return list_1
    if verificare_data(data_tastatura, list_1, number) == []:
        print("ati dat o valoare gresita la data de la tastatura! va rugam reincercati!")
        return list_1
    else:
        return verificare_data(data_tastatura, list_1, number)


def ui_ordonare_descrescatoare(list_1):
    return ordonare_descrescatoare(list_1)


def run_menu(list_1):
    while True:
        print_menu()
        option = input("dati optiunea")
        if option == "1.a":
            list_1 = ui_adaugare_cheltuiala(list_1)
        elif option == "1.s":
            list_1 = ui_sterge_cheltuiala(list_1)
        elif option == "1.m":
            list_1 = ui_modifica_cheltuiala(list_1)
        elif option == 'a':
            show_all(list_1)
        elif option == '1.2':
            list_1 = ui_stergerea_tuturor_cheltuielilor(list_1)
        elif option == '1.3':
            list_1 = ui_verificare_data(list_1)
        elif option == '1.4':
            print("ne cerem scuze, functia nu este inca finisata! Va rugam sa reveniti!")
        elif option == '1.5':
            list_1 = ui_ordonare_descrescatoare(list_1)
        elif option == '1.6':
            print("ne cerem scuze, functia nu este inca finisata! Va rugam sa reveniti!")
        elif option == '1.7':
            print("ne cerem scuze, functia nu este inca finisata! Va rugam sa reveniti!")
        elif option == '1.8':
            print("ne cerem scuze, functia nu este inca finisata! Va rugam sa reveniti!")
        elif option == 'x':
            break
        else:
            print("optiune invalida, reincercati!")
