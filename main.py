from agenda import add_contact, delete_contact, search_contact, get_phone_number, contact_exists


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
        while True:
            for contor, nume in enumerate(nume_gasite, start=1):
                print(contor, ".", nume)
            print("0. Revino la meniu.") 
            contor_ales = int(input("Introduceti un nr corespondent numelui ales: "))
            if contor_ales == 0:
                break
            nume_ales = nume_gasite[contor_ales - 1]
            numar_tel_ales = get_phone_number(nume_ales)
            print("+----------------------------+")
            print("Nume: ", nume_ales)
            print("Telefon: ", numar_tel_ales)
            print("+----------------------------+")
            input("Apasati Enter pt revenire la lista")
    elif meniu_ales == 3:
        nume_ales_stergere = input("Numele ales pt stergere: ")
        if contact_exists(nume_ales_stergere):
            delete_contact(nume_ales_stergere)
        else:
            print("Numele nu exista.")    
            


            
          








