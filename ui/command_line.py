from Logic.crud import adauga_cheltuiala, modifica_cheltuiala, sterge_cheltuiala
from domain.cheltuieli import to_string


def show_all(list_1):
    if bool(list_1) is False:
        print("Lista de cheltuieli este acum goala")
    else:
        for cheltuiala in list_1:
            print(to_string(cheltuiala))


def main_command_line(new_list_1):
    while True:
        print("Buna ziua! Aveti optiunea de a folosi o consola in care va sunt cerute datele inaintea adaugarii lor, iar alta in care le adaugati ca o lista,"
              "Daca doriti a folosi meniul in care le adaugati drept o lista, tastati 'help'. Altfel, tastati 'stop'"
              "si programul va va duce la meniul consola. Multumim!")
        message = input()
        if message == "help":
            print("add,id,numar_apartament,suma, data, tip - va adauga un element nou in lista de cheltuieli")
            print("update,id,numar_apartament,suma, data, tip - va modifica o cheltuiala existenta din lista")
            print("delete,id - va sterge elementul cu id-ul dat din lista")
            print("showall - va afisa toate elementele din lista curenta")
            print("stop - va opri programul")
        else:
            string = message.split(";")
            if string[0] == "stop":
                break
            else:
                for elemente in string:
                    new_element = elemente.split(",")
                    if new_element[0] == "add":
                        try:
                            new_list_1 = adauga_cheltuiala(new_element[1], int(new_element[2]), float(new_element[3]), new_element[4], new_element[5], new_list_1)
                        except ValueError:
                            print("Eroare! nu ati introdus un numar intreg pentru numarul de apartament sau un numar zecimal pentru suma, va rugam reincercati!")
                    elif new_element[0] == "update":
                        try:
                            new_list_1 = modifica_cheltuiala(new_element[1], int(new_element[2]), float(new_element[3]), new_element[4], new_element[5], new_list_1)
                        except ValueError:
                            print("Eroare! nu ati introdus un numar intreg pentru numarul de apartament sau un numar zecimal pentru suma, va rugam reincercati!")
                    elif new_element[0] == "showall":
                            show_all(new_list_1)
                    elif new_element[0] == "delete":
                        new_list_1 = sterge_cheltuiala(new_element[1], new_list_1)
                    else:
                        print("optiune invalida! Va rugam reincercati!")


new_list = []
main_command_line(new_list)
