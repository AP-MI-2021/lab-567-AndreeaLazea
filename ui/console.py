from Logic.crud import adauga_cheltuiala, sterge_cheltuiala, modifica_cheltuiala, \
    get_by_number
from domain.cheltuieli import to_string


def print_menu():
    print("1.a - Adaugare cheltuiala")
    print("1.s - stergere cheltuiala")
    print("1.m - modificare cheltuiala")
    print("a. Afisare cheltuiala")
    print("x. iesire")


def ui_adaugare_cheltuiala(list_1):
    try:
        nr_apartament = input("dati numarul de apartament: ")
        suma = int(input("dati suma: "))
        zi = int(input("dati ziua: "))
        luna = int(input("dati luna: "))
        anul = int(input("dati anul: "))
        intretinere = int(input("dati intretinerea: "))
        canal = int(input("dati cheltuiala pentru canalizare: "))
        alte_cheltuieli = int(input("dati alte cheltuieli: "))
        return adauga_cheltuiala(nr_apartament, suma, zi, luna, anul, intretinere, canal, alte_cheltuieli, list_1)
    except ValueError:
        print("eroare! nu ati dat un numar intreg pentru zi/ luna/ an sau un numar zecimal pentru suma/ "
              "intretinere/ canal/ alte cheltuieli")
        return list_1


def ui_sterge_cheltuiala(list_1):
    nr_apartament = input("dati numarul de apartament pe care doriti sa-l stergeti stergere: ")
    if get_by_number(nr_apartament, list_1) is None:
        print("nu exista apartament cu numarul dat de la tastatura, apartamentele valabile sunt: ")
        show_all(list_1)
        continuare = input("doriti sa reincercati cu un alt apartament valid? Scrieti DA/NU")
        if continuare == "DA":
            ui_sterge_cheltuiala(list_1)
        else:
            return list_1
    else:
        return sterge_cheltuiala(nr_apartament, list_1)


def ui_modifica_cheltuiala(list_1):
    nr_apartament = input("dati numarul de apartament al apartamentului de modificat: ")
    if get_by_number(nr_apartament, list_1) is None:
        print("nu exista apartament cu numarul dat de la tastatura, apartamentele valabile sunt: ")
        show_all(list_1)
        continuare = input("doriti sa reincercati cu un alt apartament valid? Scrieti DA/NU")
        if continuare == "DA":
            ui_modifica_cheltuiala(list_1)
        elif continuare == "NU":
            return list_1
        else:
            print("optiune invalida! Va vom intoarce la meniul principal")
            return list_1
    else:
        try:
            suma = int(input("dati noua suma: "))
            zi = int(input("dati noua ziua: "))
            luna = int(input("dati noua luna: "))
            anul = int(input("dati noul an: "))
            intretinere = int(input("dati noua intretinere: "))
            canal = int(input("dati noua cheltuiala: "))
            alte_cheltuieli = int(input("dati noile alte cheltuieli: "))
            return modifica_cheltuiala(nr_apartament, suma, zi, luna, anul, intretinere, canal, alte_cheltuieli, list_1)
        except ValueError:
            print("eroare! nu ati dat un numar intreg pentru zi/ luna/ an sau un numar zecimal pentru suma/ "
                  "intretinere/ canal/ alte cheltuieli")
            return list_1


def show_all(list_1):
    if bool(list_1) is False:
        print("Lista de cheltuieli este acum goala")
    else:
        for cheltuiala in list_1:
            print(to_string(cheltuiala))


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
        elif option == 'x':
            break
        else:
            print("optiune invalida, reincercati!")
