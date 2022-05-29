from agenda import add_contact, search_contact


while True:
    print("Meniu:")
    print("1. adauga contact")
    print("2. cauta contact")
    print("3. sterge contact")
    print("0. Iesire")

    meniu_ales = int(input("Alege un numar:"))
    if meniu_ales == 0:
        break

    if meniu_ales == 1:
        adauga_nr = "da"
        while adauga_nr == "da":
            nume = input("Nume:")
            nr_telefon = input("Nr. telefon:")
            add_contact(nume, nr_telefon)
            adauga_nr = input("Doriti sa adaugati un nr. nou? ")
    elif meniu_ales == 2:  
        litere_introduse = input("Introduceti cateva litere: ")
        nume_gasite = search_contact(litere_introduse)
        for nume, contor in enumerate(nume_gasite):
            print(contor + "." + nume)
        print("0. Revino la meniu.")   
         







